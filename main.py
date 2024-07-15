from typing import Dict
from datetime import datetime
import psycopg2
class Document:
    def __init__(self, Url: str, PubDate: datetime, FetchTime: datetime, Text: str):
        self.Url = Url
        self.PubDate = PubDate
        self.FetchTime = FetchTime
        self.Text = Text
        self.FirstFetchTime = FetchTime
    def returnAll(self):
        return(self.Url, str(self.PubDate), str(self.FetchTime), self.Text, str(self.FirstFetchTime))

class Processor:
    def __init__(self):
        self.Documents: Dict[str, Document] = {}

    def process(self, doc: Document) -> Document:
        if doc.Url not in self.Documents:
            self.Documents[doc.Url] = doc
        else:
            existing_doc = self.Documents[doc.Url]
            if doc.FetchTime > existing_doc.FetchTime:
                existing_doc.Text = doc.Text
                existing_doc.FetchTime = doc.FetchTime
            if doc.PubDate < existing_doc.PubDate:
                existing_doc.PubDate = doc.PubDate
            if doc.FetchTime < existing_doc.FirstFetchTime:
                existing_doc.FirstFetchTime = doc.FetchTime

        return self.Documents[doc.Url]

# Пример использования Processor
doc1 = Document("url1", datetime(2024,7,14,15,38),
                datetime(2024,8,24,21,48), "text1")
doc2 = Document("url1", datetime(2024,7,14,15,38),
                datetime(2024,10,27,17,38), "text2")
doc3 = Document("url1", datetime(2024,7,14,15,38),
                datetime(2024,9,6,5,24), "text3")

processor = Processor()
result1 = processor.process(doc1)
print(result1.returnAll())
result2 = processor.process(doc2)
print(result2.returnAll())
result3 = processor.process(doc3)
print(result3.returnAll())


