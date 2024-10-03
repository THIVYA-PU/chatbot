import wikipediaapi
wiki_obj = wikipediaapi.Wikipedia('English')
def wiki_summary(query):
    try:
        page = wiki_obj.page(query)
        if page.exists():
            return page.summary[:500]
        else:
            return "Sorry Can't Find the wikipedia Page"
    except Exception as e:
        return f"An error Occured:{str(e)}"

if __name__=="__main__":
    while(True):
        inp=input("Enter the Title:")
        if inp=="exit" or "quit":
            break
        else:
            res = wiki_summary(inp)
            print(f"{res}")
            