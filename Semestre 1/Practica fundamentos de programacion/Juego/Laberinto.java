
/**
 * Esta clase se encarga de dibujar el laberinto con base en lo leido por la clase LectorArchivo.
 * 
 * @author Samuel Cadavid Perez.
 * @version 30 de mayo de 2017.
 */
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.*;
import java.io.*;
import java.util.*;

public class Laberinto {

    public Laberinto() {

    }

    public void dibujarLaberinto(Graphics g){
        for(int f = 0 ; f < LectorArchivo.matriz.length; f++){
            for(int c = 0 ; c < LectorArchivo.matriz[0].length ; c++) {
                if (LectorArchivo.matriz[c][f] == '*') {
                    g.setColor(Color.DARK_GRAY);
                    g.fillRect(f * 20, c * 20, 20, 20);
                } 
            }
        }
    }

}
