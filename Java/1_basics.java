import java.io.PrintStream;

class Program {

  public static void main(String[] args) {
    // print withous using semicolon

    if (System.out.format("Oksy") == null) {
    }

    if (System.out.printf("Oksy") == null) {
    }

    for (int i = 1; i < 2; System.out.println("Hello World.")) {
      i++;
    }
  }

  public static void main4(String[] args1) {

    // Command line arguments

    String myText = args1[0];
    int num1 = Integer.parseInt(args1[1]);
    int num2 = Integer.parseInt(args1[2]);

    System.out.println(myText + '=' + (num1 + num2));

  }

  public static void main3(String[] args) {

    String str = "123";
    int num = Integer.parseInt(str); // converting non-premtive into primtive // unboxing

    float floatingNnbr = 23.11f;
    String str2 = Float.toString(floatingNnbr); // converting primtive type into non-primtive // Boxing

    System.out.println("num=" + num);
    System.out.println("str2=" + str2);

  }

  public static void main2(String[] args) {
    double num2 = 23.35d;
    int a = (int) num2; // narrowing

    int b = 11;
    float c = b; // widening

    System.out.println("a=" + a);
    System.out.println("c=" + c);

  }

  public static void main1(String[] args) {

    int number1 = 10;
    float number2 = 20.3f;

    System.out.println("Sum:  " + (number1 + number2));

  }

}