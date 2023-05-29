from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
import yfinance
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sent as sentA

def main(): #the main GUI
    global keys
    keys = {}
    
    app = QApplication([])#creates our applications and windows
    window = QWidget()
    global window2
    window2 = QWidget()
    window.setGeometry(0,0,3000,2000)

    layout  = QVBoxLayout()#creates 3 layouts the bottom 2 go inside of the top one
    #QVBox stacks them on top of each other
    labelLayout = QHBoxLayout() #stacks side to side

    resultsLayout = QHBoxLayout()

    stockInstructions = QLabel("Enter Stock Tag")#creates a label for insturctions
    graphButton = QPushButton("Get Stock Graph") #creates a button for getting the stock graph
    graphButton.clicked.connect(lambda: graph())#connects button to the function graph which creates the graph
    sentAnalysisIntructions = QLabel("Enter Keywords and Weights") #more instructions
    resultsButton = QPushButton("Run Sentiment Analysis") #creates button to run sentiment analysis
    resultsButton.clicked.connect(lambda: runSent()) #connects button to runSent method that runns teh sent.py main method
    stockInstructions.setFont(QFont("Arial",18)) #sets font
    graphButton.setFont(QFont("Arial",18))
    sentAnalysisIntructions.setFont(QFont("Arial",18))
    resultsButton.setFont(QFont("Arial",18))

    labelLayout.addWidget(stockInstructions)#adds these widgets to layout
    labelLayout.addWidget(graphButton)
    labelLayout.addWidget(sentAnalysisIntructions)
    labelLayout.addWidget(resultsButton)
    
    global stockTextBox
    stockTextBox = QLineEdit()#A edit box for the stock that wants to be graphed
    global stockGraph
    stockGraph = QLabel()#the label that stores the graph
    openKeyWindow = QPushButton("                                            ")#button for opening the second window for entering keys
    openKeyWindow.clicked.connect(lambda: getKeyWindow())#connects to method that opens the window2
    global resultsText
    resultsText = QLabel("                                               ")# label that holds the results
    resultsText.setFont(QFont("Arial",18))

    resultsLayout.addWidget(stockTextBox)#saves to layout
    resultsLayout.addWidget(stockGraph)
    resultsLayout.addWidget(openKeyWindow)
    resultsLayout.addWidget(resultsText)

    layout.addLayout(labelLayout) #adds layouts to parent layout
    layout.addLayout(resultsLayout)

    #.setFont(QFont("Arial",18))
    window.setLayout(layout)

    window.show()
    app.exec_()

def graph():
    stock = yfinance.Ticker(stockTextBox.text())#gets price for 1y from the given stock
    history = stock.history(period='1y')

    fig = make_subplots(specs=[[{"secondary_y": True}]])#creates a candle stick plot with plotly
    fig.add_trace(go.Candlestick(x=history.index,open=history['Open'],high=history['High'],low=history['Low'],close=history['Close']))

    fig.write_image("graph.png")#saves image

    print("done writing")

    stockGraph.setPixmap(QPixmap('graph.png')) #updates stockGraph with saved image

def getKeyWindow():
    window2.setGeometry(0,0,1000,1000)#sets widnwos size

    layout  = QVBoxLayout()#sets new layout

    keyDiscription = QLabel("Enter Keys") #instrucions
    global keyTextBox
    keyTextBox = QLineEdit()#text box where you enter the keys for the sentiment analysis
    weightDiscription = QLabel("Enter Weights") #insructions
    global weightTextBox
    weightTextBox = QLineEdit()#text box where you enter the weights for the sentiment analysis
    getKeysButton = QPushButton("Get Keys")
    getKeysButton.clicked.connect(lambda: getKeys())#connects button that saves keys to the function
    keyDiscription.setFont(QFont("Arial",18))
    keyTextBox.setFont(QFont("Arial",18))
    weightDiscription.setFont(QFont("Arial",18))
    weightTextBox.setFont(QFont("Arial",18))
    getKeysButton.setFont(QFont("Arial",18))

    layout.addWidget(keyDiscription)
    layout.addWidget(keyTextBox)
    layout.addWidget(weightDiscription)
    layout.addWidget(weightTextBox)
    layout.addWidget(getKeysButton)

    window2.setLayout(layout)#saves layout

    window2.show()
def getKeys():
    keyList = keyTextBox.text().split(",")
    weightList = weightTextBox.text().split(",") #splits both the keys and the weights into a list

    for x in range(len(keyList)):
        keys.update({keyList[x]:float(weightList[x])})#creates a dictionary from the lists

    window2.close()

def runSent():
    sent = sentA.main(keys) #runs sent with the key dic

    finalStr = ""
    for x in sent:
        finalStr += (x+"\n")#saves the sents in a multiline stirng
    
    print(finalStr)

    resultsText.setText(finalStr)#saves results

if __name__ == '__main__':
    main()
