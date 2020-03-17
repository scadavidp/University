
/**
 * Esta clase es el avatar que va a controlar el jugador(usuario de la aplicacion)
 * 
 * @author Samuel Cadavid Perez
 * @version 30 de mayo de 2017
 */
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
public class Avatar implements KeyListener

{
    Aviso aviso = new Aviso();

    public boolean perdio = false;

    public int corX;
    public int corY;

    Color AVATAR = new Color(75,122,151);

    Timer tiempo = new Timer();

    public Avatar(int corX, int corY) {
        this.corX = corX;
        this.corY = corY;
    }

    public void dibujarAvatar(Graphics g) {
        g.setColor(AVATAR);
        g.fillOval(corX , corY , 20 , 20);
    }

    public  int getX() {
        return corX;
    }

    public  int getY(){
        return corY;
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP ) {
            corY += -20;
        }
        if (e.getKeyCode() == KeyEvent.VK_DOWN) {
            corY += 20;
        }
        if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            corX += 20;
        }
        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            corX += -20;
        }
    }

    public void keyReleased(KeyEvent e) {}

    public void keyTyped(KeyEvent e) {}

    public void ganar(Graphics g){
        if  (getX() == 380 && getY()== 260) {
            aviso.dibujarGanaste(g);   
            start();
        }
    }

    //aqui se declara que tiene que hacer el temporizador
    TimerTask tarea = new TimerTask()
        { 
            public void run() {
                System.exit(0);
            }

        };

    public void start() {//este es el metodo que hace que se inicie el temporizador para cerrar el frame
        try {
            tiempo.schedule(tarea,1800);
        } catch (Exception e) {
            System.err.println("ACCION INVALIDA");
        }

    } 
    public void perder(Graphics g){
        if  (getX() == Enemigo.getX() && getY()== Enemigo.getY()) {
            aviso.dibujarPerdiste(g);   
            start();
        }
    }

}
