import sys
import subprocess
import re
import os
import time

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger


def docx_pdf_converter(folder, source, timeout=None):
    """Converts docx to pdf using headless module of Libre Offce (so works even without MS Office) by printing commnd into Terminal/CMD depending on the used OS"""
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)


def libreoffice_exec():
    """Returns executable libre office file (soffice) directory to use headless functions"""
    MAC_OS = 'darwin'
    WINDOWS = 'win32'
    LINUX = 'linux'

    if sys.platform == MAC_OS:
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    elif sys.platform == WINDOWS:
        return 'C:\Program Files\LibreOffice\program\soffice.exe'
    elif sys.platform == LINUX:
        return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output


def pdf_merger(pdf1, pdf2):
    pdfs = [pdf1, pdf2]
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write('połączony-plik.pdf')
    merger.close()


def get_second_file():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".pdf") and file != 'start.pdf':
            return file


def get_doc_name():
     for file in os.listdir(os.getcwd()):
         if file.endswith(".doc") or file.endswith(".docx"):
             return file


def remove_file(file):
    """Remove not anymore needed converted PDF file"""
    if file.endswith(".doc"):
        pdf_name = file.replace(".doc", ".pdf")
    elif file.endswith(".docx"):
        pdf_name = file.replace(".docx", ".pdf")

    os.remove(pdf_name)


if __name__ == '__main__':
    docx_pdf_converter(os.getcwd(), get_doc_name())
    pdf_merger('start.pdf', get_second_file())
    remove_file(get_doc_name())