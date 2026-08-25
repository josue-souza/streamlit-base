#! /bin/bash

if [ -d ".git" ]; then
    read -p "Deseja remover o repositório Git atual? [y/N] " confirm

    if [[ "$confirm" =~ ^[Yy]$ ]]; then
        rm -rf .git
        echo "Repositório Git removido."
    else
        echo "Operação cancelada."
        exit 0
    fi
fi

read -p "Deseja inicializar um novo repositório Git? [y/N] " confirm

if [[ "$confirm" =~ ^[Yy]$ ]]; then
    git init
    echo "Novo repositório Git inicializado."
else
    echo "Novo repositório não inicializado."
fi