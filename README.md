# EP-2-solitaire-accordion
Exercício Programa 2 - Curso Design de Software - Engenharia Insper 1º Semestre
TURMA A
ALUNOS: Arthur Cisotto Machado e Alessandra Yumi Carvalho Ogawa

A proposta do Exercício Programa 2 implicava o uso da plataforma Git Hub para compartilhamento e trabalho conjunto em códigos. O repositório para esse jogo foi criado por Arthur e clonado mais tarde por Alessandra para iniciar a série de commits que juntos representam os comandos necessários para a operação do Solitaire Accordion.

Iniciamos a programação realizando as funções obrigatórias que serviriam de base para a programação do jogo como um todo. Após feitas, compilamos todas em um unico arquivo juntamente com os comandos e respostas à movimentações previstas na regra do jogo.

Logo depois, adicionamos uma função para desenhar e colorir as cartas do jogo.

Por último, fizemos alguns commits de correções de bugs e erros gerados por alterações feitas em outras versões.

Detalhamento das funções do jogo:

1. cria_baralho: função obrigatória que gera o baralho;
2. empilha: função obrigatória que realiza a movimentação de empilhamento das cartas durante o jogo;
3. extrai_naipe: função obrigatória que verifica o naipe da carta escolhida;
4. extrai_valor: função obrigatória que verifica o valor da carta escolhida;
5. possui_movs_possiveis: função obrigatória que verifica de a carta escolhida possui movimentos possiveis dado seu valor/naipe e seguindo as regras do jogo;
6. movs_possiveis: função obrigatória que exibe os movimentos possíveis, se existirem,  para uma determinada carta escolhida;
7. funcoes: arquivo compilado das funções obrigatórias em conjunto com outras funções que descrevem a regra do jogo e permitem sua continuidade;
8. main: função que roda o jogo e permite recomeçar quando terminado; 