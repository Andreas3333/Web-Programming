# Web-Programming
This reposity serves to hold a minimal instance of a web page.
Implemented with the Python web frame work Flask and its utilities.
As well as Mongita for implementing a lightweight NOSQL embedded datbase


Project Description:

###---Women's Clothing and Cosmetics webpage---###

Technoligies in Use:

	Python-
		Flask framework;

			•Allowed for implementing http GET POST methods to serve
			communication between client and server, from html forms
			sending data, and returning routs for page requests.
			
			•Included libraries: Jinja template engien and Werkzeug utilities

			_page routes: serve routes to pages of the site.
				-namespaces:
					render_template, redirect, request, url_for

			_session/cookies user data storage: data about the user is stored as
				a refrencable obj for the length of the browsing session in a 
				users browser as a cookie.(may opt to change for diffrent 
				persistance of data storage)
				-namespace:
					session

			_password encription: allow for store of enchripted user passwords.
				-Werkzeug.security library:
					-namespaces:
						generate_password_hash, check_password_hash

			

				




:Product Overview:

--well designed front facing web page with reactivity.
^^ we will get there 


Site Layout/Navigation:
	
	(possible feature addition, an event pop window appears after for
	a user to login after an amount of browsing time has elapsed) 


Index:
	Index page serves as static retreval point.

Home Page:
	('/') Default destination page of the site is the Hame Page.
	A user may arrive and navigate here without being logged in, 
	however to perform any user relation acctions the user must 
	log in.
	<a href>'s For Navigation to:
		Products Page.
		Login Page.
		Create New Account.
		Logout.
	
Products Page:
	The main content browsing page of the site, where a non-logedin 
	user can browse and a loged in user may add items to thier cart.
	<a href>'s For Navigation to:
		Login.
		Home Page.
		Logout.




Features:

	Shopping cart-

		(temporary object linked to a user until it is emptied by either removing all the items,
		 purchasing items or deleting the cart completely)

			•should be able to persist over browsing sessions
			•should be able to add an item
			•should be able to remove/delete an item

	Account-
		•user account should have a username and password for access
		•user account should maintain user details
			--shipping address
			--payment methods
			--purchases history

		
	Transactions-
		•should be able to make purchases of items on webpage
		•complete purchases by committing and transacting.




:Front end-:

html 
forms
if i have time
-bootstrap for improved graphical webpage interface




:Back end-:

service all the needs of the working web page





:Data base-:

hold all nessiary data:
	•user account info
	transaction info

create reports:
	•on user sessions
	•analytics of products sold
	(performed through executing quiries)

what kind of data base should be used for the webpage and for secondary storage database(used for report and analytics building)

possibly develop a data pipeline from the webpage data base to a second storage data base







