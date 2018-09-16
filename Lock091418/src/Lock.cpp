/*
 * Lock.cpp
 *
 *  Created on: Sep 14, 2018
 *      Author: alexkorman
 */

#include "Lock.h"

using namespace std;
using namespace korman_lock;

Lock::Lock(int one, int two, int three) {
	// constructor takes lock combination
	 passcode_first = one;
	 passcode_second = two;
	 passcode_third = three;

	 current_position = 0;
	 closed = true;

	 position_one = false;
	 position_two = false;
	 position_three = false;
	 }

void Lock::turn(int position, bool direction, int turn) {
			current_position = position;
//	checks if turn, direction and passcode correspond
		if (turn == 1 && direction == true && passcode_first == position){
			position_one = true;
		}
		if (turn == 2 && direction == false && passcode_second == position){
			position_two = true;
		}
		if (turn == 3 && direction == true && passcode_third == position){
			position_three = true;
		}

	}


void Lock::close_lock(){
	// if lock open, closes it.
	if (get_status()){
		cout << "This lock is already closed" << endl;
	} else{
		closed = true;
		position_one = false;
		position_two = false;
		position_three = false;
		cout << "The lock is closed" << endl;
	}
}

void Lock::open_lock() {
// if lock closed and unlocked correctly, opens lock
	if (get_status() == false){
		cout << "This lock is already open" << endl;
	}
	if (get_status() == true && position_one == true
	&& position_two == true && position_three == true){
		closed = false;
		cout << "The lock is open" << endl;
	} else{
		cout << "Combination did not work" << endl;
	}
}
