/*
 * Lock.h
 *
 *  Created on: Sep 14, 2018
 *      Author: alexkorman
 */

#ifndef LOCK_H_
#define LOCK_H_

#include <string>
#include <iostream>

using namespace std;

namespace korman_lock {

class Lock {

public:
// constructor
	Lock(int, int, int);

//turns lock
	void turn(int, bool, int);

// opens lock
	void open_lock();

//  closes lock
	void close_lock();

//	returns whether lock is closed or not
	bool get_status() const {return closed; };

//  returns position
	int get_position() const {return current_position; };


//	return_position();

private:
	int current_position;
	int passcode_first;
	int passcode_second;
	int passcode_third;

	bool closed;
	bool position_one;
	bool position_two;
	bool position_three;
};

}

#endif /* LOCK_H_ */
