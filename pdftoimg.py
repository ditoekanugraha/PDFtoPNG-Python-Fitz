import fitz
i=0;
kontinu=True;
print("""|   Converting PDF to multiple PNG files using python(+fitz)""")
while(kontinu):
    files=input("PDF filenames (without .pdf): ")
    document=fitz.open("./"+files+".pdf")
    for page in document:
        pager = document.loadPage(i)
        i=i+1;
        pix = pager.getPixmap(matrix=fitz.Matrix(300/72,300/72))
        output = "./PNG, "+files+", Page "+str(i)+".png"
        print("Printed page: "+str(i))
        pix.writePNG(output)
    print("Conversion completed, check your file")
    choice = input("""------
1: Convert other PDF
2: Quit
Convert other PDF or Quit: """)
    if(int(choice) == 2):
        kontinu=False
    else:
        kontinu=True
        document.close()
        i=0
        print("-----")
