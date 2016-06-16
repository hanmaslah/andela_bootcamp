class NotesApplication():
    """
This class creates an application for holding notes and categorises
them according to the author and gives them an index. You can also
search for a word in the notes list.
    """
   
    def __init__(self,author):
        self.author=author
        self.notes_list=[]
        
    def create(self, note_content):
        if note_content.strip():
            
            self.notes_list.append(note_content)
        else:
            return "enter some notes"
    def list(self):
        if self.notes_list==[]:
            return "There are no notes in the list"
        else:
                  
            for n,i in enumerate (self.notes_list):
                
                print("Note ID: ",n)
                print(i,"\n")
                
            print ('By Author: ', self.author)           
                
        
    def get(self,note_id):
        if not isinstance( note_id, int ):
            print("<",note_id,">should be a digit")
        elif note_id>=len(self.notes_list) or note_id < 0:
            return "Index out of range"
        else:
            return self.notes_list[note_id]   
        
        
    def search(self,search_text):
        
        if not search_text.strip():
            return "enter something to search"
        else:
            print("Showing results for search '[<", search_text,">]'\n")
            for n,i in enumerate (self.notes_list):
                if search_text == i:
                    print("Note ID:", n)
                    print(i,"\n")
                    print("By Author: ",self.author)
                else:
                    
                    return "OOps sorry, no results found!!"
                    
        
    def edit(self,note_id,new_content):
        if not isinstance( note_id, int ):
            print("<",note_id,">should be a digit")
        elif note_id>=len(self.notes_list) or note_id < 0:
            print("Index out of range")
        elif not new_content.strip():
            print("Enter something to edit")
        
        else:
            self.notes_list[note_id]=new_content
            
        

        
