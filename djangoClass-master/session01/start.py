nombre="cesar"


print(nombre)
print(type(nombre))


tmp=nombre.upper()
print(tmp)



score=20
print(score)
print(type(score))


tmp1=11.4
print(tmp1)
print(type(tmp1))


you_passed_the_exam=True
# you_passed_the_exam=False


import datetime

actual_time=datetime.datetime.now()


print(f"The time now is {actual_time}")


#list
# List are mutables
languages=['Python', 'Java','PHP','Javascript']
print(type(languages))
languages.append('Kottlin')
# languages.insert()
print(languages[3])

languages.insert(2,'C++')

print(languages)

languages[2]='c#'
print(languages)


languages.remove('Kottlin')
print(languages)


print('*********************************')
del languages[3]
print(languages)


#tuples
frameworks=('Laravel', 'Django','Flask','FastAPI')
print(frameworks)
print(type(frameworks))



#dictionary

my_dictionary={'name':'Juan',
                'surname':'castro',
                'birtday':"09/20/1992",
                'weight':89,
                'averaged':17.89,
                'license':True,
                'graduated':True,
                'uptodate with payment':True}

print(my_dictionary)
print(type(my_dictionary))


#sets
average_scores={13.5,20,2.2,10.5,3.2,15,15}
print(average_scores)
print(type(average_scores))



abc='asdf;lkhqwerzxclj'
print(abc[:6])
print(abc[1:2])