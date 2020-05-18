

//export CLASSPATH="./bin" 

class Program {

  public static void main(String[] args)
  {
    
    Employee emp1=new Employee("Ketan",1,40000d);

    System.out.println(emp1.getName());
    System.out.println(emp1.getNumber());
    System.out.println(emp1.getSalary());

    Employee.setCompany("Evosys2");
    System.out.println(Employee.getCompany());
  }

}