import json
people={
        'person1':{'name':'Jim',
                 'age':30,
                 'skills':['computer vision','statistics']},
        
        'person2':{'name':'Jane',
                 'age':28,
                 'skills':['ai','calculus']}   ,
        'person3':{'name':'Jack',
                 'age':29,
                 'skills':['ai','calculus','statistics','machine learning']}   ,
        'person4':{'name':'Jose',
                 'age':27,
                 'skills':['ai','calculus','mlops']} ,
        'person5':{'name':'Jill',
                 'age':29,
                 'skills':['LLMops','calculus','mlops']} ,
        'person6':{'name':'Jira',
                 'age':27,
                 'skills':['ML','data science','mlops']}  

                 
        }
with open('people.json','w') as f:
      json.dump(people,f,indent=4)
      