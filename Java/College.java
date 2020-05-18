package ketan.test; //new creeated package name

public class College {

  private String name;

  public void setName(String name) {
    this.name = name;
  }

  public College() // public constructor to access outside the package
  {
    this.name = "TKIET";

  }

  public String toString() // overridden toString method from Object classs.
  {
    return String.format("%-100s%s", this.name, "ketan"); // to format the string
  }

}
