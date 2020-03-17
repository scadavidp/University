import java.lang.Object;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.*;
/**
 * Esta clase se encarga de mostrar los letreros de puntaje, ganaste y perdiste.
 * 
 * @author Samuel Cadavid Perez.
 * @version 30 de mayo de 2017.
 */
public class Aviso
{
    Color w = new Color(85,140,220);
    Color p = new Color (30, 255, 87);
    int puntaje = 0;
    public Aviso(){

    }

    public void contarPuntaje(){
        puntaje++;
    }

    public void dibujarGanaste(Graphics g) {
        Font a = new Font("American Typewriter", Font.PLAIN, 32);
        g.setFont(a);
        g.setColor(w);
        g.drawString("GANASTE", 400, 280);
    }

    public void dibujarPerdiste(Graphics g) {
        g.setColor(Color.RED);
        g.drawRect(0,0,575,472);
        g.setColor(Color.BLACK);
        g.fillRect(0,0,575,472);
        Font b = new Font("Dialog", Font.PLAIN,78);
        g.setFont(b);
        g.setColor(Color.RED);
        g.drawString("PERDISTE!",75, 220);
    }

    public void dibujarPuntaje(Graphics g){
        Font a = new Font("American Typewriter", Font.PLAIN, 32);
        g.setFont(a);
        g.setColor(p);
        g.drawString("PUNTAJE: " + puntaje , 5 , 425);
    }
}
