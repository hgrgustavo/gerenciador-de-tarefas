class Async {
  constructor() {
    this.updateTaskStatus();

  }

  getCSRFToken() {
    const token = document.querySelector("[name=csrfmiddlewaretoken]") ||
      document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute('content') || token.value : '';
  }


  deleteTask(urlId) {
    if (confirm("Deseja excluir este item?")) {
      fetch(`excluir/${urlId}/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": this.getCSRFToken(),
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.status === "success") {
            const elementToDelete = document.getElementById(urlId);

            if (elementToDelete) {
              elementToDelete.remove();
              alert("Tarefa deletada com sucesso!");
            } else {
              console.error("Elemento não encontrado no DOM!");
            }
          }
        })
        .catch(error => {
          alert("Ocorreu um erro ao tentar excluir a tarefa.");
          console.error("Erro ao deletar: ", error);
        });
    }
  }

  updateTaskStatus() {
    document.addEventListener("DOMContentLoaded", () => {
      document.querySelectorAll("button[class]").forEach((button) => {
        button.addEventListener("click", (event) => {
          const selectElement = event.target.closest("div").querySelector("select");
          const newStatus = selectElement ? selectElement.value : null;

          if (newStatus) {
            if (confirm(`Atualizar status para ${newStatus}?`)) {
              const urlId = event.target.closest("div[id]").id;

              fetch(`atualizar-status/${urlId}/`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": this.getCSRFToken(),
                },
                body: JSON.stringify({ status: newStatus }),
              })
                .then(response => response.json())
                .then(data => {
                  if (data.success) {
                    const taskContainer = document.getElementById(urlId);
                    taskContainer.parentNode.removeChild(taskContainer);

                    const newColumn = document.getElementById(`coluna-${newStatus}`)
                    newColumn.appendChild(taskContainer);

                    alert("Status atualizado com sucesso!");
                  } else {
                    alert("Falha ao atualizar o status.");
                  }
                })
                .catch(error => {
                  console.error("Erro ao atualizar o status: ", error);
                  alert("Ocorreu um erro.");
                });
            }
          }
        });
      });
    });
  }

}

const async = new Async();
