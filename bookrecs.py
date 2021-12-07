'''
Project: Book Recommendations
Author: Christian Alexander
Created: 04/24/21
Course: CS1410-002
'''
from breezypythongui import EasyFrame

# makes tuple book_list (author,title) from booklist.txt
file1 = open("booklist.txt", "r")
book_list = []
for book in file1:
    author_book = book.strip().split(",")
    book_list.append((author_book[0],author_book[1]))

# makes dictionary ratings_dict (name, rating) from ratings.txt
file2 = open("ratings.txt","r")
name_list = []
count = 1
global ratings_dict
final = ""
ratings_dict = {}
for line in file2:
    if count % 2 != 0:
        name = line.strip().lower()
        name_list.append(name)
    else:
        ratings_num = line.split()
        ratings = []
        for i in ratings_num:
            i = int(i)
            ratings.append(i)
        ratings_dict[name] = ratings
    count += 1

# finds affinity through dot product comparison of readers ratings (list3)
def dotprod():
    length = len(name_list)
    
    r = 0
    while r < length:
        candidate_ratings = ratings_dict.get(name_list[r])
        list1 = READER_RATINGS
        list2 = candidate_ratings
        list3 = (x*y for x,y in zip(list1,list2))
        list3 = (sum(list3))
        r += 1
        products.append(list3)
        if r == length:
            break
    name_rating_list = list(zip(name_list, products))
    name_rating_list.sort(key=lambda x:x[1], reverse=True)
    return name_rating_list

# returns a person’s top 2 friends as a sorted list of strings.
def friends():
    indices = [0]
    friends_dotprod = [dotprod()[index] for index in indices]
    friends_dotprod.sort(reverse=False)
    friend1 = [a_tuple[0] for a_tuple in friends_dotprod]
    indices = [1]
    friends_dotprod = [dotprod()[index] for index in indices]
    friends_dotprod.sort(reverse=False)
    friend2 = [a_tuple[0] for a_tuple in friends_dotprod]
    return friend1, friend2

# returns a list of books recommended for the person from a given friend1 or friend2
def recommend(friend):
    recommend_list = []
    for line in file2:
        if count % 2 != 0:
            name = line.strip().lower()
            name_list.append(name)
        else:
            ratings_num = line.split()
            ratings = []
            for i in ratings_num:
                i = int(i)
                ratings.append(i)
            ratings_dict[name] = ratings
        count += 1
    friend_ratings = ratings_dict.get(friend)
    length = len(book_list)
    
    s = 0
    while s < length:
         if friend_ratings[s] >= 3 and READER_RATINGS[s] == 0:
             recommend_list.append(book_list[s])
         s = s + 1
    return recommend_list

# gui
class bookface(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,
                           background = '#B0E0E6',
                           width = 225,
                           height = 50,
                           resizable = True)
        self.setTitle("bookface")
        self.friend_button = self.addButton(text = 'Friends',
                                            row = 0,
                                            column = 0,
                                            command = self.search)
        self.recommend_button = self.addButton(text = 'Recommend',
                                               row = 0,
                                               column = 1,
                                               command = self.bookrec)
        self.report_button = self.addButton(text = 'Report',
                                            row = 0,
                                            column = 2,
                                            command = self.report)
    def search(self):
        text = self.prompterBox(title = "Friends",
                                promptString = "Enter Reader Name:",
                                fieldWidth = 30)
        READER_NAME = text
        while 1==1:
            global READER_RATINGS
            READER_RATINGS = ratings_dict.get(READER_NAME)
            if READER_RATINGS is None:
                print("No such reader " + READER_NAME)
                break
            else:
                name_list.remove(READER_NAME)
            global products
            products = []
            friend = friends()
            self.messageBox(title = 'Friends of ' + READER_NAME,
                            message = '\n'.join([str(i[0]) for i in friend]))
            name_list.append(READER_NAME)
            break
    def bookrec(self):
        text = self.prompterBox(title = "Recommendations",
                                promptString = "Enter Reader Name:",
                                fieldWidth = 30)
        READER_NAME = text
        while 1==1:
            global READER_RATINGS
            READER_RATINGS = ratings_dict.get(READER_NAME)
            if READER_RATINGS is None:
                print("No such reader " + READER_NAME)
                break
            else:
                name_list.remove(READER_NAME)
            global products
            products = []
            friend = friends()

            friend1 = (str(friend[0]))
            friend1 = (friend1.rstrip("']"))
            friend1 = (friend1.lstrip("['"))
            recommend(friend1)
            friend1_list = recommend(friend1)

            friend2 = (str(friend[1]))
            friend2 = (friend2.rstrip("']"))
            friend2 = (friend2.lstrip("['"))
            recommend(friend2)
            friend2_list = recommend(friend2)
            
            set_1 = set(friend1_list)
            set_2 = set(friend2_list)
            new_items = list(set_2 - set_1)
            combined_list = friend1_list + new_items
            combined_list = (sorted(combined_list, key=lambda x: x[0].split(" ")[-1]))
            recs = ""
            for lines in combined_list:
                recs = recs + (lines[0] + ", " + lines[1] + "\n")
            self.messageBox(title = 'Recommendations for ' + READER_NAME,
                            width = 55,
                            height = 25,
                            message = recs)
            name_list.append(READER_NAME)
            break
    def report(self):
        global name_list
        name_list = sorted(name_list)
        for i in name_list:
            READER_NAME = i
            while 1==1:
                global READER_RATINGS
                READER_RATINGS = ratings_dict.get(READER_NAME)
                name_list.remove(READER_NAME)
                global products
                products = []
                friend = friends()
                
                friend1 = (str(friend[0]))
                friend1 = (friend1.rstrip("']"))
                friend1 = (friend1.lstrip("['"))
                recommend(friend1)
                friend1_list = recommend(friend1)

                friend2 = (str(friend[1]))
                friend2 = (friend2.rstrip("']"))
                friend2 = (friend2.lstrip("['"))
                recommend(friend2)
                friend2_list = recommend(friend2)
                
                set_1 = set(friend1_list)
                set_2 = set(friend2_list)
                new_items = list(set_2 - set_1)
                combined_list = friend1_list + new_items
                combined_list = (sorted(combined_list, key=lambda x: x[0].split(" ")[-1]))
                recs = ""
                for lines in combined_list:
                    recs = recs + (lines[0] + ", " + lines[1] + "\n\t")
                recs =  "Recommendations for " + READER_NAME + " from " + (' and '.join([str(i[0]) for i in friend])) + ":\n\t" + recs + "\n"
                global final
                final = final + recs
                name_list.insert(0, READER_NAME)
                break
        self.messageBox(title = 'Report',
                        width = 65,
                        height = 25,
                        message = final)

# gui main loop
def main():
    bookface().mainloop()
if __name__ == '__main__':
    main()
