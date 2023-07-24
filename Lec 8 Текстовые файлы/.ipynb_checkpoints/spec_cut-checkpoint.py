import csv
import fnmatch #модуль для сравнения с шаблоном

#def write_stroke(filename, line, writing_type):
#       file = open(filename, writing_type, newline ='') 
#        with file:     
#            write = csv.writer(file)
#            # записываем строку, отрезая переход на новую строку 
#            write.writerow([line.rstrip()])
#        file.close()


f = open('teo2_energyloop_acoust.spec')


for line in f:
    if fnmatch.fnmatch(line, '#S*')== True: 
        filename = ('scan_'+ line[3:8]+'.csv')
        #write_stroke(filename, line, 'w+')
        file = open(filename, 'w+', newline ='') 
        with file:     
            write = csv.writer(file)
            # записываем строку, отрезая переход на новую строку 
            write.writerow([line.rstrip()])
        file.close()

    elif fnmatch.fnmatch(line, '#C Acquisition ended*')== True: 
        continue
    elif line == '\n': 
        continue
    elif fnmatch.fnmatch(line, '#*')== True:
        file = open(filename, 'a', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerow([line.rstrip()])
        file.close() 
    else:
        lst = line.split()
        #print(lst)
        file = open(filename, 'a', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerow(line.rstrip().split())
        file.close()   



f.close()