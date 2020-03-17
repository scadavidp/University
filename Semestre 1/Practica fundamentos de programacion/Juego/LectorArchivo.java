
/**
 * La clase LectorArchivo se encarga de leer el laberinto en formato txt.
 * 
 * @author Samuel Cadavid Perez.
 * @version 30 de mayo de 2017.
 */
import java.io.*;
import java.util.*;
import java.awt.*;
public class LectorArchivo
{
    String nombreArchivo;
    public int corX;
    public int corY;

    public static  char [][] matriz; //para poder invocarla en otras clases evitando problemas como que no sepueda invocar en contextos estaticos

    public LectorArchivo() {

    }

    public void leerArchivo(String nombreArchivo)  {
        try {
            int x;
            int y;
            matriz = new char [20][20];
            Scanner input = new Scanner(new File(nombreArchivo));
            for(int i = 0 ; i < matriz.length; i++) {
                String linea = input.nextLine();
                for(int j = 0; j < matriz[0].length; j++) {
                    matriz[i][j] = linea.charAt(j);
                    if(matriz[i][j] == 'j'){
                        x = j;
                        y = i;
                        corX = x;
                        corY = y;

                    }
                }
            }
        }catch (Exception e){

            System.out.println("ERRROR!");

        }
    }

    public int getX() {
        return corX;
    }

    public int getY(){
        return corY;
    }

}
