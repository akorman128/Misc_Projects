/*
 * Sequence3.cpp
 *
 *  Created on: Oct 12, 2018
 *      Author: alexkorman
 */
#include <cassert>    // Provides assert
#include <cstdlib>    // Provides NULL and size_t
#include <iostream>     // Provides istream and ostream
#include "sequence3.h"
using namespace std;

namespace korman_sequence {

	Sequence::Sequence() {
		// TODO Auto-generated constructor stub
		head_ptr = NULL;
		tail_ptr = NULL;
		cursor = NULL;
		precursor = NULL;
		many_nodes = 0;

	}

	Sequence::Sequence(const Sequence& source){
		assert(this != &source);

		if(many_nodes == 0){
			list_copy(source.head_ptr, head_ptr, tail_ptr);
			precursor = NULL;
			cursor = NULL;
			many_nodes = source.many_nodes;
		}

		else if (many_nodes == 1){
			list_copy(source.head_ptr, head_ptr, tail_ptr);
			precursor = NULL;
			cursor = head_ptr;
			many_nodes = source.many_nodes;
		}

		else {
			list_piece(source.head_ptr, source.precursor, head_ptr, tail_ptr);
			precursor = tail_ptr;

			list_piece(source.cursor, source.tail_ptr, cursor, tail_ptr);
			precursor->set_link(cursor);

			many_nodes = source.many_nodes; }
	}


	void Sequence::start(){
		if (is_item() == true) //if head isn't NULL
			cursor = head_ptr; //set cursor to first node in sequence
	}

	void Sequence::advance(){
		if (is_item() == true) //if cursor isn't NULL
			precursor = cursor;
			cursor = cursor->link(); //cursor points to the next node
	}

	void Sequence::insert(const value_type& entry){
		//REMINDER: CASE OF ADVANCE NULL
		if (many_nodes == 0){ //if cursor is NULL
			list_head_insert(head_ptr, entry); //head points to new node with data entry
			cursor = head_ptr;
			tail_ptr = head_ptr;
			many_nodes = 1; }

		else if (many_nodes == 1 || cursor == head_ptr) //edge case for cursor being at start
		{	list_head_insert(head_ptr, entry);
			precursor = NULL;
			cursor = head_ptr;
			many_nodes +=1; }

		else {
			precursor = cursor;
			list_insert(cursor, entry);
			many_nodes += 1; }
	}

	void Sequence::attach(const value_type& entry){
		if (many_nodes == 0){ //if cursor == NULL
			list_head_insert(head_ptr, entry); //head points to new node with data entry
			cursor = head_ptr;
			tail_ptr = head_ptr;
			many_nodes = 1; }

		else if (many_nodes == 1) {
			precursor = cursor;
			list_insert(cursor,entry); //cursor appends new node which points to old cursor address,
										//cursor now points to new node
			many_nodes +=1; }

		else{
			precursor = cursor;
			cursor->link();
			list_insert(cursor, entry);
			many_nodes += 1;
		}
	}

	void Sequence::remove_current(){


		if(is_item()){
			list_remove(cursor); //removes what precursor points to
			many_nodes -=1;
		}
		//no else, if doesn't exist, nothing to remove

	}

	void Sequence::operator =(const Sequence& source){

		assert(this != &source);

				if(many_nodes == 0){
					list_copy(source.head_ptr, head_ptr, tail_ptr);
					precursor = NULL;
					cursor = NULL;
					many_nodes = source.many_nodes;
				}

				else if (many_nodes == 1){
					list_copy(source.head_ptr, head_ptr, tail_ptr);
					precursor = NULL;
					cursor = head_ptr;
					many_nodes = source.many_nodes;
				}

				else {
					list_piece(source.head_ptr, source.precursor, head_ptr, tail_ptr);
					precursor = tail_ptr;

					list_piece(source.cursor, source.tail_ptr, cursor, tail_ptr);
					precursor->set_link(cursor);

					many_nodes = source.many_nodes; }
	}


	Sequence::~Sequence() {
		// TODO Auto-generated destructor stub
		list_clear(head_ptr);
		many_nodes = 0;
		}

	} /* namespace korman_sequence */
