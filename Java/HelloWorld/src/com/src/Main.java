/**
 * My first java class in 2022
 */
package com.src;


class Main
{
	
	public static void main(String[] argsss)
	{	
		int num=5_00_000_000;
		float frac=123/12;
		double frac2=12.1;	//default is double in java. 
		
		long long_num= 100000000000l;
		byte byte_num='A';
		
		char c= '(';
		c=65; //ASCI
		
		System.out.println("Hello from Ketan");
		System.out.println(num);
		System.out.println(frac);
		System.out.println(long_num);
		System.out.println(byte_num);
		System.out.println(c);
		
		double d= 5;// implicite conversion
		int k= (int)6.6; //type casting
	}
}