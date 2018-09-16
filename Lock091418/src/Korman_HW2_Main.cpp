//============================================================================
// Name        : Lock091418.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>  // Provides cin and cout
#include <cstdlib>   // Provides EXIT_SUCCESS
#include "Lock.h"    // Provides the lock class
using namespace std;
using namespace korman_lock;

int main( )
{
    Lock my_bike_lock(14, 36, 10);
    int number[3];

    cout << "Guess the 3 numbers of the combination: "
	 << endl;
    cin >> number[0] >> number[1] >> number[2];

    my_bike_lock.turn(number[0], true, 1);
    my_bike_lock.turn(number[1], false, 2);
    my_bike_lock.turn(number[2], true, 3);

    my_bike_lock.open_lock( );
    my_bike_lock.close_lock();

    my_bike_lock.get_position();

    return EXIT_SUCCESS;
}
