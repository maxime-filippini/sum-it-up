from sumitup.nlp.model import FrequencySummarizer
from sumitup.structures import Article

text = """
Researchers studying the ocean at depths of up to 6km have found that climate change has a "worrying" effect on its ability to lock away carbon. The latest discovery comes from the International "i-Atlantic" project. It has revealed that - if global temperatures increase to levels predicted - the ocean will not be able to provide what is currently Earth\'s largest long-term carbon store. One third of the carbon dioxide in our atmosphere dissolves in the ocean. It therefore acts as an important buffer against rising temperatures. Carbon is one of the chemical elements in the key planet-warming gas known as carbon dioxide (CO2). CO2 from the atmosphere can be taken up by the ocean, where the carbon within it can be stored in a different form
- such as carbonates.However, this stored carbon has the potential to be released back into the atmosphere at a later date as CO2, where it can contribute to global warming. When the carbon dioxide taken up by the ocean is used in photosynthesis by marine plants, it becomes part of a cycle that has stored billions of tonnes of carbon in the deep ocean - and its muddy floor. The researchers say their latest experiments show that this cycle is disrupted by rising ocean temperatures. In experiments carried out from the Spanish research vessel Sarmiento de Gamboa, scientists used tethered, robotic sample collectors to bring tubes of seafloor mud into their ocean laboratories. They then incubated those samples at deep ocean temperatures that are currently predicted for the end of this century. "This deep \'abyssal\' ocean covers 60% of our planet and we\'re finding that, under higher temperatures, we can store less carbon in these places," said Prof Murray Roberts from the University of Edinburgh. "The ecosystems are turning the carbon over faster, they\'re running at a higher temperature more quickly, and they\'re going to release more carbon in the future." Prof Roberts said these experiments, which were led by Prof Andrew Sweetman\'s team at Edinburgh\'s Heriot-Watt University, showed that human activity had changed the "very nature" of the
vast ocean. "As well as our carbon emissions, the ocean has absorbed over 90% of global heating," he explained. "And if we don\'t understand [the impact of this] well enough, we can\'t make the most accurate models in the future." The need to understand more about the ocean\'s response to climate change, he added, was being brought into sharp focus by the negotiations at COP26 about how global leaders tackle the crisis. The same research project, which is funded by the European Commission, recently discovered a dozen new ocean species in the Atlantic. Professor Daniela Schmidt, from the University of Bristol, who was not involved in this research, and who studies the causes and effects of climate change in the ocean, told BBC News: "It\'s often
said that we know more about the surface of the Earth than we do about the deep ocean, and it\'s true. "It\'s the largest habitat on Planet Earth." Because it\'s so vast, and so poorly understood, Prof Schmidt added, "the worry is that we\'ll start destroying those ecosystems - and perturb all these vital processes - that we really don\'t understand".
"""

article = Article(
    headline="Ocean's climate change 'buffer' role under threat",
    body=text,
    url="",
    sentences=[],
)

fs = FrequencySummarizer()

summarized = fs.run(article=article)

print(summarized.body)
