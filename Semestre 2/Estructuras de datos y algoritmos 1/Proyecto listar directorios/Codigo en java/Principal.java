
/**
 * Esta es la clase principal del programa, esta es la que se debe ejecutar.
 * 
 * @author Santiago Avendaño y Samuel Cadavid
 * @version 11 de noviembre de 2017
 */
import java.util.Scanner;
import java.io.*;
public class Principal
{

    public static void main(String [] args) throws Exception {
        String nombreArchivo = "treeEtc.txt";
        
        File archivo = new File (nombreArchivo);
        // LectorArchivo lector = new LectorArchivo();
        //lector.muestraContenido(nombreArchivo);
        // lector.contarProfundidad(archivo);
        
        Arbol arb = new Arbol();
        arb.arreglo(archivo);
    }

    
}
