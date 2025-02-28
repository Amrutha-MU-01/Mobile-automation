file_html = open("C:\\Users\\2022374\\Documents\\vscode\\automation\\demo.html","w")

full_html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    <body>

    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
    <table>
  <tr>
    <th>Sl.No</th>
    <th>Link Name</th>
    <th>LInk href</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>

    </body>
    </html>

'''

#write the html
file_html.write(full_html)

#saving data into html file
file_html.close()
