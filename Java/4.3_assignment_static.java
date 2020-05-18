//assignment 1 to find number of instances of a class Employee
//assigment 2 for singleton class.

class Employee {

  private String name;
  private double salary;
  private static int instance_count;

  public static int getInstance_count() {

    return instance_count;
  }

  static {
    instance_count = 0;
  }

  Employee() {
    instance_count += 1;
  }

   Employee(String name, double salary) {
    this.name = name;
    this.salary = salary;
    instance_count += 1;
  }
}


class Sun
{
  private String name;
  private int planets;

  private static int instance_count=0;
  private static Sun s;  


  public static int getInstance_count() {

    return instance_count;
  }


  private Sun()
  {
    this.name="Sun";
    this.planets=9;
  }

  /**
   * @return the name
   */
  public String getName() {
    return name;
  }

  /**
   * @return the planets
   */
  public int getPlanets() {
    return planets;
  }

  /**
   * @param name the name to set
   */
  public void setName(String name) {
    this.name = name;
  }
  /**
   * @param planets the planets to set
   */
  public void setPlanets(int planets) {
    this.planets = planets;
  }


  public static Sun getInstance()
  {
      if (Sun.getInstance_count() == 0)
      {
        Sun s= new Sun();
        Sun.s=s;
        Sun.instance_count+=1;
        return s;
      }
      else
      {
        return Sun.s;  
      }
      
  }
}

class Program {
  public static void main(String[] args) {
    Employee emp1 = new Employee();
    Employee emp2 = new Employee("Ketan", 2111111);
    Employee emp3= new Employee();
    System.out.println("Number of instances: " + Employee.getInstance_count());


    System.out.println(Sun.getInstance_count() );
    Sun s1= Sun.getInstance();
    System.out.println(Sun.getInstance_count() );
    Sun s2= Sun.getInstance();
    System.out.println(Sun.getInstance_count() );

    System.err.println("s1  :"+s1.getName());
    System.err.println("s2  :"+s2.getName());
    s1.setName("BigSun");
    System.err.println("s1  :"+s1.getName());
    System.err.println("s2  :"+s2.getName());
  }

}