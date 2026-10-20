import pygame

pygame.init()
skrin = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Permainan Bola Tampar")

# Warna
PUTIH = (255, 255, 255)
BIRU = (0, 100, 255)

# Pemain
pemain = pygame.Rect(350, 500, 80, 20)
bola = pygame.Rect(380, 300, 15, 15)
kelajuan_bola = [4, -4]

larian = True
while larian:
    for peristiwa in pygame.event.get():
        if peristiwa.type == pygame.QUIT:
            larian = False
    
    # Pergerakan pemain
    kekunci = pygame.key.get_pressed()
    if kekunci[pygame.K_LEFT] and pemain.left > 0:
        pemain.x -= 5
    if kekunci[pygame.K_RIGHT] and pemain.right < 800:
        pemain.x += 5
    
    # Pergerakan bola
    bola.x += kelajuan_bola[0]
    bola.y += kelajuan_bola[1]
    
    # Pantulan dinding
    if bola.left <= 0 or bola.right >= 800:
        kelajuan_bola[0] *= -1
    # Pantulan pemain
    if bola.colliderect(pemain) and kelajuan_bola[1] > 0:
        kelajuan_bola[1] *= -1
    # Bola jatuh
    if bola.top > 600:
        bola.x, bola.y = 380, 300
    
    # Lukis
    skrin.fill(PUTIH)
    pygame.draw.rect(skrin, BIRU, pemain)
    pygame.draw.circle(skrin, (255, 0, 0), bola.center, 7)
    pygame.display.flip()

pygame.quit()
