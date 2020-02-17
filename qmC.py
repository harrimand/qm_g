
class Qm():
    def __init__(self, data, dc=[]):
        self.data = data
        self.dc = dc
        if(isinstance(data, (list))):
            self.tt = data
            self.usop = self.tt2usop(self.data)
            self.vars = self.getVars(self.usop)
        elif(isinstance(data, (str))):
            if '+' not in data:
                self.tt = self.impStr2impList(data)
                self.usop = self.tt2usop(self.tt)
                self.vars = self.getVars(self.usop)
            else:
                self.vars = self.getVars(data)
                self.tt = self.sop2imps(data, self.vars)
                self.usop = self.tt2usop(self.tt)
                # self.sop2tt(data)

#    def tt(self, data):
#        print("It was a list")

    def sop2tt(self, data):
        print("It was a string")


    def impStr2impList(self, impStr):
        '''Parameter:  A string containing decimal integers seperated by commas or
        spaces.  Range operators (..) are interpreted as follows:
        ..3 [0, 1, 2, 3]  #include all integers from 0 to 3
        6..10 [6, 7, 8, 9, 10]  all integers from 6 to 10 inclusive.
        5..  [5, 6, 7]  include all 3 bit integers starting at 5.  5 is a 3 bit int.
        12.. [12, 13, 14, 15]  include all 4 bit integers starting at 12.
        Return a sorted unique list of all integers in string including ranges.'''
        imptmp = impStr.replace(", ", " ")
        implist = ' '.join(imptmp.split()).split()
        decimps = []
        for i in implist:
            if ".." not in i:
                if i not in decimps:
                   decimps.append(int(i))
            elif i.find("..")+2 == len(i):
                seqEnd = pow(2, int(i[:i.find("..")]).bit_length())
                for n in range(int(i[:i.find("..")]),seqEnd):
                    if n not in decimps:
                        decimps.append(n)
            elif i.find("..") == 0:
                for n in range(0, int(i[i.find("..")+2:])+1):
                   if n not in decimps:
                      decimps.append(n)
            else:
                for n in range(int(i[:i.find("..")]),int(i[i.find("..")+2:])+1):
                   if n not in decimps:
                      decimps.append(n)
        decimps.sort()
        return decimps

#------------------------------------------------------------

    def getVars(self, sop):
        '''Takes a string containing single character variables and makes a sorted
        list of the unique variables (Upper or Lower Case) found in the string.
        Non alpha characters will not be included in the list
        Ex: "AC!D + !AB!D+A!B" returns ['A', 'B', 'C', 'D']'''
        vars = []
        for c in sop:
            if (ord(c) > 64 and ord(c) < 91 or ord(c) > 97 and ord(c) < 123)\
            and c not in vars:
                vars.append(c)
        vars.sort()
        return vars

    def setVars(self, V)
        vars = 



#------------------------------------------------------------

    def sop2imps(self, sop, vars):
        '''Parameters: sop: String containing a SOP (sum of products)
                       vars: list containing variables
        vars may include variables not in sop string
        Returns sorted list of all implicants covered by the sop'''
        soplist = ' _ '.join(sop.split('+')).replace(' ', '').split('_')
    #    print(sop, "\n\n ", soplist, "\n\n") #Comment

        covers = []
        for T in soplist:
            covers.append(self.v2bterms(T, vars))
    #    print("\n\t", covers, "\n") #Comment

        coverImps = []
        for term in covers:
            for I in self.decImps(term):
                if I not in coverImps:
                    coverImps.append(I)
        coverImps.sort()
        return coverImps

#------------------------------------------------------------

    def v2bterms(self, instr, vars):
        """ parameters:
        string  "A!B!D" representing a product in a sum of products
        boolean expression.
        list ['A', 'B', 'C', 'D'] containing all variables in the sum
        of products expression.
        returns a string "10X0" with missing variables in string replaced
        with a "X".  """
        inlist = []
        c = 0
        while c < len(instr):
            if instr[c] == '!':
               inlist.append(instr[c] + instr[c+1])
               c += 2
            else:
                inlist.append(instr[c])
                c += 1
        #print("\n\n\tinstr: {}\n\n\tinlist: {}".format(instr, inlist))
        #print("\n\n\t vars: {}".format(vars))

        resb = ''
        for c in vars:
            if c not in inlist and ('!' + c) not in inlist:
                resb += 'X'
            elif c in inlist:
                resb += '1'
            else:
                resb += '0'
        #print("Result: {}".format(resb))
        return resb

#------------------------------------------------------------

    def decImps(self, term):
        """Parameter: String containing characters 1, 0 and X.
        Return list of all values where X's are replaced with all
        possible combinations of 1s and 0s"""
        numX = term.count("X")
        decList = []
        for b in range(2**numX):
            bbits = ("{:0>{}}".format(bin(b)[2:], numX))
            imp = term
            for bit in bbits:
                imp = imp.replace("X", bit, 1)
            decList.append(int(imp, 2))
        return(decList)

#------------------------------------------------------------

    def binToVars(self, essStr):
        """Take a string containing 0s, 1s and Xs and return a string starting
        with A or !A if string starts with a 1 or 0 and exclude letters represented
        by X. Example:  X1X01 returns B !D E"""
        term = ""
        ch = 0
        for c in essStr:
            if c == '0':
               term += '!' + chr(ord('A') + ch) + ''
            elif c == '1':
                term += chr(ord('A') + ch) + ''
            ch += 1
        return term

#------------------------------------------------------------

    def tt2usop(self, data):
        '''Parameter: List containing integers that produce True
        on the output of the Sum of Products (SOP).
        Returns an Unsimplified SOP that covers all integers in List.'''
        termList = []
        bitsize = max(data).bit_length()
        for d in data:
            termList.append(self.binToVars(bin(d)[2:].zfill(bitsize)))
        SOPstring = ""
        for i, t in enumerate(termList):
            SOPstring += t
            if i < (len(termList) - 1):
                SOPstring += " + "
        return SOPstring

#------------------------------------------------------------





#------------------------------------------------------------





#------------------------------------------------------------


print('\n\n')
myQM1 = Qm([1, 2, 3, 4])
print("myQM1 = Qm([1, 2, 3, 4])")
print(myQM1.vars)
print(myQM1.tt)
print(myQM1.usop)
print('\n\n')

myQM2 = Qm("1 2..5 7 9..13")
print("myQM2 = Qm('1 2..5 7 9..13')")
print(myQM2.vars)
print(myQM2.tt)
print(myQM2.usop)
print('\n\n')

myQM3 = Qm('A!B + C!D + BC')
print("myQM3 = Qm('A!B + C!D + BC')")
print(myQM3.vars)
print(myQM3.tt)
print(myQM3.usop)
print('\n\n')

# print(Qm.sop2imps('A!C', ['A', 'B', 'C', 'D']))


# Vset = [chr(n) for n in range(65, ord(max(list(VS)+Vm))+1)]
# Vset = [chr(n) for n in range(65, ord(max(list(VS)+Vm))+1)]




