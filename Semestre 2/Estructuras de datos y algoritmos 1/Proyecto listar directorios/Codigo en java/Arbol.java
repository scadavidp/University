
/**
 * La clase arbol se encarga de hacer la busqueda del archivo que ingrese el usiario, asi como de construir la estructura de datos (arreglo)
 * 
 * @author Santiago Avendaño y Samuel Cadavid
 * @version noviembre 19 de 2017
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.util.Scanner;
public class Arbol
{

    String [] texto = new String [3653];
    
    Linea [] lineas = new Linea [texto.length];
    //DESDE AQUI EMPIEZAN LOS METODOS CON ARREGLOS:
    public String [] arreglo(File nombre) throws FileNotFoundException, IOException {

        FileReader f = new FileReader (nombre);
        BufferedReader bufer = new BufferedReader(f);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce el archivo a buscar");
        String request = scanner.next();
        String line = "";
        System.out.println("\n" + "\n");

        for (int i = 0 ; i < texto.length ; i++) {
            line = bufer.readLine();
            texto[i] = line;
            lineas[i] = new Linea(line, i, countLine(line));
            if(line.indexOf(request)!= -1){
                System.out.println("se encontro: "+ line );//+ "   En la posicion: [" +  i + "]");
                System.out.println("\n");
                ruta(lineas[i]);
                //System.out.println("["+i+"]: "+texto[i]);
            }  else {
                System.out.println("No se encontro el archivo que desea buscar");
                System.exit(0);
            }

            //System.out.println("["+i+"]: "+texto[i]);
        }

        return texto;
    }

    //Metodo para la ruta:
    public void ruta(Linea linea) {
        int temp;
        int menor;
        int var;

        System.out.println("La ruta es: ");
        System.out.println(linea.texto);

        for(int i = linea.pos ; i > 0 ; i--){
            if (lineas[i].prof - lineas[i - 1].prof == 1) {
                System.out.println("" + lineas[i-1].texto);
                temp = lineas [i-1].pos;
                i = temp;
            }
        }
        System.out.println(""+lineas[0].texto);
        
        System.out.println("\n" );
    }

    public void acumular(String [] s) throws FileNotFoundException, IOException{
        int temp;
        int carpetas = 0;
        int subCar = 0;
        int subSubCar = 0;
        int arch = 0;

        for (int i = 0; i < s.length ; i++){
            temp = countLine(s[i]);
            if (temp == 1) {
                carpetas++;
            } else if (temp == 2) {
                subCar++;
            } else if (temp == 3) {
                subSubCar++;
            } else if (temp == 4) {
                arch++;
            }
        }

        System.out.println("Numero de carpetas: " + carpetas);
        System.out.println("Numero de subCarpetas: " + subCar );
        System.out.println("Numero de subSubCarpetas: " + subSubCar );
        System.out.println("Numero de archivos: " + arch);

    }

    //AQUI TERMINAN LOS METODOS CON ARREGLOS

    public  void contarProfundidad(File f) throws FileNotFoundException{
        Scanner scan = new Scanner (f);
        int cont = 0;

        while (scan.hasNextLine()){
            String linea = scan.nextLine();
            countLine(linea);              
        }

        //System.out.println (""+cont);         
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
        // System.out.println(""+profundidad);

        //arbol.arreglo(profundidad);
        return profundidad;
    }

    public int contarProfundidad(String s) {
        String line = s;
        int profundidad = 0;

        char uno = '\u2502';
        char dos = '\u251C';
        char tres = '\u2514';

        for (int i = 0; i < line.length() ; i++) {
            if (line.charAt(i) == uno || line.charAt(i) == dos || line.charAt(i) == tres || line.indexOf("   ") == -1) {
                profundidad++;
            }
        }
        // System.out.println(""+profundidad);

        //arbol.arreglo(profundidad);
        return profundidad;
    }

}
