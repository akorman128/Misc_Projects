/*
 * PrintWorld.cpp
 *
 *  Created on: Sep 6, 2018
 *      Author: alexkorman
 */

#include "caesar.h"
#include <iostream>
using namespace std;

Caesar::Caesar(string newKey){
	key = newKey;
}

string Caesar::get_key() const{
	return key;
}

string Caesar::encode(string message){
//	Postcondition: Takes string and augments according to the key value

	string response = "";
	for (int x = 0; x < message.length(); x++){ // iterate through each letter in message
		int int_char = message[x] - MIN_ORD; //casts char ascii val

		int code = get_key()[x % get_key().length()]; // set code = to correct ascii val of letter in key

		int shifted_char = ((int_char + code) - MIN_ORD) % ((MAX_ORD + 1) - MIN_ORD); //shift the character based off of key value

		char letter_conversion = shifted_char + MIN_ORD; //convert augmented ascii val into char equivelant

		response += letter_conversion; //concatenate characters in string
	}

	cout << response << endl;

	return response;
}

string Caesar::decode(string decode) const{
	//	Postcondition: Takes string and reverts according to the key value

	string response = "";
	for (int x = 0; x < decode.length(); x++){

		int int_char = decode[x] - MIN_ORD;

		int code = get_key()[x % get_key().length()]; // set code = to correct ascii val of letter in key

		int decoded_char = (((int_char - code) - MIN_ORD) % ((MAX_ORD + 1) + MIN_ORD));

		decoded_char += ((MAX_ORD + 1) + MIN_ORD);

//		decoded_char = decoded_char % ((MAX_ORD + 1) + MIN_ORD);

		char letter_conversion = decoded_char + MIN_ORD;

		response += letter_conversion;
	}

	cout << response << endl;

	return response;
}


