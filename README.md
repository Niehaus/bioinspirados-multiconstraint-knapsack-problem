# Multiconstraints Knapsack Problem (MCKP)

## Grupo

- Bárbara Boechat
- Juliana Araújo
- Tiago Trotta

## Dependências

- Versão do Python: `3.8`

## Execução

    ~$ python main.py [Arquivo de instância] [Arquivo de saída] [Número de formigas] [Máximo de iterações] [Alfa] [Beta]

## Formato do arquivo de instância

Os arquivos de entrada das instâncias podem ser encontrados em [mknap2](http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/mknap2.txt). Neste trabalho foram utilizadas as instâncias `PB*`.

Formato do arquivo utiliza 10 colunas sempre que possível, segue um exemplo:

    <n := #knapsacks> <m := #objects>
    <m weights of objects>
    <n knapsack capacities>
    <A := mxn matrix of constraints>
 
    <known optimum>
 

Este é o arquivo WEING1.DAT com comentários, este arquivo não é
uma instância, é apenas um exemplo. 


    2 28 // 2 knapsacks, 28 objects
    1898 440 22507 270 14148 3100 4650 30800 615 4975
    1160 4225 510 11880 479 440 490 330 110 560
    24355 2885 11748 4550 750 3720 1950 10500 // 28 weights
    600 600 // 2 knapsack capacities
    45 0 85 150 65 95 30 0 170 0
    40 25 20 0 0 25 0 0 25 0
    165 0 85 0 0 0 0 100 // #1 constr.
    30 20 125 5 80 25 35 73 12 15
    15 40 5 10 10 12 10 9 0 20
    60 40 50 36 49 40 19 150 // #2 constr.
 
    141278 // optimum value


