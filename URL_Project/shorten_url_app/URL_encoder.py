import short_url

class URL_encoder():
    def __init__(self, id, url_list):
        self.id = id+1          #take into account that some URLs are in database, initialize id accordingly when 'runserver'
        self.url2id = {}        #use dictionary to save original URLs
        self.url_list = url_list

    def encode_url(self, user_url, base_domain):
        if user_url in self.url2id:         #if already in dict
            id = self.url2id[user_url]
            shorten_url = short_url.encode_url(id)
        else:
            self.url2id[user_url] = self.id
            shorten_url = short_url.encode_url(self.id)
            self.id += 1                    #avoid duplicate ids

        return "{}/{}".format(
            base_domain,
            shorten_url
        )