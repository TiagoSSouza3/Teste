var current_page = ""
var header_text = document.getElementById("header_text");

function lista_de_alunos(){
    current_page = "Lista de Alunos"
    header_text.innerHTML = current_page
}

function cadastrar_aluno(){
    current_page = "Cadastrar Alunos"
    header_text.innerHTML = current_page
}

function remover_alunos(){
    current_page = "Remover Alunos"
    header_text.innerHTML = current_page
}

