
/**
 * Estos son los recolectables que hacen que el jugador sume puntos.
 * 
 * @author Samuel Cadavid Perez.
 * @version 30 de mayo de 2017.
 */

import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.*;
import java.io.*;
import java.util.*;
public class Tokens
{
    public int cX;
    public int cY;
    public int size = 10;
    public Tokens(){

    }

    public void dibujarTokens(Graphics g, char [][] matriz){
        for(int f = 0 ; f < matriz.length; f++){
            for(int c = 0 ; c < matriz[0].length ; c++) {
                if (matriz[c][f] == 't') {
                    g.setColor(new Color(255,200,0));
                    g.fillRect(f * 20 , c * 20 , size, size);
                }
            }
        }

    }

    public int getcX(){
        return cX;
    }

    public int getcY(){
        return cY;
    }

}
