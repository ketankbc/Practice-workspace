import java.io.Console;
import java.io.PrintStream;
import java.util.Scanner;
class Program {


  public static void main(String[] args) {
    //console inputs ways 1
    String str = System.console().readLine();
    System.out.println(str);

    //2
    Console c = System.console();
    String str2 = c.readLine();
    System.out.println(str2);

    //3
    Scanner sc= new Scanner(System.in);
    String k=sc.nextLine();

    System.out.println("k="+k);

  }

}