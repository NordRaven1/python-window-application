import data

data.get_result()
data.createGreetingWindow()
if data.Username != "":
    data.get_result()
    while True:
        if data.Aanswers != 10:
            if data.Flag:
                data.createTestWindow(data.Window_number)
        else:
            data.write_result(data.Username)
            break
if data.Aanswers == 10:
    data.createResultsWindow()
