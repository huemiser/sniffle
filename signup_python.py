import bottle
@bottle.get('/signup')
@bottle.post('/signup')
def signup():
    with open('signup.html') as template:
        name = bottle.request.forms.get('name')
        email = bottle.request.forms.get('email')
        password1 = bottle.request.forms.get('password1')
        password2 = bottle.request.forms.get('password2')
        likes = bottle.request.forms.get('likes')
        well = ''
        no_content = ''
        for field in ["name", "email", "password1", "password2", "likes"]:
            if not bottle.request.forms.get(field):
                no_content = "You didn't fill all the fields"
            elif password2 != "":
                if password1 != password2:
                    well = "password doesn't match"
                else:
                    well = ''
        return bottle.template(template.read(), okOrNot = well, no_content = no_content)

@bottle.get("/confirm")
def confirm():
    with open('done.html') as template:
        username23 = bottle.request.forms.get('email', None)
        pass23 = bottle.request.forms.get('password2', None)
        if username23 and pass23:
            return bottle.template(template.read(), usrn = "username: ", realusrn = username23, passw = "password: ", realpassw = pass23)
        else:
            return "something went wrong"


@bottle.get("/static/<filename:path>")
def static_file(filename):
    return bottle.static_file(filename, root="static/")
bottle.run(port=8080, debug=True)
