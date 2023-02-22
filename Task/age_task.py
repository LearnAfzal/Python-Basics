smith=25
john=45
henry=65
if smith<john and smith<henry:
    print("smith is younger")
elif john<smith and john<henry:
    print("john is younger")
elif henry<smith and henry<john:
    print("henry is younger")
elif smith==john and john==henry:
    print("smith,john,henry are same age")
