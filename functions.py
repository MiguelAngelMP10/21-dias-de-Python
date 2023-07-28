def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Playground - retorna el tipo
def found_type(value):
    # Tu código aquí 👇
    return type(value)
    pass


# Playground - calcula la propina
def calculate_tip(bill_amount, tipPercentage):
    if bill_amount >= 0 and tipPercentage >= 0:
        return round(bill_amount * tipPercentage / 100, 2)
    else:
        print("Ingrese valores mayores a 0")
        return False


# Playground - averigua si un año es bisiesto
def is_leap_year(year):
    # tu código aquí 👈
    if year % 1 != 0 or year <= 0:
        return False

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        return True
    return False


# Playground - Dibuja un triangulo usando bucles
def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return triangle


# Encuentra a los gatitos más famosos
def find_famous_cat(cats):
    most_followers = []
    total_followers = []

    # se suman los followers en una lista
    for cat in cats:
        total_followers.append(sum(cat["followers"]))

    # se consigue el máximo
    max_followers = max(total_followers)

    # se añaden los nombres de quienes tengan el max
    for idx, followers in enumerate(total_followers):
        if followers == max_followers:
            most_followers.append(cats[idx]["name"])
    return most_followers


# Obtén el promedio de los estudiantes
def get_student_average(students):
    # Tu código aquí 👈
    students_average = {'class_average': 0.0, 'students': []}
    class_size = len(students)
    class_total = 0

    for student in students:
        student_average = round(sum(student['grades']) / len(student['grades']), 2)
        class_total += student_average
        students_average['students'].append({
            'name': student['name'],
            'average': student_average
        })

    students_average['class_average'] = round(class_total / class_size, 2)
    return students_average


def get_packages_info(packages):
    # Tu código aquí 👈
    packages_info = {
        'total_weight': 0,
        'destinations': {
        }
    }

    total_weight = 0
    for package in packages:
        total_weight += package[1]
        country_key = package[2]
        if country_key in packages_info['destinations']:
            packages_info['destinations'][country_key] += 1
        else:
            packages_info['destinations'][country_key] = 1

    packages_info['total_weight'] = round(total_weight, 2)
    return packages_info


# Calcula la cantidad de letras en una oración
def count_letters(phrase):
    # Tu código aquí 👈
    counter = {}
    for letter in phrase:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


# Encuentra el mayor palíndromo

def find_largest_palindrome(words):
    largest = 0
    palindrome = ""

    for word in words:
        if word == word[::-1]:
            if len(word) > largest:
                palindrome = word
                largest = len(word)

    return palindrome if palindrome else None


# Encuentre la intersección de conjuntos
def find_set_intersection(sets):
    if not sets:
        return set()
    intersection = sets[0]
    for i in sets[1:]:
        intersection &= i
    return intersection


# Filtra mensajes de un user específico
def filter_user_messages(messages, user):
    filtered = list(filter(lambda msg: msg["sender"].upper() == user.upper(), messages))
    return filtered


# Crea tu propio método map
def my_map(list, func):
    # Tu código aquí 👈
    return [func(x) for x in list]


# Encuentra palabras con dos vocales
def count_words_by_length(words):
    # Tu código aquí 👈
    list_word = [len(word) for word in words]
    return {word: list_word.count(word) for word in list_word}


# Maneja correctamente los errores
def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("La lista está vacía")

    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("La lista contiene elementos no numéricos")

    avg = sum(numbers) / len(numbers)
    return avg


# Maneja las excepciones
def calculate_discounted_price(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("El precio y el descuento deben ser números")

    if price < 0 or discount < 0:
        raise ValueError("El precio y el descuento deben ser valores positivos")

    try:
        return price - (price * discount)
    except Exception as e:
        raise Exception(f"Ha ocurrido un error inesperado")


# Playground - Crea un task manager usando closures
def createTaskPlanner():
    # Tu código aquí 👇

    list_taks = []

    def addTask(task):
        # Tu código aquí 👇
        task['completed'] = False
        list_taks.append(task)

    def removeTask(value):
        # Tu código aquí 👇
        for item in list_taks:
            if item['id'] == value or item['name'] == value:
                list_taks.remove(item)

    def getTasks():
        # Tu código aquí 👇
        return list_taks

    def getPendingTasks():
        # Tu código aquí 👇
        return [item for item in list_taks if item['completed'] == False]

    def getCompletedTasks():
        # Tu código aquí 👇
        return [item for item in list_taks if item['completed'] == True]

    def markTaskAsCompleted(value):
        # Tu código aquí 👇
        for item in list_taks:
            if item['id'] == value or item['name'] == value:
                item['completed'] = True

    def getSortedTasksByPriority():
        # Tu código aquí 👇
        taks_priority = list_taks.copy()
        taks_priority.sort(key=lambda x: x['priority'])
        return taks_priority

    def filterTasksByTag(tag):
        # Tu código aquí 👇
        tags_list = []
        for item in list_taks:
            for i in range(len(item['tags'])):
                if item['tags'][i] == tag:
                    tags_list.append(item)
        return tags_list

    def updateTask(taskId, updates):
        # Tu código aquí 👇
        for i in range(len(list_taks)):
            if list_taks[i]['id'] == taskId:
                list_taks[i].update(updates)

    return {
        'addTask': addTask,
        'removeTask': removeTask,
        'getTasks': getTasks,
        'getPendingTasks': getPendingTasks,
        'getCompletedTasks': getCompletedTasks,
        'getSortedTasksByPriority': getSortedTasksByPriority,
        'markTaskAsCompleted': markTaskAsCompleted,
        'filterTasksByTag': filterTasksByTag,
        'updateTask': updateTask
    }
