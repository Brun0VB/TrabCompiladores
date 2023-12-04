Linguagem C+/-
A C+/- é uma linguagem de programação descomplicada, desenvolvida como parte do nosso trabalho na disciplina de compiladores. Ela é baseada em C e Python, visando simplicidade e praticidade. Utilizamos a ferramenta PLY (Python Lex-Yacc) para criar analisadores léxicos e sintáticos de forma direta. A C+/- é projetada para ser acessível a programadores familiarizados com C e Python, proporcionando uma experiência amigável. Este trabalho explora a implementação da C+/-, destacando as escolhas de design simples e os passos básicos de construção do compilador. O objetivo é criar uma linguagem fácil de entender, adequada para avaliação na disciplina, sem pretensões complexas.

Os desenvolvedores do projeto são:
Bruno Vilela Batista
Felipe Souza Fernandes
Rodrigo Nascimento Pereira


Utilização
A implementação adotada realiza a geração de código em linguagem C, que pode ser posteriormente compilada. No arquivo exemplos.py, encontram-se diversos códigos de exemplo para as funcionalidades propostas na linguagem. Se desejar criar seu próprio código, basta construir outro código seguindo o padrão encontrado nos exemplos e atribuir o nome dado para o trecho desenvolvido para 'interpretar', ficando assim 'interpretar = _nomeDoTrechoDesenvolvido'. O mesmo vale para testar outro exemplo, basta substituir o nome como já foi explicado. 
Para executar a geração de código, utilize o seguinte comando no terminal:
    python cpm_yacc.py
O código em c será gerado no arquivo 'codigogerado.c', podendo ser então compilado e posteriormente executado.