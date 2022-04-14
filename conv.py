#!/usr/bin/env python3
import codecs
import sys

def main():

    #Check that the amount of arguments provided is correct
    if(len(sys.argv) != 3):
        manual()
        exit()

    #Get the input and output type
    inputType = sys.argv[1][0]
    outputType = sys.argv[1][1]

    #Get the input data
    inputData = sys.argv[2]

    #Convert the data into hex
    hexData = inputToHex(inputData, inputType)
    
    #Convert the hex data to desired output and print
    print(str(hexToOutput(hexData, outputType)))

#Converts the input data of a particular type to hex
def inputToHex(data, dataType):
    if(dataType == "b"):
        return binaryToHex(data)
    if(dataType == "x"):
        return hexToHex(data)
    if(dataType == "d"):
        return decimalToHex(data)
    if(dataType == "s"):
        return stringToHex(data)

#Converts the hex input data to a particular type
def hexToOutput(data, dataType):
    if(dataType == "b"):
        return hexToBinary(data)
    if(dataType == "x"):
        return data   
    if(dataType == "d"):
        return hexToDecimal(data)
    if(dataType == "s"):
        return hexToString(data)

#Formats hex to what program accepts
def hexToHex(hexData):
    hexData = hexData.lower()
    if(hexData[0:2] != "0x"):
        hexData = "0x" + hexData
    return hexData

#Converts binary to hexadecimal
def binaryToHex(binaryData):
    count = 0
    end = False
    while end == False:
        if(binaryData[count] == "0"):
            count = count + 1
        else:
            end = True
    #Add the zero padding back
    padding = "0" * (count // 4)
    unPadded = str(hex(int(binaryData, 2)))
    return unPadded[0:2] + padding + unPadded[2:]

#Converts decimal to hexadecimal
def decimalToHex(decimalData):
    return hex(int(decimalData))

#Converts string to hexadecimal
def stringToHex(stringData):
    temp = codecs.encode(stringData.encode("utf-8"), "hex")
    return "0x" + str(temp.decode("utf-8"))

#Converts hexadecimal to ASCII string
def hexToString(hexData):
    return bytes.fromhex(str(hexData)[2:]).decode("ASCII")

#Converts hexadecimal to decimal
def hexToDecimal(hexData):
    return int(hexData, 16)

#Converts hexadecimal to binary
def hexToBinary(hexData):
    numOfBits = (len(hexData) - 2) * 4
    return bin(int(hexData, 16))[2:].zfill(numOfBits)

#Simple manual
def manual():
    print("Supports conversions between")
    print("  (b)inary")
    print("  he(x)")
    print("  ascii (s)tring")
    print("  (d)ecimal")
    print("To use: ./conv <inputFormat><outputFormat> <inputData>")
    print("  <inputFormat> and <outputFormat> is the letter in brackets in supported formats")
    print("  EG: `./conv xd 0x1337` converts the hexadecimal value 0x1337 to decimal")
    print("  EG: `./conv sb 'hi there'` converts the string 'hi there' to binary")
    print("I just tested the bare essentials, will probably get around to improving it later")


if __name__ == "__main__":
    main()
