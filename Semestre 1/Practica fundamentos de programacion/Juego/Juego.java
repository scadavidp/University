

/**
 * Aqui debe estar el juego completo (aplicacion), esta es la clase principal del programa.
 * 
 * @author Samuel Cadavid Perez.
 * @version 7 de mayo 2017.
 * ultima modificacion 30 de mayo de 2017.
 */

import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.SwingUtilities;

public class Juego extends JPanel implements KeyListener {
    public static final int NUMFILAS = 20;
    public static final int NUMCOLUMNAS = 20;
    public int x;
    public int y;
    static Avatar jugador;
    LectorArchivo lector;
    Aviso aviso;
    Enemigo enemigo;

    Tokens tokens;
    Laberinto laberinto;

    public Juego() {
        lector = new LectorArchivo();
        lector.leerArchivo("LaberintoEnTexto.txt");
        laberinto = new Laberinto();
        aviso = new Aviso();
        enemigo = new Enemigo();
        tokens = new Tokens ();
        jugador = new Avatar(40,20);//este contructor recibe la posicion inicial del avatar (no se lee del archivo de texto)
        this.addKeyListener(this);
        this.setFocusable(true);
    }

    public void paintComponent (Graphics g) {
        super.paintComponent(g);
        dibujarFondo(g);
        laberinto.dibujarLaberinto(g);
        jugador.dibujarAvatar(g);
        enemigo.dibujarEnemigo(g);
        tokens.dibujarTokens(g, lector.matriz);
        aviso.dibujarPuntaje(g);
        jugador.ganar(g);
        jugador.perder(g);

    }
    public static void main(String[] args) {
        // Crear un nuevo Frame
        JFrame frame = new JFrame("Juego");

        // Al cerrar el frame, termina la ejecución de este programa
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Agregar un JPanel que se llama Points (esta clase)
        frame.add(new Juego());
        // Asignarle tamaño
        frame.setSize(575,472);
        frame.setBackground(Color.BLACK);
        // Poner el frame en el centro de la pantalla
        frame.setLocationRelativeTo(null);
        // Mostrar el frame
        frame.setVisible(true);        
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP  ) {

            if(lector.matriz[jugador.corY/20 - 1][jugador.corX/20] != '*') {
                jugador.keyPressed(e);
            }
            if (lector.matriz[enemigo.cordY/20 - 1][enemigo.cordX/20] != '*') {
                enemigo.keyPressed(e);      
            }

        }
        if (e.getKeyCode() == KeyEvent.VK_DOWN ) {

            if(lector.matriz[jugador.corY/20 + 1][jugador.corX/20] != '*') {
                jugador.keyPressed(e);
            }
            if (lector.matriz[enemigo.cordY/20 + 1][enemigo.cordX/20] != '*' ) {
                enemigo.keyPressed(e);
            }

        }
        if (e.getKeyCode() == KeyEvent.VK_RIGHT) {

            if(lector.matriz[jugador.corY/20][jugador.corX/20 + 1] != '*') {
                jugador.keyPressed(e);
            }
            if ( lector.matriz[enemigo.cordY/20][enemigo.cordX/20 + 1] != '*') {
                enemigo.keyPressed(e);
            }

        }
        if (e.getKeyCode() == KeyEvent.VK_LEFT ) {

            if( lector.matriz[jugador.corY/20][jugador.corX/20 - 1]  != '*' && jugador.corX>= 0) {
                jugador.keyPressed(e);
            }
            if (lector.matriz[enemigo.cordY/20][enemigo.cordX/20 - 1]  != '*' && enemigo.cordX>= 0 ) {
                enemigo.keyPressed(e);
            }

        }
        removerTokens();
        repaint();
    }

    public void removerTokens() {
        if (lector.matriz[jugador.corY/20][jugador.corX/20]  == 't') {
            lector.matriz[jugador.getY()/20][jugador.getX()/20] = 'p';
            aumentarPuntaje();
        }

    }

    public void aumentarPuntaje(){
        aviso.contarPuntaje();
    }

    public void dibujarFondo(Graphics g) {
        g.setColor(Color.BLACK);
        g.fillRect(0,0,575,472);
    }

    public void keyReleased(KeyEvent e) {}
    public void keyTyped(KeyEvent e) {}
    
}
