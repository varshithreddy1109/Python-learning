'''
                       USING AND OPERATOR
'''
has_high_income = True
has_high_credit = False

if has_high_income and has_high_credit :
    print("Eligible for loan")
else:
    print("Not eligible")
#when we use and both should be true
'''
                    USING OR OPERATOR
'''
has_high_income = True
has_high_credit = False

if has_high_income or has_high_credit :
    print("Eligible for loan")
else:
    print("Not eligible")
#when we use and both should be true
'''
                and-both conditions should be true
                or-atleast one
                not-
'''

'''
                      USING NOT OPERATOR
'''
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else : 
    print("Not eligible")