for d in $(ls train); do
    for f in $(ls train/$d | shuf | head -n 100 ); do
        mkdir -p validation/$d/
        mv train/$d/$f validation/$d/;
    done;
done
