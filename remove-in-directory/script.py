import os
import time

import xlrd
import xlwt


class SpreadsheetError(Exception):
    """ Raises spreadsheet error if files not found or too many in directory """
    def __init__(self, files_number):
        self.files_number = files_number
        self.message_zero_files = 'No xls files found'
        self.message_more_than_one = 'More than 1 xls file found: '
        
        if self.files_number == 0:
            super().__init__(self.message_zero_files)
        else:
            super().__init__(
                self.message_more_than_one +
                str(self.files_number) +
                ' files in directory')


def spreadsheet_finder():
    """ Returns spreadsheet filename in directory """
    spread_sheet = ([ file for file in os.listdir(os.getcwd()) if file.endswith('xls') ])

    if len(spread_sheet) == 1:
        return ''.join(spread_sheet)
    else:
        raise SpreadsheetError(len(spread_sheet))


def spreadsheet_values_loader():
    """
    Loads spreadsheet values from first column into a list.
    Each value in list is string
    """
    worksheet = xlrd.open_workbook(spreadsheet_finder()).sheet_by_index(0)
    items = []

    for row_number in range(worksheet.nrows):
        items.append(worksheet.cell_value(row_number, 0))

    return items


def old_files_remover():
    """ Removes files in directory which are not in excel spreadsheet """
    files_in_directory = [ files for files in os.listdir(os.getcwd()) ]
    indexes_in_spreadsheet = spreadsheet_values_loader()
    files_deleted_counter = 0
    files_deleted = []

    for file in files_in_directory:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
            if '-' in file:
                if file[0:8] not in indexes_in_spreadsheet:
                    os.remove(file[0:8])
                    files_deleted_counter += 1
                    files_deleted.append(file)
            else:
                if file[0:5] not in indexes_in_spreadsheet:
                    os.remove(file)
                    files_deleted_counter += 1
                    files_deleted.append(file[0:5])

    save_new_spreadsheet('usunięte-pliki.xls', list(dict.fromkeys(files_deleted)))
    
    return files_deleted_counter


def file_extension_and_letter_remover():
    """ removes files extension and letter in name"""
    files_in_directory = [ files for files in os.listdir(os.getcwd()) ]
    files_without_extension = []
    files_without_letters = []

    for file in files_in_directory:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
            files_without_extension.append(file[0:-4])

    for index in files_without_extension:
        if '-' in index:
            files_without_letters.append(index[0:8])
        else:
            files_without_letters.append(index[0:5])

    return files_without_letters


def files_checker():
    """ 
    Checks if every index in xls has photo in directory.
    If not, index is added to list to generate new xls file later.
    """
    files_in_directory = file_extension_and_letter_remover() # files in directory without letters and extensions
    indexes_in_spreadsheet = spreadsheet_values_loader()
    files_not_in_directory = []

    for index in indexes_in_spreadsheet:
        if index not in files_in_directory:
            files_not_in_directory.append(index)

    save_new_spreadsheet('brak-w-folderze.xls', list(dict.fromkeys(files_not_in_directory)))


def save_new_spreadsheet(filename, elements):
    """
    Saves new spreadsheet with one column with walues
    """
    new_file = xlwt.Workbook()
    sheet = new_file.add_sheet("Arkusz 1")
    sheet.write(0, 0, "INDEX")
    counter = 1

    for element in elements:
        sheet.write(counter, 0, element)
        counter += 1

    new_file.save(filename)


def main():
    old_files_remover()
    time.sleep(2)
    files_checker()
    print('Zapisano plik brak-w-folderze.xls')
    print('Zapisano plik usunięte-pliki.xls z listą usuniętych plików')


if __name__ == '__main__':
    main()