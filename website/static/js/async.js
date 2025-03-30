class Async {
  constructor() {
    this.updateTaskStatus();
    this.deleteTask();

  }


  getCSRFToken() {
    const token = document.querySelector("[name=csrfmiddlewaretoken]") ||
      document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute('content') || token.value : '';
  }


  deleteTask() {
    document.addEventListener("DOMContentLoaded", () => {
      document.querySelectorAll("a.bg-red-600.rounded-md.p-2.flex.items-center.shadow-xs.shadow-red-600\\/50.hover\\:text-white").forEach((anchor) => {
        anchor.addEventListener("click", (event) => {
          const closestDiv = event.target.closest("div[id]");
          if (!closestDiv) {
            console.error("Div com ID não encontrada!");
            return;
          }
          const urlId = closestDiv.id;

          if (confirm(`Deseja excluir a tarefa #${urlId}?`)) {
            fetch(`excluir/${urlId}/`, {
              method: "DELETE",
              headers: {
                "X-CSRFToken": this.getCSRFToken(),
                "Content-Type": "application/json",
              }
            })
              .then(response => response.json())
              .then(data => {
                if (data.status === "success") {
                  const taskContainer = document.getElementById(urlId);
                  if (taskContainer) {
                    taskContainer.parentNode.removeChild(taskContainer);
                  } else {
                    console.error("Elemento não encontrado no DOM!");
                  }
                } else {
                  console.error("Erro no servidor ao excluir a tarefa.");
                }
              })
              .catch(error => {
                console.error("Erro ao excluir tarefa: " + error);
              });
          }
        });
      });
    });
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
