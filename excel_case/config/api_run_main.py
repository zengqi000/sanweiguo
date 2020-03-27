import requests
import json
class ApiRunMain(object):
    def post_main(self,url,data,header=None):
        res = None
        if header!=None:
            res = requests.post(url = url,data = data,headers = header).json()
        else:
            res = requests.post(url = url,data = data).json()
        return res
    def get_main(self,url,header=None):
        res = None
        if header!=None:
            res = requests.get(url = url,headers = header).json()
        else:
            res = requests.get(url = url).json()
        return res
    def delete_main(self,url,header=None):
        res = None
        if header != None:
            res = requests.get(url = url, headers = header).json()
        else:
            res = requests.get(url = url).json()
        return res
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        elif method == 'get':
            res = self.get_main(url,header)
        else:
            res = self.delete_main(url,header)
        return res
if __name__=='__main__':
    method = 'get'
    url = 'https://www.yeechoo.com/api/relatedProduct/1?page=0&limit=0'
    res = ApiRunMain().run_main(method=method,url=url)
    #res = ApiRunMain().get_main(url=url)
    print (res)


