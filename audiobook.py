import pyttsx3
import PyPDF2
import sys

class AudioBook:
    def __inti__(self):
        pass

    def read_pdf(self, path, start_page, end_page):
        with open(path, "rb") as book:
            pdfReader = PyPDF2.PdfFileReader(book)
            nop = pdfReader.numPages
            if end_page > nop:
                end_page = nop
            for pno in range(start_page, end_page+1):
                page    = pdfReader.getPage(pno)
                text    = page.extractText()
                speaker = pyttsx3.init()
                speaker.say(text)
                speaker.runAndWait()

if __name__ == "__main__":
    b = AudioBook()
    start_page = 0
    end_page   = 0
    if len(sys.argv) == 3:
        start_page = int(sys.argv[2])
    if len(sys.argv) == 4:
        start_page = int(sys.argv[2])
        end_page   = int(sys.argv[3])

    b.read_pdf(sys.argv[1], start_page, end_page)
