#!/bin/bash

list_db () {
	echo "Here are the current book entries:"
	scripts/list_db.py
}

confirm () {
	echo -n "Enter (Y/N): "
	read confirm_yn
}

scripts/create_db.py

while :
do
	echo -e "Available Actions: [n] = New Book, [r] = Remove Book,\n[p] = Progress, [u] = Undo Progress, [e] = Build and Exit"
	echo -n "Enter an action: "
	read curr_action
	case "$curr_action" in
		n)
			echo -n "Enter book title: "
			read book_title
			echo -n "Enter book author(s): "
			read book_author
			scripts/new_book.py "$book_title" "$book_author"
			;;
		r)
			list_db
			echo -n "Enter book id: "
			read rm_id
			echo "Are you sure you want to remove $(scripts/get_book.py $rm_id)?"
			confirm
			if [[ "$confirm_yn" == "Y" ]]
			then
				scripts/rm_book.py $rm_id
			else
				echo "Aborting!"
			fi
			;;
		p)
			list_db
			echo -n "Enter book id: "
			read prog_id
			echo "Are you sure you want to add progress to $(scripts/get_book.py $prog_id)?"
			confirm	
			if [[ "$confirm_yn" == "Y" ]]
			then
				scripts/prog_book.py $prog_id
			else
				echo "Aborting!"
			fi
			;;
		e)
			echo "Building..."
			scripts/build_html.py
			echo "Done!"
			echo "Goodbye."
			exit 0
			;;
		*)
			echo "Unknown action."
			;;
	esac
done
