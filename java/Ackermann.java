package com.leetcode.ackermann;

import java.util.Scanner;

public class Ackermann {
	public static long computeAckermann(long m, long n) {
		long answer;
		if(m == 0) answer = n + 1;
		else if(n == 0) answer = computeAckermann(m-1, 1);
		else answer = computeAckermann(m-1, computeAckermann(m, n-1));
		return answer;
	}
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the input for m: ");
		int m = input.nextInt();
		System.out.println("Enter the input for n: ");
		int n = input.nextInt();

		System.out.printf("Computing Ackermann(%d,%d)...\n", m, n);
		long answer = computeAckermann(m, n);
		
		System.out.printf("Ackermann(%d,%d) is %d", m, n, answer);
	}
}
