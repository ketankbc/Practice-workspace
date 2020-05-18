class Bank {

  String name;
  int number;

  // parametrer less constructor
  Bank() {

    this("King", 1); // constructor Chaining
    System.out.println("1st");
  }

  // parameterized constructor
  Bank(String name, int number) {
    this.name = name;
    this.number = number;
    System.out.println("2nd");
  }
}

class Program {
  public static void main(String[] args) {

    Bank b1 = new Bank();
    System.out.println("name=" + b1.name);
    System.out.println("number=" + b1.number);

  }

}