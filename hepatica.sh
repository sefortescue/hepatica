#!/bin/bash

list_db () {
	echo "Here are the current book entries:"
	scripts/list_db.py
}

check_exit () {
    if [[ $? != 0 ]]
    then
        echo "Internal Error. Check Arguments."
    fi
}

confirm () {
	echo -n "Confirm? (Y/N): "
	read confirm_yn
    if [[ "$confirm_yn" == "Y" ]]
    then
        scripts/$1 $2 #2>/dev/null
        check_exit
    else
        echo "Aborting!" 
    fi
}

scripts/create_db.py

while :
do
	echo -e "Available Actions: [n] = New Book, [r] = Remove Book,\n[p] = Progress, [e] = Build and Exit"
	echo -n "Enter an action: "
	read curr_action
	case "$curr_action" in
		n)
			echo -n "Enter book title: "
			read book_title
			echo -n "Enter book author(s): "
			read book_author
			scripts/new_book.py "$book_title" "$book_author" 2>/dev/null
            check_exit
			;;
		r)
			list_db
			echo -n "Enter book id: "
			read rm_id
			confirm "rm_book.py" $rm_id
			;;
		p)
			list_db
			echo -n "Enter book id: "
			read prog_id
			confirm	"prog_book.py" $prog_id
			;;
		e)
            echo "Building..."
			scripts/build_html.py > docs/index.html
			echo "Done!"
			echo "Goodbye."
			exit 0
			;;
		*)
			echo "Unknown action."
			;;
	esac
done
