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
            print("enter some notes")
    def list(self):
        if self.notes_list==[]:
            print("There are no notes in the list")
        else:
            
            idx=0
            for i in self.notes_list:
                
                print("Note ID: [",idx,"]")
                print("[",self.notes_list[idx],"]\n")
                idx+=1
            print("By Author[", self.author,"]\n")
                
        
    def get(self,note_id):
        if not isinstance( note_id, int ):
            print("<",note_id,">should be a digit")
        elif note_id>=len(self.notes_list) or note_id < 0:
            print ("Index out of range")
        else:
            idx=0
            for i in self.notes_list:
                if note_id==idx:
                    return self.notes_list[idx]
                idx+=1
                    
        
        
    def search(self,search_text):
        idx=0
        not_available=True
        if not search_text.strip():
            print("enter something to search")
        else:
            print("Showing results for search '[<", search_text,">]'\n")
            for i in self.notes_list:
                if search_text in i:
                    not_available=False
                    print("Note ID:", idx)
                    print("[",self.notes_list[idx],"]\n")
                    print("By Author[",self.author,"]\n")
                idx+=1
            if not_available:
                
                print("OOps sorry, no results found!!")
                    
        
    def edit(self,note_id,new_content):
        if not isinstance( note_id, int ):
            print("<",note_id,">should be a digit")
        elif note_id>=len(self.notes_list) or note_id < 0:
            print("Index out of range")
        elif not new_content.strip():
            print("Enter something to edit")
        
        else:
            self.notes_list[note_id]=new_content
            
        

        
