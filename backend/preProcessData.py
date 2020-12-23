import string,re
from pyvi.ViTokenizer import tokenize


def wordSegment(sent):
    sent = tokenize(sent)
    return sent

def sentenceSegment(text):
    sents = re.split('[\s-]|(?<!\d)[,.](?!\d)', text)
    sents = list(filter(None,sents))
    return sents
# ()?[]+||\s
def normalizeText(text):
    listpunctuation = string.punctuation.replace('_', '')
    for i in listpunctuation:
        text = text.replace(i, ' ')
    return text.lower()

def removeStopWord(text,list_stopwords):
    pre_text = []
    words = text
    
    for word in words[0]:
        if word not in list_stopwords:
            pre_text.append(word)
    # text2 = ' '.join(pre_text)

    return pre_text
def stopWordsLst():
    data = []
    with open('stopwords.txt', 'r') as fp:
        for line in fp:
            data.append(line.strip('\n'))
    return data

# sentences = ['cán vi phạm lọt ủy nguyễn phú trọng đảng cộng sản việt nam tô lâm tổng bí thư chủ tịch nguyễn phú trọng thủ tướng nguyễn xuân phúc trưởng công an tô lâm đại hội cán vi phạm ủy', 
#             'đại biểu quốc hội lo tốc bắc nam chậm tiến độ quốc hội đầu tư ppp đầu tư công chậm tiến độ đấu thầu định thầu đường sắt', 'ban bí thư bổ nhiệm phó trưởng ban tuyên giáo trung ương đảng cộng sản việt nam', 'quan lựa nhân', 'mỹ hào thành thành phố 2025', '90 ngành tuyên giáo đảng đảng cộng sản việt nam việt hùng trực ban bí thư trần quốc vượng 90 ngành tuyên giáo đảng', 'mặt nhân kỷ niệm 90 ngành tuyên giáo đảng cộng sản việt nam việt hùng kỷ niệm 90 ngành tuyên giáo trực ban bí thư trí thức nghệ sĩ', 
#             'hàng loạt lãnh đạo huyện kỷ luật hóa lãnh đạo kỷ luật vay 52 tỷ chi tiêu kỷ luật lãnh đọa yên định', 
#             'khai trừ đảng cựu phó chủ tịch tp hcm nguyễn hữu tín tp', 'hồ chí minh phan văn vũ nguyễn phú trọng đảng cộng sản việt nam ban bí thư ủy ban kiểm tra trung ương tổng bí thư chủ tịch nguyễn phú trọng kỷ luật tài sản thất thoát khai trừ đảng', 'thủ tướng mặt mẹ việt nam hùng hà nội quảng nam phủ đào ngọc dung đặng thị ngọc thịnh mẹ việt nam hùng thủ tướng nguyễn xuân phúc thương binh liệt sỹ', 'mai văn bí thư ban tổ chức trung ương đảng cộng sản việt nam ban tổ chức trung ương mai văn trưởng ban bí thư', 
#             'tổng bí thư chủ tịch nguyễn phú trọng bcđ tư phòng chống tham nhũng đà nẵng thái nguyên quảng ngãi phú thọ nguyễn phú trọng đảng cộng sản việt nam ban đạo trung ương phòng chống tham nhũng tổng bí thư chủ tịch nguyễn phú trọng']

# print(sentences[0].split(" "))
# print(sentenceSegment(sentences[0]))
# print(sentences[0])
