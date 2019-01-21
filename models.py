from datetime import datetime
comments = []

class Comment():
    """ Model class for comment """
        
    def save(self, data):
        data['id'] = generate_id()
        comments.append(data)

def generate_id():
    if len(comments) == 0:
        return 1
    else:
        return len(comments)