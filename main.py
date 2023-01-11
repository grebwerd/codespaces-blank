import os
import openai
import webbrowser

prompt = "A mad unicorn drinking coffee."
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    openai.api_key = ""

    response_summary = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create an analogy for this phrase: You come most carefully upon your hour.",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(f"response: {response_summary}")

    summary_tokens = response_summary["choices"][0]["text"].split(".")


    for summary_token in summary_tokens:
        print(f"summary_token:  {summary_token}")
        if summary_token:
            response = openai.Image.create(
                prompt=summary_token,
                n=1,
                size="1024x1024",
            )

            response_url = response["data"][0]["url"]
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(response_url)
