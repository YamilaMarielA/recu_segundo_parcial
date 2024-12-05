import pygame
# Iniciar Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Preguntas")
fondo = pygame.image.load("fondoprincipal.jpg")  # Asegúrate de tener la imagen de fondo en la carpeta correcta
fondo = pygame.transform.scale(fondo, (800, 600))
fondo_final = fondo
fondo_final = pygame.transform.scale(fondo_final, (800, 600))

fondo_solo_juego = pygame.image.load("fondoprincipal.jpg")
fondo_solo_juego = pygame.transform.scale(fondo_solo_juego, (800, 600))


imagen_boton = pygame.image.load("boton1.jpg")  # Imagen de botones
imagen_boton_hover = pygame.image.load("boton2.jpg")  # Imagen de botones cuando pasas el mouse

imagen_boton_jugar = pygame.transform.scale(imagen_boton, (200, 50))
imagen_boton_jugar_hover = pygame.transform.scale(imagen_boton_hover, (200, 50))

# Puedes hacer lo mismo para los otros botones si los necesitas (TOP 10, Configuración)
imagen_boton_top10 = pygame.transform.scale(imagen_boton, (200, 50))
imagen_boton_top10_hover = pygame.transform.scale(imagen_boton_hover, (200, 50))

imagen_boton_config = pygame.transform.scale(imagen_boton, (200, 50))
imagen_boton_config_hover = pygame.transform.scale(imagen_boton_hover, (200, 50))

imagen_boton_activado = pygame.image.load("boton_activado.jpg") 
imagen_boton_activado = pygame.transform.scale(imagen_boton_activado, (200, 50))
imagen_boton_desactivado = pygame.image.load("boton_desactivado.jpg") 
imagen_boton_desactivado = pygame.transform.scale(imagen_boton_desactivado, (200, 50))

imagen_fondo_para_pregunta = pygame.image.load("fondo_para_pregunta.jpg") 
imagen_fondo_para_pregunta = pygame.transform.scale(imagen_fondo_para_pregunta, (700, 50))


# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (169, 169, 169)


# Fuentes
fuente = pygame.font.SysFont("Arial", 30)
fuente_pequeña = pygame.font.SysFont("Arial", 24)
fuente_nombre = pygame.font.SysFont("Arial", 24)

#musica
# Cargar el sonido de activación y desactivación de la música
sonido_activar_musica = pygame.mixer.Sound('sonido_juego (1).mp3')


# Variables de juego
vidas = 3
puntos = 0
respuestas_correctas = 0
categoria_seleccionada = None
comodin_duplicar_puntos_usado = False
comodin_pasado_usado = False
musica_activada = True
volumen_musica = 0.5  # Volumen inicial