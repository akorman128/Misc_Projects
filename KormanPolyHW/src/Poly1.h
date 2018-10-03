
#ifndef POLY1_H
#define POLY1_H
#include <cstdlib>      // Provides size_t type
#include <iostream>     // Provides istream and ostream

namespace korman_poly
{

    class polynomial
    {
    public:

    typedef double value_type;
    const static unsigned int DEFAULT_CAP = 5;

	// CONSTRUCTORS and DESTRUCTOR
	polynomial( );
	polynomial(const polynomial& source);
	polynomial(double c, unsigned int exponent);
	~polynomial( );

	// MODIFICATION MEMBER FUNCTIONS
	void add_to_coef(double amount, unsigned int exponent);
	void assign_coef(double coefficient, unsigned int exponent);
	void clear( );
	void reserve(size_t number);
	void trim();


	// MODIFICATION OPERATORS
	polynomial& operator =(const polynomial& source);
	polynomial& operator =(double c)
	    { clear( ); assign_coef(c, 0); return *this; }
	polynomial& operator -=(const polynomial& p);
	polynomial& operator -=(double c)
	    { add_to_coef(-c, 0); return *this; };
	polynomial& operator +=(const polynomial& p);
	polynomial& operator +=(double c)
	    { add_to_coef(c, 0); return *this; };
	polynomial& operator *=(double c);

	// CONSTANT MEMBER FUNCTIONS
	value_type coefficient(unsigned int exponent) const;
	unsigned int next_term(unsigned int e) const;
	unsigned int previous_term(unsigned int e) const;
	unsigned int degree( ) const {return current_degree;};
	size_t size () const {return current_array_size;};
	double eval(double x) const;

    private:
	size_t current_array_size;
	value_type *coef;
	unsigned int current_degree;
    };
}
#endif
