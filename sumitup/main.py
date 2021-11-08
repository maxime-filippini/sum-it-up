import sumitup.source.cnn as cnn
import sumitup.source.bbc as bbc
import sumitup.nlp.model as model


source = bbc.BbcNewsSource()
page_urls = source.get_page_urls()
page_gen = source.parse_pages(page_urls)

page = next(page_gen)

model = model.FrequencySummarizer()
output = model.run(text=page.body)

print(output)
