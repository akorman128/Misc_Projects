#ifndef CAESAR_H
#define CAESAR_H

#include <string>
#include <iostream>

// ASCII ordinal range for shifts
#define MIN_ORD 32
#define MAX_ORD 122

using namespace std;

class Caesar {
  public:

    Caesar(string);
    // return the current cipher key
    string get_key() const;
    // return key
    string decode(string) const;
    // decode the string argument using the key, return decoded string
	string encode(string message);
    // encode the string argument using the key, return encoded string

  private:
    string key;

};

#endif
//______________________
/*
 * PrintWorld.h
 *
 *  Created on: Sep 6, 2018
 *      Author: alexkorman
 */

//#ifndef CAESAR_H_
//#define CAESAR_H_
//#include <iostream>
//using namespace std;
//
//// ***Caesar cypher class defintion***
//
//class Cypher {
//
//private:
//	//define all of letter in caesar cipher
//	int min_char = 32;
//	int max_char = 122;
//
//public:
//	string encrypt(string message, string key);
//
//};
//
//#endif /* CAESAR_H_ */
