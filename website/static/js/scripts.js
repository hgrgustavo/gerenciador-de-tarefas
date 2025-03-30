class Scripts {
  constructor() {

  }

  removeSelectDashes(selectId) {
    document.addEventListener("DOMContentLoaded", () => {
      const select = document.getElementById(selectId);
      if (select && select.options.length > 0) {
        select.remove(0);
        console.log("Dashes removidos com sucesso!");
      } else {
        console.error("O elemento select não foi encontrado ou está vazio.");
      }
    });
  }
}

const rmsd_usuario = new Scripts().removeSelectDashes("usuario__select");
const rmsd_prioridade = new Scripts().removeSelectDashes("prioridade__select");

