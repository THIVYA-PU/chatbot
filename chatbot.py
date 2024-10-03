import wikipediaapi
wiki_obj = wikipediaapi.Wikipedia('English')
def wiki_summary(query):
    try:
        page = wiki_obj.page(query)
        if page.exists():
            res_summary = page.summary[:600]
            words = len(res_summary.split())
            link = page.fullurl
            print(f"This summary contains {words} words\n")
            return f"{res_summary}\n\nIf you want You can read more at: {link}"
        else:
            return "Sorry Can't Find the wikipedia Page"
    except Exception as e:
        return f"An error Occured:{str(e)}"

if __name__=="__main__":
    while(True):
        try:
            inp=input("Enter the Title:")
            if inp=="exit" or inp == "quit":
                break
            else:
                res = wiki_summary(inp)
                print(f"{res}")
        except KeyboardInterrupt:
            print("Exiting")
            break
        except Exception as e:
            print(f"Error Occured {str(e)}")
            break
            