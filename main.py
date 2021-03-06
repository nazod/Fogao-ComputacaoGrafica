#Feito por Hudson e Gabriel


import numpy as np
import pygame
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math

from carregaTextura import retornaTextura
from movimentacao import retornaMovimentacao
from iluminacao import retornaIluminacao
from fogao import *


fogaoTextura = [ "", "", "", "", "", "", "", ""]

	
def main():
    # Translação do cubo verde
    tx = 0
    ty = 0

    #UP vector angle = Pi/2 (90o) 
    up_angle = 3.1415/2

    
    rot_angle = 3.1415/2

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    retornaIluminacao()

    gluPerspective(45, (display[0]/display[1]), 0.1, 20.0)

    # eye = (0, 0, 10)
    eye = np.zeros(3)
    eye[2] = 10

    # target = (0, 0, 0)
    target = np.zeros(3)

    # up = (1, 0, 0)
    up = np.zeros(3)
    up[0] = 0
    up[1] = 1
    up[2] = 0

    up[1] = math.sin(up_angle)
    up[0] = math.cos(up_angle)


    fogaoTextura[0] = retornaTextura('Imagens/fogao-front.jpg')
    fogaoTextura[1] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[2] = retornaTextura('Imagens/fogao-up-new.jpeg')
    fogaoTextura[3] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[4] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[5] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[6] = retornaTextura('Imagens/grades.jpeg')
    fogaoTextura[7] = retornaTextura('Imagens/pe-fogao.jpeg')
    
    while True:

        ty, tx, target, eye, up, up_angle, rot_angle = retornaMovimentacao(ty, tx, target, eye, up, up_angle, rot_angle)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        gluLookAt(eye[0], eye[1], eye[2], 
                target[0], target[1], target[2], 
	    	    up[0], up[1], up[2] )

        glPushMatrix()
        glTranslatef(tx,ty, 0.) #Monta as Faces do Fogão
        retornaNovaFace(face1, normal1, fogaoTextura[0]) # Z Positivo
        retornaNovaFace(face2, normal2, fogaoTextura[1]) # Z Negativo
        retornaNovaFace(face3, normal3, fogaoTextura[2]) # Y Positivo
        retornaNovaFace(face4, normal4, fogaoTextura[3]) # Y Negativo
        retornaNovaFace(face5, normal5, fogaoTextura[4]) # X Positivo
        retornaNovaFace(face6, normal6, fogaoTextura[5]) # X Negativo
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx,ty+2, 0.)
        retornaNovaFace(face2, normal2, fogaoTextura[5]) #Tampa do Fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx-0.9,ty-1.1, 0.9)
        retornaOsPesDoFogao(fogaoTextura[7]) #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx+0.9,ty-1.1, 0.9)
        glRotatef (180.0, 0.0, 1.0, 0.0)
        retornaOsPesDoFogao(fogaoTextura[7]) #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx-0.9,ty-1.1, -0.9)
        retornaOsPesDoFogao(fogaoTextura[7]) #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx+0.9,ty-1.1, -0.9)
        glRotatef (180.0, 0.0, 1.0, 0.0)
        retornaOsPesDoFogao(fogaoTextura[7]) #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, fogaoTextura[6])
        q = gluNewQuadric() #Grades das bocas do fogão
        gluQuadricDrawStyle(q, GLU_FILL)
        gluQuadricNormals(q, GLU_SMOOTH)
        glTranslatef(0.5,1.01,0.55)
        glRotatef (90.0, 1.0, 0.0, 0.0)
        gluDisk(q, 0.2, 0.3, 64, 6)
        glPopMatrix()

        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, fogaoTextura[6])
        q = gluNewQuadric() #Grades das bocas do fogão
        gluQuadricDrawStyle(q, GLU_FILL)
        gluQuadricNormals(q, GLU_SMOOTH)
        glTranslatef(-0.5,1.01,0.55)
        glRotatef (90.0, 1.0, 0.0, 0.0)
        gluDisk(q, 0.2, 0.3, 64, 6)
        glPopMatrix()

        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, fogaoTextura[6])
        q = gluNewQuadric() #Grades das bocas do fogão
        gluQuadricDrawStyle(q, GLU_FILL)
        gluQuadricNormals(q, GLU_SMOOTH)
        glTranslatef(0.5,1.01,-0.55)
        glRotatef (90.0, 1.0, 0.0, 0.0)
        gluDisk(q, 0.2, 0.3, 64, 6)
        glPopMatrix()

        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, fogaoTextura[6])
        q = gluNewQuadric() #Grades das bocas do fogão
        gluQuadricDrawStyle(q, GLU_FILL)
        gluQuadricNormals(q, GLU_SMOOTH)
        glTranslatef(-0.5,1.01,-0.55)
        glRotatef (90.0, 1.0, 0.0, 0.0)
        gluDisk(q, 0.2, 0.3, 64, 6)
        glPopMatrix()

        #Grade 1 Inicio
        glPushMatrix()
        glTranslatef(0.35,1,0.7)
        glRotatef (45.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.65,1,0.7)
        glRotatef (135.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.65,1,0.4)
        glRotatef (225.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.35,1,0.4)
        glRotatef (315.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()
        #Grade 1 Fim

        #Grade 2 Inicio
        glPushMatrix()
        glTranslatef(-0.35,1,0.7)
        glRotatef (135.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.65,1,0.7)
        glRotatef (45.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.65,1,0.4)
        glRotatef (315.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.35,1,0.4)
        glRotatef (225.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()
        #Grade 2 Fim

        #Grade 3 Inicio
        glPushMatrix()
        glTranslatef(0.35,1,-0.7)
        glRotatef (315.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.65,1,-0.7)
        glRotatef (225.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.65,1,-0.4)
        glRotatef (135.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.35,1,-0.4)
        glRotatef (45.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()
        #Grade 3 Fim

        #Grade 4 Inicio
        glPushMatrix()
        glTranslatef(-0.35,1,-0.7)
        glRotatef (225.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.65,1,-0.7)
        glRotatef (315.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.65,1,-0.4)
        glRotatef (45.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.35,1,-0.4)
        glRotatef (135.0, 0.0, 1.0, 0.0)
        retornaGradesDoFogao(fogaoTextura[6])
        glPopMatrix()
        #Grade 4 Fim

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()
