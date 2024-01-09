from ToolSets import *

# MainWindow - Class that incorporates all of the PyQt components that are necessary for a GUI in this program
# Constructor
#   * Set the title of the window
#   * Set the minimum height and width of the window
#   * Generate the main layouts of the window
#   * Generate the nested layouts for the main layouts
#   * Generate the widgets for the encode column
#       * Set the default values of each widget
#       * Set alignments and object names of each widget
#       * Add widgets to nestedEncodeLayout
#   * Generate the widgets for the decode column
#       * Set the default values of each widget
#       * Set alignments and object names of each widget
#       * Add widgets to nestedDecodeLayout
#   * Generate the widgets for the results row
#       * Set the default values of each widget
#       * Set alignments and object names of each widget
#       * Add widgets to mainResultsLayout
#   * Add the Encode and Decode layouts to mainInputLayout
#   * Add the Input and Results layouts to mainLayout
#   * Set the main layout
#   * Set the central layout
# ClearInputs - See inline comments
# Decode - See inline comments
# Encode - See inline comments
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("RSA")
        # Height and Width of Window
        self.resize(850,500)
        self.setMinimumWidth(850)
        self.setMinimumHeight(400)
        # Main Layouts
        mainLayout = QVBoxLayout()
        mainInputLayout = QHBoxLayout()
        mainEncodeLayout = QVBoxLayout()
        mainDecodeLayout = QVBoxLayout()
        mainResultsLayout = QVBoxLayout()
        # Nested Layouts
        nestedEncodeLayout = QGridLayout()
        nestedDecodeLayout = QGridLayout()
        # Encode Column Widgets
        encodeColumnTitle = QLabel("Encode Message")
        encodeColumnTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        encodeMessage = QTextEdit()
        encodeMessage.setPlaceholderText("Enter Message Here...")
        encodeMessage.setObjectName("encodeMessage")
        encodePublicKey = QLineEdit()
        encodePublicKey.setPlaceholderText("Enter Public Key Here...")
        encodePublicKey.setMaxLength(10000)
        encodePublicKey.setMinimumWidth(400)
        encodePublicKey.setObjectName("encodePublicKey")
        encodenValue = QLineEdit()
        encodenValue.setPlaceholderText("Enter n Value Here...")
        encodenValue.setMaxLength(10000)
        encodenValue.setMinimumWidth(400)
        encodenValue.setObjectName("encodenValue")
        encodeButton = QPushButton("Encode Message")
        encodeButton.setObjectName("encodeButton")
        encodeButton.clicked.connect(self.Encode)
        # Add Widgets To nestedEncodeLayout Layout
        nestedEncodeLayout.addWidget(encodeColumnTitle, 0,0)
        nestedEncodeLayout.addWidget(encodeMessage,1,0)
        nestedEncodeLayout.addWidget(encodePublicKey,2,0)
        nestedEncodeLayout.addWidget(encodenValue,3,0)
        nestedEncodeLayout.addWidget(encodeButton,4,0)
        mainEncodeLayout.addLayout(nestedEncodeLayout)
        # Decode Column Widgets
        decodeColumnTitle = QLabel("Decode Message")
        decodeColumnTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        decodeMessage = QTextEdit()
        decodeMessage.setPlaceholderText("Enter Message Here...")
        decodeMessage.setObjectName("decodeMessage")
        decodePrivateKey = QLineEdit()
        decodePrivateKey.setPlaceholderText("Enter Private Key Here...")
        decodePrivateKey.setMaxLength(10000)
        decodePrivateKey.setMinimumWidth(400)
        decodePrivateKey.setObjectName("decodePrivateKey")
        decodenValue = QLineEdit()
        decodenValue.setPlaceholderText("Enter n Value Here...")
        decodenValue.setMaxLength(10000)
        decodenValue.setMinimumWidth(400)
        decodenValue.setObjectName("decodenValue")
        decodeButton = QPushButton("Decode Message")
        decodeButton.setObjectName("decodeButton")
        decodeButton.clicked.connect(self.Decode)
        # Add Widgets To nestedDecodeLayout Layout
        nestedDecodeLayout.addWidget(decodeColumnTitle,0,0)
        nestedDecodeLayout.addWidget(decodeMessage,1,0)
        nestedDecodeLayout.addWidget(decodePrivateKey,2,0)
        nestedDecodeLayout.addWidget(decodenValue,3,0)
        nestedDecodeLayout.addWidget(decodeButton,4,0)
        mainDecodeLayout.addLayout(nestedDecodeLayout)
        # Results Row Widgets
        resultsRowTitle = QLabel("Encoding / Decoding Results")
        resultsRowTitle.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        resultsRowTitle.setObjectName("resultsRowTitle")
        encodingDecodingResults1 = QTextEdit()
        encodingDecodingResults1.setPlaceholderText("Encoding / Decoding Results Here...")
        encodingDecodingResults1.setMaximumHeight(400)
        encodingDecodingResults1.setObjectName("encodingDecodingResults1")
        encodingDecodingResults2 = QTextEdit()
        encodingDecodingResults2.setPlaceholderText("Private Key / Public Key Here...")
        encodingDecodingResults2.setMaximumHeight(400)
        encodingDecodingResults2.setObjectName("encodingDecodingResults2")
        resultsRowClearButton = QPushButton("Clear Entries")
        resultsRowClearButton.setObjectName("clearResultsButton")
        resultsRowClearButton.clicked.connect(self.ClearInputs)
        # Add Widgets to Results Layout
        mainResultsLayout.addWidget(resultsRowTitle)
        mainResultsLayout.addWidget(encodingDecodingResults1)
        mainResultsLayout.addWidget(encodingDecodingResults2)
        mainResultsLayout.addWidget(resultsRowClearButton)
        # Add Layouts to mainInputLayout
        mainInputLayout.addLayout(mainEncodeLayout)
        mainInputLayout.addLayout(mainDecodeLayout)
        # Add Layouts to Main Layout
        mainLayout.addLayout(mainInputLayout)
        mainLayout.addLayout(mainResultsLayout)
        # Set Main Layout
        widget = QWidget()
        widget.setLayout(mainLayout)
        # Set The Central Widget
        self.setCentralWidget(widget)

    # ClearInputs - Clears the inputs in the window
    def ClearInputs(self):
        # Grab children from main window
        decodeButton = self.findChild(QPushButton,"decodeButton")
        decodeMessage = self.findChild(QTextEdit,"decodeMessage")
        decodenValue = self.findChild(QLineEdit,"decodenValue")
        decodePrivateKey = self.findChild(QLineEdit,"decodePrivateKey")
        encodeButton = self.findChild(QPushButton,"encodeButton")
        encodeMessage = self.findChild(QTextEdit,"encodeMessage")
        encodenValue = self.findChild(QLineEdit,"encodenValue")
        encodePublicKey = self.findChild(QLineEdit,"encodePublicKey")
        resultsTitle = self.findChild(QLabel,"resultsRowTitle")
        encodingDecodingResults1 = self.findChild(QTextEdit,"encodingDecodingResults1")
        encodingDecodingResults2 = self.findChild(QTextEdit,"encodingDecodingResults2")
        # Enable buttons
        encodeButton.setEnabled(True)
        decodeButton.setEnabled(True)
        # Clear text edit boxes
        encodeMessage.clear()
        decodeMessage.clear()
        encodingDecodingResults1.clear()
        encodingDecodingResults2.clear()
        # Clear line edit boxes
        decodenValue.clear()
        decodePrivateKey.clear()
        encodenValue.clear()
        encodePublicKey.clear()
        # Clear labels
        resultsTitle.setText("Encoding / Decoding Results")

    # Decode - Decodes a message from the decode text box, private key and n value line edits
    def Decode(self):
        # Grab children from main window (convert them to their correct data types if necessary)
        decodeMessageText = str(self.findChild(QTextEdit,"decodeMessage").toPlainText())
        decodePrivateKey = str(self.findChild(QLineEdit,"decodePrivateKey").text())
        decodenValue = str(self.findChild(QLineEdit,"decodenValue").text())
        encodeButton = self.findChild(QPushButton,"encodeButton")
        decodeButton = self.findChild(QPushButton,"decodeButton")
        encodeButton.setEnabled(False)
        decodeButton.setEnabled(False)
        resultsTitle = self.findChild(QLabel,"resultsRowTitle")
        decodingResults = self.findChild(QTextEdit,"encodingDecodingResults1")
        publicPrivateKey = self.findChild(QTextEdit,"encodingDecodingResults2")
        # Create place holders for return values
        decodedMessage = ""
        # Make sure that all fields are entered
        if (decodeMessageText.strip() != "" and decodePrivateKey != "" and decodenValue != ""):
            # Convert entries to correct data types
            decodeMessage = ast.literal_eval(self.findChild(QTextEdit,"decodeMessage").toPlainText())
            decodenValue = int(decodenValue)
            decodePrivateKey = int(decodePrivateKey)
            decodedMessage = Decode(decodenValue,decodePrivateKey,decodeMessage)
            # Update the labels in the main window with the results from the decoding
            resultsTitle.setText("Decoding Results")
            decodingResults.append("Decoded Message: " + str(decodedMessage))
            publicPrivateKey.append("Private Key d = " + str(decodePrivateKey) + ", n = " + str(decodenValue))
        else:
            encodeButton.setEnabled(True)
            decodeButton.setEnabled(True)

    # Encode - Encodes a message from the encode text edit box
    def Encode(self):
        # Grab children from main window (convert them to their correct data types if necessary)
        encodeMessage = self.findChild(QTextEdit,"encodeMessage").toPlainText()
        encodenValueText = str(self.findChild(QLineEdit,"encodenValue").text())
        encodePublicKeyText = str(self.findChild(QLineEdit,"encodePublicKey").text())
        encodeButton = self.findChild(QPushButton,"encodeButton")
        decodeButton = self.findChild(QPushButton,"decodeButton")
        encodeButton.setEnabled(False)
        decodeButton.setEnabled(False)
        resultsTitle = self.findChild(QLabel,"resultsRowTitle")
        encodingResults = self.findChild(QTextEdit,"encodingDecodingResults1")
        publicPrivatekey = self.findChild(QTextEdit,"encodingDecodingResults2")
        # Create place holders for values
        encodedMessage = ""
        nValue = 0
        publicKey = 0
        privateKey = 0
        # Check if public key and n value are empty
        if (encodenValueText == "" and encodePublicKeyText == ""):
            # Generate random prime numbers
            firstSeed = random.randrange(100,1000)
            secondSeed = random.randrange(2,10)*firstSeed
            firstPrime = GeneratePrime(firstSeed,secondSeed)
            secondPrime = GeneratePrime(10*firstSeed,10*secondSeed)
            # Calculate the public and private keys using the Second Tool Set module (STS)
            nValue = Find_Public_Key_e(firstPrime,secondPrime)[1]
            publicKey = Find_Public_Key_e(firstPrime,secondPrime)[0]
            privateKey = Find_Private_Key_d(publicKey,firstPrime,secondPrime)
            # Encode the message using the Encode / Decode module (ED)
            encodedMessage = Encode(nValue,publicKey,encodeMessage)
        # Check if the user has entered a public key and n value
        elif (encodenValueText != "" and encodePublicKeyText != ""):
            # Convert the entries to integers
            nValue = int(encodenValueText)
            publicKey = int(encodePublicKeyText)
            # Encode the message using the Encode / Decode module (ED)
            encodedMessage = Encode(nValue,publicKey,encodeMessage)
        if ((encodenValueText == "" and encodePublicKeyText == "") or (encodenValueText != "" and encodePublicKeyText != "")):
            # Update the labels in the main window with the results from the encoding
            resultsTitle.setText("Encoding Results")
            encodingResults.append("Encoded Message: " + str(encodedMessage))
            publicPrivatekey.append("Public Key e = " + str(publicKey) + ", Private Key d = " + str(privateKey) + ", n = " + str(nValue))


# Run - Runs the program
# Input:
#   This function does not have any inputs
# Algorithm:
#   * Create a QApplication instance
#   * Create a window and show it
#   * Kill the application upon closing
# Output:
#   This application does not return a value
def Run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())