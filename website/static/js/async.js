class Async {
  constructor() {
    document.addEventListener("DOMContentLoaded", () => {
      this.deleteTask();

    })
  }

  getCSRFToken() {
    const token = document.querySelector("[name=csrfmiddlewaretoken]") ||
      document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute('content') || token.value : '';
  }

  deleteTask() {
    document.getElementById("delete-anchor").addEventListener("click", (event) => {
      if (confirm("Deseja excluir este item?")) {
        const urlId = event.target.closest("div[id]").id;

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
          })
      }
    })
  }
}

const async = new Async();
