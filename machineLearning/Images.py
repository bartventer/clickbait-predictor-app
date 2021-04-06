from random import randint

class Images():
    def __init__(self,result):

        '''
        Required arguments are the result from the Classifer model. Either "Clickbait!" or "Not Clickbait!".
        '''

        self.result = result

        self.bad = ["https://images.unsplash.com/photo-1506702315536-dd8b83e2dcf9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1542573863806-efc9a2dee0c8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1554280955-b112f2babdc0?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1604423792252-b64e3e5437f1?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1052&q=80","https://images.unsplash.com/photo-1594850015290-2cd2d512a508?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=967&q=80","https://images.unsplash.com/photo-1494798109427-e44b68ca5a8b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1511737207395-5b1ff1f86e54?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1503525537183-c84679c9147f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"]
    
        self.good = ["https://images.unsplash.com/photo-1534361960057-19889db9621e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80","https://images.unsplash.com/photo-1468818438311-4bab781ab9b8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1051&q=80","https://images.unsplash.com/photo-1517867134921-7623876aaaa9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80","https://images.unsplash.com/photo-1517867134921-7623876aaaa9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80","https://images.unsplash.com/photo-1517867134921-7623876aaaa9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80","https://images.unsplash.com/photo-1581590289461-df5e0e97dbb9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80","https://images.unsplash.com/photo-1616855484668-439d852aaae0?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=737&q=80","https://images.unsplash.com/photo-1529429617124-95b109e86bb8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80"]
    
    def generateImage(self):

        '''
        Returns a random 'good' or 'bad' picture.
        '''

        if self.result =="Clickbait!":
            randomIndex = randint(0,(len(self.bad) -1))
            return self.bad[randomIndex]
        else:
            randomIndex = randint(0,(len(self.good) -1))
            return self.good[randomIndex]