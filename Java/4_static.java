import org.w3c.dom.NameList;

class Employee {
  private String name;
  private int number;
  private double salary;
  private static String company;

  // static initilizer block
  static {
    Employee.company = "Evosys";
  }

  public static void setCompany(String company) {
    Employee.company = company;
  }

  public static String getCompany() {
    return company;
  }

  /**
   * @return the name
   */
  public String getName() {
    return name;
  }

  /**
   * @return the number
   */
  public int getNumber() {
    return number;
  }

  /**
   * @return the salary
   */
  public double getSalary() {
    return salary;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setNumber(int number) {
    this.number = number;
  }

  public void setSalry(double salary) {
    this.salary = salary;
  }

  Employee() {
    this("", 0, 0);
  }

  Employee(String name, int number, double salary) {
    this.name = name;
    this.number = number;
    this.salary = salary;

  }

}
