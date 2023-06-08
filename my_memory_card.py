from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle, randint

class  Question ():
        def __init__(self,question,right_answer, wrong1,wrong2,wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

question_list = []
question_list.append(Question("Kada je palo Zapadno Rimsko carstvo?","476.god","467.god","671.god", "845.god"))
question_list.append(Question("Kada je Cristofer Columbo otkrio Ameriku?","1492.god","1592.god","1389.god","782.god"))
question_list.append(Question("Kada su Huni dostigli najvecu moc","434-453","672-812","456-512","345-425"))
question_list.append(Question("Kada je Karlo Veliki krunisan za kralja","800.god.","900.god","565.god","745.god"))
question_list.append(Question("Kada su Homadska plemena Huni prosli kroz vrata naroda", "375.god","370.god","567.god","373.god"))
question_list.append(Question("Od kad do kad je vladao car Justinijan","527-567","657-690","238-386","534-587"))
question_list.append(Question("Ko je osnivac islama","Muhamed","Djuro","Amer","Georgije"))
question_list.append(Question("Kako su oznacavali gde da naprave kule","Bacanjem strele","Bacanjem kamena","Basanjem vode","Bacanjem makaza"))
question_list.append(Question("Kada je bio boj na Kosovu","1389","1400","1489","1387"))
question_list.append(Question("Ko je izvrsio antentan za Fendinarta","Gavrilo princim","Georgije","Djurdjevic Marko","Konstantin"))
app = QApplication([])
lb_Question = QLabel("Kako se zove nastavnik?")#kreirali pitanje
btn_Answer = QPushButton('Answer')
RadioGroupBox = QGroupBox("Answer options")#kreirali group box

rbtn_1 = QRadioButton("Pero")#kreirali prvi odg
rbtn_2 = QRadioButton("Milijan")
rbtn_3 = QRadioButton("Obrad")
rbtn_4 = QRadioButton("Andjela")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_answer1 = QHBoxLayout()#u gropu boxu kreirali 3 linije
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(rbtn_1)#dodajemo pitanja na prvu liniju
layout_answer2.addWidget(rbtn_2)
layout_answer3.addWidget(rbtn_3)
layout_answer3.addWidget(rbtn_4)


layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)

RadioGroupBox.setLayout(layout_answer1)
 

AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel ("True/False")
lb_Correct = QLabel ("Correct answer")

layout_result = QVBoxLayout()
layout_result.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_result)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Answer, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_Answer.setText("Next question")

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_Answer.setText("Answer")
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
    
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask (q:Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()
def show_correct(res):
        lb_Result.setText(res)
        show_result()

def chech_answer():
        if answers[0].isChecked():
            show_correct("Correct!")
            window.score+=1
            print("Statistic \n - Total questions:", window.total, "\n - Right answers:",window.score)
            print("Rating:",(window.score / window.total)*100, "%")
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct("Incorrect")

def next_question():
        window.total += 1
        print("Statistic \n - Total questions:", window.total, "\n - Right answers:",window.score)
        cur_question = randint(0, len(question_list)-1) 
        q = question_list[cur_question]
        ask(q)

def click_OK():
        if btn_Answer.text() == "Answer":
                chech_answer()
        else:
                next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle("Memo card")
window.cur_question = -1

btn_Answer.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()


window.show()
app.exec()