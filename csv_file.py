from metaflow import FlowSpec, Parameter, step, IncludeFile
 
from io import StringIO
import csv
 
class CSVFileFlow(FlowSpec):
 
    data = IncludeFile('csv',
                       help="CSV file to be parsed",
                       is_text=True)
 
    delimiter = Parameter('delimiter',
                          help="delimiter",
                          default=',')
 
    @step
    def start(self):
        print(self.data)
        print(len(self.data))
        print('num lines:', len(self.data.split('\n')))
        print(type(self.data))
        # fileobj = StringIO(self.data)
        # for i, row in enumerate(csv.reader(fileobj, delimiter=self.delimiter)):
        #     print("row %d: %s" % (i, row))
        self.next(self.end)
 
    @step
    def end(self):
        print('done!')
 
if __name__ == '__main__':
    CSVFileFlow()