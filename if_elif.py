print("Question 10")

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
print(traffic_report('yellow'))

def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

print(fruit_color('pear'))

print("Question 12")

def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'
print(grade_report(50))
print(grade_report(70))
print(grade_report(40))
print(grade_report(80))

# For python visualizer
def greeting(name):
    return 'Hi, ' + name

def exclaim(statement):
    return statement + '!'

def enthusiastic_greeting(name):
    greeting_message=exclaim(greeting(name))
    print(greeting_message)

enthusiastic_greeting('Orion')

