# $1 arquivo da instância
# $1 arquivo de saida

sudo rm $2
touch $2
sudo chmod 777 $2
echo -e "N. de Formigas\tMáx. de Iterações\tAlfa\tBeta\tMelhor Fitness" >> $2

cat arguments.txt | while read line; do
    echo "$line"
    python3 main.py $1 $2 $line
done