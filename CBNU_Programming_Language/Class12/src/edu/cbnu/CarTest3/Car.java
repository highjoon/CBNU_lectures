package edu.cbnu.CarTest3;

public class Car {
	Car() {
		System.out.println("슈퍼 클래스 생성자 호출 (파라미터 없음)");
	}
	
	Car(String str) {
		System.out.println("슈퍼 클래스 생성자 호출 ==> " + str);
	}
}

class Sedan extends Car {
	Sedan(String str) {
		
		super(str);
		
		System.out.println("서브 클래스 생성자 호출 ==> " + str);
	}
}