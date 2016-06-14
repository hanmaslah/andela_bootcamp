class NotesApplication():
   
    def __init__(self,author, notes_list=[]):
        self.author=author
        self.notes_list=notes_list
        
    def create(self, note_content):
        self.notes_list.append(note_content)
    def list(self):
        if self.notes_list==[]:
            print("There are no notes in the list")
        else:
            
            idx=0
            for i in self.notes_list:
                
                print("Note ID:", idx)
                print("[",self.notes_list[idx],"]\n")
                print("By Author", self.author,"\n")
                idx+=1
        
    def get(self,note_id):
        if note_id>=len(self.notes_list) or note_id < 0:
            return "Index out of range"
        else:
            idx=0
            for i in self.notes_list:
                if note_id==idx:
                    return self.notes_list[idx]
                idx+=1
                    
        
        
    def search(self,search_text):
        idx=0
        not_available=True
        print("Showing results for search '[<", search_text,">]'\n")
        for i in self.notes_list:
            if search_text in i:
                not_available=False
                print("Note ID:", idx)
                print("[",self.notes_list[idx],"]\n")
                print("By Author", self.author,"\n")
            idx+=1
        if not_available:
            
            print("OOps sorry, no results found!!")
                    
        
    def edit(self,note_id,new_content):
        if note_id>=len(self.notes_list) or note_id < 0:
            return "Index out of range"
        else:
            self.notes_list[note_id]=new_content
            
        

        
