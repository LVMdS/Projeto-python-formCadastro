# Projeto-python-formCadastro

Documentação Simples e Objetiva: Cadastro de Clientes

O código apresentado implementa um sistema de cadastro de clientes utilizando a biblioteca tkinter em Python. Abaixo, fornecemos uma breve documentação para entender as principais funcionalidades e estrutura do código.

Estrutura da Classe: CadastroClientes
Método __init__:

Inicializa a interface gráfica e as variáveis para armazenar os dados do cliente.
Define elementos da GUI, como rótulos, entradas de texto e botão de cadastro.
Métodos de Validação (validar_telefone, validar_numero, validar_cep, validar_idade):

Realizam validações específicas para os campos de telefone, número, CEP e idade.
São utilizados como comandos de validação nas entradas de texto.
Método cadastrar_cliente:

Obtém dados do formulário, verifica o preenchimento e formata o telefone.
Chama o método adicionar_cliente_csv para salvar os dados em um arquivo CSV.
Exibe mensagens de sucesso ou aviso, limpa os campos do formulário.
Método adicionar_cliente_csv:

Adiciona os dados do cliente a um arquivo CSV chamado "clientes.csv".
Verifica se o arquivo está vazio e escreve o cabeçalho se necessário.
Uso Principal (__main__):
Cria uma instância da classe CadastroClientes e inicia a interface gráfica.
Observações:
A interface gráfica utiliza a biblioteca tkinter para criar rótulos, entradas e botões.
Há validações simples nos campos de telefone, número, CEP e idade para garantir dados adequados.
Os dados dos clientes são salvos em um arquivo CSV chamado "clientes.csv".
Como Executar:
Execute o script Python para iniciar o aplicativo de cadastro de clientes.
Preencha os campos do formulário e clique no botão "Cadastrar".
Os dados serão adicionados ao arquivo "clientes.csv".
