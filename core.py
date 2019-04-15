from Error import *
from copy import  *

class Word:
    __length = 0
    __begin = ''
    __end = ''
    __word = ''
    used = False

    def __init__(self, word_input):
        self.__word = word_input
        self.__length = len(word_input)
        self.__begin = word_input[0]
        self.__end = word_input[-1]
        self.used = False

    def begin(self):
        return self.__begin

    def end(self):
        return self.__end

    def word(self):
        return self.__word

    def length(self):
        return self.__length

    def set_word(self, input_word):
        self.__word = input_word
        self.__length = len(input_word)
        self.__begin = input_word[0]
        self.__end = input_word[-1]


class Wordlist:

    def __init__(self):
        self.frontlist = [[] for i in range(26)]
        self.taillist = [[] for i in range(26)]
    
    # Add the input word into the wordlist, the rawlist is supposed to be a string list.
    def add(self, rawlist):
        for word in rawlist:
            word_elem = Word(word)
            self.frontlist[ord(word_elem.begin())- ord('a')].append(word_elem)
            self.taillist[ord(word_elem.end())- ord('a')].append(word_elem)
        return


class ChainNode:
    def __init__(self, _word = None, _input_word = ''):
        if _word == None:
            self.member = Word(_input_word)
        else:
            self.member = _word
        self.next_search_char = ''


class Chain:
    def __init__(self):
        self.charcnt = 0
        self.wordcnt = 0
        self.searchchain = [ChainNode('\0')]


class Core:
    def __init__(self, input_words=60, searched_num=1200):
        self.__max_inputwords = input_words
        self.__max_searched_num = searched_num
        self.__searched_chain_num = 0
        self.__tmpchain = Chain()
        self.__searchchain = [] #List of Chain
        self.__wlist = Wordlist()

    def __clear(self):
        self.__searchchain = [Chain()]
        self.__searched_chain_num = 0
        self.__tmpchain.charcnt = 0
        self.__tmpchain.wordcnt = 0
        self.__tmpchain.searchchain = [ChainNode('\0')]
        self.__wlist = Wordlist()

    def __checkwords(self, words):
        for i, word in enumerate(words):
            if len(word) == 0:
                return 1
            for j, word_other in enumerate(words):
                if i != j and word == word_other:
                    return 2
            for char in word:
                if not char.isalpha():
                    return 3
        return 0

    '''
    mode refers to head or tail.(True for tail and False for head)
    chain is a single search chain.(Type: Chain)
    '''
    def result_transfer_one(self, chain, mode):
        chain: Chain
        result_chain = Chain()
        if mode:
            for i in range(len(chain.searchchain) - 1, 0, -1):
                result_chain.searchchain.append(chain.searchchain[i])
        else:
            for i in range(1, len(chain.searchchain)):
                result_chain.searchchain.append(chain.searchchain[i])

        result_chain.wordcnt = chain.wordcnt
        result_chain.charcnt = chain.charcnt
        return result_chain

    def get_result(self):
        return self.__searchchain

    """
        This function completes the search task on wlist in the core object 
        and returns 0 if the search completes successfully.
        
        Parameters:
        "head" is the assigned head character of the search chain and is set to empty as default.
        "tail" is the assigned tail character of the search chain and is set to empty as default.
        "len" is the assigned length of the search chain and is set to 0 as default.
        "w_or_c" is the assigned search type and is set to True for default referring to '-w'.
        
    """
    def __search(self, head = '', tail = '', len = 0, w_or_c = True):
        # Divide into two types of search.
        if head != '':  # -h selected, search using frontlist.
            list_index = self.__tmpchain.searchchain[self.__tmpchain.wordcnt].next_search_char

            curword: Word
            for i, curword in enumerate(self.__wlist.frontlist[list_index]):
                if not curword.used:
                    curword.used = True
                    self.__tmpchain.wordcnt += 1
                    if self.__tmpchain.wordcnt >= self.__max_searched_num:
                        raise runtimeError(msg="The search has reached its upper bound!",
                                           detail="There are too many words from the input!")

                    # Set the value for the current level
                    new_chain_node = ChainNode(curword)
                    new_chain_node.next_search_char = ord(curword.end()) - ord('a')
                    self.__tmpchain.searchchain.append(new_chain_node)
                    self.__tmpchain.charcnt += curword.length()

                    # Process search result and copy the tmpchain
                    if self.__tmpchain.wordcnt > 1 \
                            and (tail == '' or tail == curword.end())\
                            and (len == 0 or len == self.__tmpchain.wordcnt):
                        # Store the tmpchain into searchchain in core only if the conditions above are satisfied.
                        if w_or_c:
                            # searching for longest word chain
                            if self.__tmpchain.wordcnt > self.__searchchain[0].wordcnt:
                                # Found a longer chain
                                self.__searched_chain_num = 1
                                self.__searchchain.clear()
                                self.__searchchain.append(deepcopy(self.__tmpchain))

                            elif self.__tmpchain.wordcnt == self.__searchchain[0].wordcnt:
                                # Found a chain which has the same length as the current longest chain
                                if self.__searched_chain_num + 1 > self.__max_searched_num:
                                    raise runtimeError(msg="The search has reached its upper bound!",
                                                       detail="There are too many solitaire combinations!")
                                else:
                                    self.__searched_chain_num += 1
                                    self.__searchchain.append(deepcopy(self.__tmpchain))

                        else:
                            # searching for longest character chain
                            if self.__tmpchain.charcnt > self.__searchchain[0].charcnt:
                                # Found a longer chain
                                self.__searched_chain_num = 1
                                self.__searchchain.clear()
                                self.__searchchain.append(deepcopy(self.__tmpchain))

                            elif self.__tmpchain.charcnt == self.__searchchain[0].charcnt:
                                # Found a chain which has the same length as the current longest chain
                                if self.__searched_chain_num + 1 > self.__max_searched_num:
                                    raise runtimeError(msg="The search has reached its upper bound!",
                                                       detail="There are too many solitaire combinations!")
                                else:
                                    self.__searched_chain_num += 1
                                    self.__searchchain.append(deepcopy(self.__tmpchain))

                    # Expand the level
                    if len == 0 or self.__tmpchain.wordcnt < len:
                        self.__search(head, tail, len, w_or_c)

                    # Backtrace and restore the variable
                    self.__tmpchain.charcnt -= curword.length()
                    self.__tmpchain.wordcnt -= 1
                    curword.used = False
                    self.__tmpchain.searchchain.pop()

        else:           # -h not selected, search using tailist.
            list_index = self.__tmpchain.searchchain[self.__tmpchain.wordcnt].next_search_char

            curword: Word
            for i, curword in enumerate(self.__wlist.taillist[list_index]):
                if not curword.used:
                    curword.used = True
                    self.__tmpchain.wordcnt += 1
                    if self.__tmpchain.wordcnt >= self.__max_searched_num:
                        raise runtimeError(msg="The search has reached its upper bound!",
                                           detail="There are too many words from the input!")

                    # Set the value for the current level
                    new_chain_node = ChainNode(curword)
                    new_chain_node.next_search_char = ord(curword.begin()) - ord('a')
                    self.__tmpchain.searchchain.append(new_chain_node)
                    self.__tmpchain.charcnt += curword.length()

                    # Process search result and copy the tmpchain

                    if self.__tmpchain.wordcnt > 1 \
                            and (len == 0 or len == self.__tmpchain.wordcnt):
                        # Store the tmpchain into searchchain in core only if the conditions above are satisfied.
                        if w_or_c:
                            # searching for longest word chain
                            if self.__tmpchain.wordcnt > self.__searchchain[0].wordcnt:
                                # Found a longer chain
                                self.__searched_chain_num = 1
                                self.__searchchain.clear()
                                self.__searchchain.append(deepcopy(self.__tmpchain))

                            elif self.__tmpchain.wordcnt == self.__searchchain[0].wordcnt:
                                # Found a chain which has the same length as the current longest chain
                                if self.__searched_chain_num + 1 > self.__max_searched_num:
                                    raise runtimeError(msg="The search has reached its upper bound!",
                                                       detail="There are too many solitaire combinations!")
                                else:
                                    self.__searched_chain_num += 1
                                    self.__searchchain.append(deepcopy(self.__tmpchain))

                        else:
                            # searching for longest character chain
                            if self.__tmpchain.charcnt > self.__searchchain[0].charcnt:
                                # Found a longer chain
                                self.__searched_chain_num = 1
                                self.__searchchain.clear()
                                self.__searchchain.append(deepcopy(self.__tmpchain))

                            elif self.__tmpchain.charcnt == self.__searchchain[0].charcnt:
                                # Found a chain which has the same length as the current longest chain
                                if self.__searched_chain_num + 1 > self.__max_searched_num:
                                    raise runtimeError(msg="The search has reached its upper bound!",
                                                       detail="There are too many solitaire combinations!")
                                else:
                                    self.__searched_chain_num += 1
                                    self.__searchchain.append(deepcopy(self.__tmpchain))

                    # Expand the level
                    if len == 0 or self.__tmpchain.wordcnt < len:
                        self.__search(head, tail, len, w_or_c)

                    # Backtrace and restore the variable
                    self.__tmpchain.charcnt -= curword.length()
                    self.__tmpchain.wordcnt -= 1
                    curword.used = False
                    self.__tmpchain.searchchain.pop()

        return 0

    """
        Parameters:
        words: a list of string that contains all the input words.(Duplication allowed)
        head: the head character for the searched chain.
        tail: the tail character for the searched chain.
    """
    def chain_word(self, words, head, tail):
        results = []
        head = head.lower()
        tail = tail.lower()
        if len(words) == 0:
            raise inputError("The input wordchain is empty!")
        elif len(words) > self.__max_inputwords:
            raise inputError("The input word stream is too long!")
        elif head != '' and (not head.isalpha()):
            raise syntaxError("Illegal head letter input for the solitaire!")
        elif tail != '' and (not tail.isalpha()):
            raise syntaxError("Illegal tail letter input for the solitaire!")
        
        errcode = self.__checkwords(words)
        if errcode == 1:
            raise inputError("Empty element in the word stream detected!")
        elif errcode == 2:
            raise inputError("Duplicate element in the word stream detected!")
        elif errcode == 3:
            raise inputError("Illegal character detected in the word stream!")

        self.__clear()
        self.__wlist.add(words)

        if head != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(head) - ord('a')
            self.__search(head, tail, 0, True)
        elif tail != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(tail)- ord('a')
            self.__search(head, tail, 0, True)

        else:
            for i in range(26):
                self.__tmpchain.searchchain[0].next_search_char = i
                self.__search(head, tail ,0, True)

        # For console printing
        # self.print_for_num()
        # self.print()
        return deepcopy(self.__searchchain)

    def chain_char(self, words, head, tail):
        results = []
        head = head.lower()
        tail = tail.lower()
        if len(words) == 0:
            raise inputError("The input wordchain is empty!")
        elif len(words) > self.__max_inputwords:
            raise inputError("The input word stream is too long!")
        elif head != '' and (not head.isalpha()):
            raise syntaxError("Illegal head letter input for the solitaire!")
        elif tail != '' and (not tail.isalpha()):
            raise syntaxError("Illegal tail letter input for the solitaire!")

        errcode = self.__checkwords(words)
        if errcode == 1:
            raise inputError("Empty element in the word stream detected!")
        elif errcode == 2:
            raise inputError("Duplicate element in the word stream detected!")
        elif errcode == 3:
            raise inputError("Illegal character detected in the word stream!")

        self.__clear()
        self.__wlist.add(words)

        if head != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(head) - ord('a')
            self.__search(head, tail, 0, False)
        elif tail != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(tail) - ord('a')
            self.__search(head, tail, 0, False)

        else:
            for i in range(26):
                self.__tmpchain.searchchain[0].next_search_char = i
                self.__search(head, tail, 0, False)

        # For console printing
        # self.print_for_num()
        # self.print()
        return deepcopy(self.__searchchain)

    def chain_num(self, words, head, tail, length, w_or_c):
        results = []
        head = head.lower()
        tail = tail.lower()
        if len(words) == 0:
            raise inputError("The input wordchain is empty!")
        elif len(words) > self.__max_inputwords:
            raise inputError("The input word stream is too long!")
        elif head != '' and (not head.isalpha()):
            raise syntaxError("Illegal head letter input for the solitaire!")
        elif tail != '' and (not tail.isalpha()):
            raise syntaxError("Illegal tail letter input for the solitaire!")
        elif length <= 1:
            raise inputError("The assigned length for the solitaire must be above 1!")

        errcode = self.__checkwords(words)
        if errcode == 1:
            raise inputError("Empty element in the word stream detected!")
        elif errcode == 2:
            raise inputError("Duplicate element in the word stream detected!")
        elif errcode == 3:
            raise inputError("Illegal character detected in the word stream!")

        self.__clear()
        self.__wlist.add(words)

        if head != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(head) - ord('a')
            self.__search(head, tail, length, w_or_c)
        elif tail != '':
            self.__tmpchain.searchchain[0].next_search_char = ord(tail) - ord('a')
            self.__search(head, tail, length, w_or_c)

        else:
            for i in range(26):
                self.__tmpchain.searchchain[0].next_search_char = i
                self.__search(head, tail, length, w_or_c)

        # For console printing
        # self.print_for_num()
        # self.print()
        return deepcopy(self.__searchchain)

    def print_for_num(self):
        search_chain: Chain
        self.__searchchain:list[Chain]
        if len(self.__searchchain) == 1 \
                and self.__searchchain[0].searchchain[0].member == '\0'\
                and self.__searchchain[0].wordcnt == 0:
            print("There isn't a solitaire that matches the input requirements.")
        else:
            print("Total solitaire number: %d" % len(self.__searchchain))
            for i, search_chain in enumerate(self.__searchchain):
                print("----------------------------------------------")
                print("No: %d" % (i + 1))
                if search_chain.wordcnt >= 1:
                    print("The length of this solitaire is %d." % search_chain.wordcnt)
                else:
                    print("The solitaire is empty.")

                if search_chain.charcnt == 1:
                    print("There is only one character in the solitaire.")
                else:
                    print("There are %d characters in the solitaire.\n" % search_chain.charcnt)

                for node in search_chain.searchchain[1:]:
                    print(node.member.word())

                print()

    def print(self):
        search_chain: Chain
        self.__searchchain: list[Chain]
        if len(self.__searchchain) == 1 \
                and self.__searchchain[0].searchchain[0].member == '\0' \
                and self.__searchchain[0].wordcnt == 0:
            print("There isn't a solitaire that matches the input requirements.")
        else:
            printchain: Chain
            printchain = self.__searchchain[0]
            print("----------------------------------------------")
            if printchain.wordcnt >= 1:
                print("The length of this solitaire is %d." % printchain.wordcnt)
            else:
                print("The solitaire is empty.")

            if printchain.charcnt == 1:
                print("There is only one character in the solitaire.")
            else:
                print("There are %d characters in the solitaire.\n" % printchain.charcnt)

            node: Word
            for node in printchain.searchchain[1:]:
                print(node.member.word())

            print()


if __name__ == "__main__":
    word1 = ['thed', 'dota', 'dadq', 'kingase', 'astralis', 'solitaire', 'equality', 'yes', 'yellow', 'youngs', 'yon', 'ngs', 'you', 'ugs']
    word2 = [['thed', 'dota', 'dadq', 'kingase', 'astralis'], ['solitaire', 'equality', 'yes', 'yellow']]
    core = Core()
    # core.chain_char(word1, '', '')
    # print()
    # core.chain_word(word1, '', '')
    # core.chain_num(words=word1, head='', tail='', length=7, w_or_c=False)