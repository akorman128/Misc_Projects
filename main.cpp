//============================================================================
// Name        : 090618.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "caesar.h"
#include <iostream>
using namespace std;


int main() {
	Caesar translate; // constructs object
	string input; // declares input string
	cout << "Input the word you would like to encrypt: "; // asks for string to code
	cin >> input; // user inputs
	cout << translate.encode(input) << endl;
	cout << translate.decode(translate.encode(input)) << endl;
	return 0;
}

