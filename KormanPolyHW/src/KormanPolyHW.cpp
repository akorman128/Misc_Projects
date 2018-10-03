//============================================================================
// Name        : KormanPolyHW.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "Poly1.h"
using namespace std;
using namespace korman_poly;

int main() {

	double coefficient = 2.0;
	unsigned int exp = 1;

	polynomial p(coefficient, exp);
	p.assign_coef(1.0,1);
	p.assign_coef(1.0,4);

	cout << p.degree() << endl;

	p.reserve(10);
	cout << p.size() << endl;

	polynomial s(p);
	cout << s.size() << endl;

	return 0;
}
