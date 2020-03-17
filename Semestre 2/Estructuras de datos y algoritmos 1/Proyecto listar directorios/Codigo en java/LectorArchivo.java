
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.util.Scanner;
/**
 * Esta clase se encarga de leer el archivo de texto
 * 
 * @author (Santiago Avendaño y Samuel Cadavid) 
 * @version 11 de noviembre de 2017
 */
public class LectorArchivo
{   

    public static void muestraContenido(String archivo) 
    throws FileNotFoundException, IOException {
        String cadena;
        FileReader f = new FileReader(archivo);
        BufferedReader b = new BufferedReader(f);
        try {
            while((cadena = b.readLine())!=null) {
                System.out.println(cadena);
            } 
        }catch (Exception e) {
            System.out.println("FileNotFoundException");
        }
        b.close();
    }

    public  void contarProfundidad(File f) throws FileNotFoundException{
        Scanner scan = new Scanner (f);
        int cont = 0;
        int i = 0;
        int [] arr = new int [3653] ;
        while (scan.hasNextLine()){
            String linea = scan.nextLine();
            countLine(linea);   
          
        }
      
    }

    public  int countLine(String str) throws FileNotFoundException {
        String line = str;
        int profundidad = 0;
        
        char uno = '\u2502';
        char dos = '\u251C';
        char tres = '\u2514';
        
        
        for (int i = 0; i < line.length() ; i++) {
            if (line.charAt(i) == uno || line.charAt(i) == dos || line.charAt(i) == tres) {
                profundidad++;
            }
        }
        System.out.println(""+profundidad);
        return profundidad;
    }


}
