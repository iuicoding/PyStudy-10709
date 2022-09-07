#구문 오류
#코드에 문제가 있어서
#실행X
#print("실행되었습니다")
#print("ㅇㅂㅇ)

#while True:
#    string_input = input("정수 입력: ")
#    if string_input.isdigit():
#        number_input_a = int(string_input)
#        print("원의 반지름: ", number_input_a)
#        print("원의 둘레: ", 2*3.14*number_input_a)
#        print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
#        break
#    else:
#        print("정수를 입력해주세요!")

#while True:
#    try:
#        #예외가 발생할 수 있는 가능성이 있는 코드
#        print(float(input(">숫자를 입력해주세요: "))**2)
#        break
#    except:
#        pass

#list_a = ["52", "273", "32", "스파이", "103"]
#
#list_b = []
#for item in list_a:
#    try:
#        float(item)
#        list_b.append(item)
#    except:
#        pass
#
#print("{}내부에 있는 숫자는".format(list_a))
#print("{}입니다".format(list_b))


#def test():
#    print("text()함수의 첫 줄입니다.")
#    try:
#        print("try구문이 실행되었습니다.")
#        ㅇㅂㅇ.ㅇㅂㅇ()
#        return
#        print("try 구문의 return 키워드 뒤입니다.")
#    except:
#        print("except 구문이 실행되었습니다")
#    finally:
#       print("finally 구문이 실행되었습니다.")
#   print("test()함수의 마지막 줄입니다.")
#
#test()

#students = [
#    {"name": "이준혁", "korean": 87, "math": 98, "english": 88, "science": 95},
#    {"name": "신재용", "korean": 92, "math": 98, "english": 88, "science": 95},
#    {"name": "나강민", "korean": 76, "math": 98, "english": 88, "science": 95},
#    {"name": "최동은", "korean": 98, "math": 98, "english": 88, "science": 95},
#    {"name": "황규연", "korean": 95, "math": 98, "english": 88, "science": 95},
#    {"name": "백승훈", "korean": 64, "math": 98, "english": 88, "science": 95},
#]

#def 총점(student):
#    return student["korean"] + student["math"] +\
#        student["english"] + student["science"]
#def 평균(student):
#    return 총점(student) / 4
#def 출력(student):
#   print(student["name"], 총점(student), 평균(student), sep="\t")
#
#
#print("이름", "총점", "평균", sep="\t")
#for student in students:
#    출력(student)



#class Student:
#    def __init__(self, 이름, 나이):
#        print("객체가 생성되었습니다")
#        self.이름=이름
#        self.나이=나이
#    def __del__(self):
#        print("객체가 소멸되었습니다")
#    def 출력(self):
#        print(self.이름, self.나이)
#
#student = Student("운인성", 3)
#student.출력()












