
/**
 * El enemigo puede hacer que el jugador pierda el juego, este sigue al jugador.
 * 
 * @author Samuel Cadavid Perez.
 * @version 30 de mayo de 2017.
 */
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
public class Enemigo 
implements KeyListener

{
    public static int cordX = 340; //tiene que ser estartica para que el metodo getX() funcione
    public static  int cordY = 80; //tiene que ser estatico para que metodo getY() funcione

    Color ENEMIGO = new Color(195,100,100);
    public Enemigo() {

    }

    public void dibujarEnemigo(Graphics g) {
        g.setColor(ENEMIGO);
        g.fillOval(cordX , cordY , 20 , 20);
    }

    //estos metodos tienen que ser estaticos para que el metodo dibujarPerder en avatar funcione
    public static  int getX() {
        return cordX;
    }

    public static int getY(){
        return cordY;
    }

    public void keyPressed (KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP || e.getKeyCode() == KeyEvent.VK_DOWN || e.getKeyCode() == KeyEvent.VK_RIGHT || e.getKeyCode() == KeyEvent.VK_LEFT) {
            if (getX () < Juego.jugador.getX() && LectorArchivo.matriz[getY()/20][getX()/20 + 1] != '*') {
                cordX += 20;               
            } else if(getX() > Juego.jugador.getX() && LectorArchivo.matriz[getY()/20][getX()/20 - 1]  != '*') {
                cordX -= 20;                
            } else if (getY() < Juego.jugador.getY()&& LectorArchivo.matriz[getY()/20 + 1][getX()/20]  != '*') {
                cordY += 20;                
            } else if (getY() > Juego.jugador.getY() && LectorArchivo.matriz[getY()/20 - 1][getX()/20]  != '*') {
                cordY -= 20;
            }
        }
    }

    public void keyReleased(KeyEvent e) {}

    public void keyTyped(KeyEvent e){}

}
