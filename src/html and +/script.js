var current_page = ""
var header_text = document.getElementById("header_text");

class Alunos{
    nome = ""
    data_nascimento = null
    cpf = 0
    prontuario = ""
    constructor(nome, ano, mes, dia, cpf) {
        this.nome = nome
        this.data_nascimento = new Date(ano, mes, dia)
        this.cpf = cpf
        this.prontuario = gerar_prontuario()
    }
}

let numero_prontuario = "0000000";
function gerar_prontuario() {
    let numero_final = numero_prontuario.split("");
    for (let index = numero_final.length - 1; index >= 0; index--) {
        if (numero_final[index] !== "9") {
            numero_final[index] = String(parseInt(numero_final[index]) + 1);
            break;
        } else {
            numero_final[index] = "0";
        }
    }

    numero_prontuario = numero_final.join("");
    return "SP" + numero_prontuario;
}

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
