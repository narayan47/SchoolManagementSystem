def write_html(child_field):
    import webbrowser

    filename = child_field + "_dropdown.html"

    f = open( filename, 'wb' )

    message = """
	<html>
	<head></head>
	<body>



	<option value="">---------</option>
	# {% for var in forms%}
	# <option value="{{var.pk }}">{{var.section_name }}</option>
	# {% endfor %}


	</body>
	</html>
	"""

    f.write( message.encode() )
    f.close()


write_html( child_field='section_name' )
# import webbrowser

# f = open('helloworld.html','wb')

# message = """<html>
# <head></head>
# <body><p>Hello World!</p></body>
# </html>"""

# f.write(message)
# f.close()
