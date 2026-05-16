# 🚀 Space Shooter — Jogo Atari

Um jogo arcade 2D estilo *space shooter* desenvolvido com **Python** e **Pygame**, criado como projeto acadêmico para a disciplina de desenvolvimento de software.

## 🎮 Sobre o Jogo

O jogador controla uma nave espacial e deve destruir asteroides que descem pela tela enquanto sobrevive o máximo possível, acumulando pontos a cada asteroide destruído.

## 🕹️ Mecânicas

- **Movimentação horizontal** da nave com as setas do teclado
- **Disparo de projéteis** com a barra de espaço
- **Asteroides** gerados aleatoriamente de cima para baixo
- **Detecção de colisão** entre projéteis/nave e asteroides
- **Sistema de pontuação** por asteroides destruídos
- **Game Over** quando um asteroide atinge a parte inferior ou colide com a nave

## 📁 Estrutura do Projeto

```
GoogleAntigravity/
├── jogo-atari/
│   ├── game.py       # Loop principal e lógica do jogo
│   ├── sprites.py    # Classes dos sprites (nave, projétil, asteroide)
│   └── settings.py   # Constantes e configurações globais
├── main.py           # Ponto de entrada da aplicação
└── README.md
```

## ▶️ Como Executar

1. Certifique-se de ter o Python 3.x instalado
2. Instale as dependências:
   ```bash
   pip install pygame
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 🛠️ Tecnologias

- **Python 3.x**
- **Pygame**

## 👤 Autor

**Miguel Henrique** — [@MiguelHenriqueO](https://github.com/MiguelHenriqueO)
