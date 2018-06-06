str = "this is string example....wow!!!";
print "str.capitalize() : ", str.capitalize()
print ""

str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.lower()
print ""

str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix)
print str.endswith(suffix,20)

suffix = "is";
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)
print ""

str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)


