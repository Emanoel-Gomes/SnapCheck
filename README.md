# SnapCheck
"SnapCheck" é um programa em Python que tira screenshots de uma determinada área da tela a cada segundo e verifica se ela mudou. Se a imagem mudou, ele salva o screenshot com um número de sequência. Ideal para monitorar mudanças em páginas da web ou em jogos.

Você pode modificar o comando "São iguais" e "Não são iguais" por uma determinada ação.
## Como usar
Abra o programa "SnapCheck".

Digite as coordenadas X e Y da posição na tela em que deseja tirar os screenshots.

Digite a largura e altura da região de captura.

Clique no botão "Select Directory" para escolher o diretório onde as imagens dos screenshots serão salvas.

Clique no botão "Start" para iniciar a captura de screenshots.

Para pausar a captura, clique no botão "Pause".

Para retomar a captura, clique no botão "Resume".

Lembre-se de mudar o local da imagem em:
    
    self.reference_image = Image.open("referencia.png")
Caso queira salvar todas imagens, modifique isso:
      
    screenshot.save("screenshot.png")
 
Para isso:

    screenshot.save(f"screenshot_{self.screenshot_count}.png")
