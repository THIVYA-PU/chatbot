import wikipediaapi
wiki_obj = wikipediaapi.Wikipedia('English')
def wiki_summary(query):
    page = wiki_obj.page(query)
    if page.exists():
        return page.summary[:500]
    else:
        return "Sorry"

if __name__=="__main__":
    while(True):
        inp=input("Enter:")
        if inp=="exit":
            break
        else:
            res = wiki_summary(inp)
            print(f"{res}")
            