name=input("enter A name:- ")
name_title=name.title()
space_index=name_title.index(" ")
initials=name_title[0]+name_title[space_index+1]
print("initials are:- ",initials)

