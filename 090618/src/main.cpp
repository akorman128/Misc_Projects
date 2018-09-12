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

	string message, key;

	cout << "Input the word you would like to encrypt: "; // asks for string to code
	cin >> message; // user inputs
	cout << "Input the key you would like to implement: "; // asks for string to code
	cin >> key;

	Caesar translate(key);
	string code = translate.encode(message);
	translate.decode(code);

	return 0;
}
