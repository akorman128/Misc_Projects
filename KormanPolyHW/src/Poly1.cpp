

#include <fstream>  //provides ostream for << operater
#include <cstdlib>
#include <cassert>  //provides assert to check preconditions
#include <cmath>    //provides pow
#include <climits>  //provides UINT_MAX
#include <algorithm>//provides fill_n
#include "Poly1.h"  //the polynomial class header

using namespace std;
using namespace korman_poly;


//The Default Constructor

polynomial::polynomial(double c, unsigned int exponent)
{
    assert(exponent<= DEFAULT_CAP);
    current_array_size = DEFAULT_CAP;
    coef = new value_type[current_array_size];
    current_degree = exponent;

    coef[exponent] = c;
    if(current_degree==exponent && c==0 && current_degree!=0)
        {
    		if(previous_term(current_degree)==UINT_MAX)
    			current_degree=0;
    		else
    			current_degree=previous_term(current_degree);
        }
}

polynomial::polynomial(const polynomial& source){
	coef = new value_type[source.current_degree];
	current_array_size = source.current_array_size;
	current_degree = source.degree();
	copy(source.coef, source.coef + source.degree()+1, coef);
}


//Adds a term to an existing term.
void polynomial::add_to_coef(double amount, unsigned int exponent)
{
    if (exponent<=current_array_size)
    	reserve(exponent);
    assign_coef(amount+coefficient(exponent), exponent);
}

//Replaces whatever term was in the original polynomial with
//a new term.

void polynomial::assign_coef(double coefficient, unsigned int exponent)
{
    if(exponent<=DEFAULT_CAP)
    	reserve(exponent);
    coef[exponent]=coefficient;


    if(exponent>current_degree && coefficient!=0)
	current_degree=exponent;
    else if(current_degree==exponent && coefficient==0 && current_degree!=0)
    {
		if(previous_term(current_degree)==UINT_MAX)
			current_degree=0;
		else
			current_degree=previous_term(current_degree);
    }

}

//Resets all the terms in the polynomial to zero.
void polynomial::clear( )

{
    fill_n(coef, current_array_size, 0.0);
    current_degree=0;
}


//Returns the coefficient of a term, if the exponent is
//greater than allowed, the function returns zero.
double polynomial::coefficient(unsigned int exponent) const

{
    if(exponent>degree())
    	return 0.0;
    else
	return coef[exponent];
}

//This function returns the polynomials value at some x value.

double polynomial::eval(double x) const
{
    double sum=0;
    unsigned int n=0;

    do
    {
	sum+=coefficient(n)*pow((long double)x, (int)n);
	n=next_term(n);
    }while(n!=0);

    return sum;
}

//Return the power of the next greatest term to e.
unsigned int polynomial::next_term(unsigned int e) const
{
    unsigned int n;

    if(e<degree())
    {
	for(n=e+1; n<=degree(); n++)
	    if(coefficient(n)!=0.0)
		return n;
    }

    return 0;
}


//Returns the power of the previous term to e.
unsigned int polynomial::previous_term(unsigned int e) const
{
    unsigned int n=e;

    if(e==0)
	return UINT_MAX;

    do
    {
	if(n>degree())
	    return degree();
	n--;
	if(coefficient(n)!=0.0)
	    return n;
    }while(n>0);

    return UINT_MAX;
}

//Reserves memory in new dynamic array for degrees that exceeds current allotted space
void polynomial::reserve(size_t new_capacity){
	value_type *larger_array;

	if (new_capacity == current_array_size)
		return;

	if (new_capacity < degree())
		new_capacity = degree();

	larger_array = new value_type[new_capacity];
	copy(coef, coef + degree()+1, larger_array);
	delete [ ] coef;
	coef = larger_array;
	current_array_size = new_capacity;
}

// Destructor
polynomial::~polynomial(){
	delete [] coef;
}
