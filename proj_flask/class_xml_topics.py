""" class_xml_topics.py
	Processes XML file topics.xml
"""
# class_xml_topics.py

### Usage:
##import class_xml_topics
##import class_xml_topics
##topics = class_xml_topics.XmlTopics('topics.xml')
##print('\nGet all topics:')
##li = topics.get()
##for dic in li:
##    print('\t', dic['title'])
##
##url_find = 'url-topic-two'
##print('\nGet topic title = "%s" :' %url_find)
##li = topics.get(url_find)
##if len(li) == 0:
##    print('\taHref "%s" not found in topics' %url_find)
##else:
##    for dic in li:
##        print('\t', dic['title'])
##        print('\t', dic['aHref'])
##        print('\t', dic['aTitle'])
##    print('Also:')
##    print("\ttopics.title: %s" % topics.title)
##    print("\ttopics.ahref: %s" % topics.ahref)
##    print("\ttopics.atitle: %s" % topics.atitle)
##
##url_find = 'Not Found'
##print('\nGet topic title = "%s" :' %url_find)
##li = topics.get(url_find)
##if len(li) == 0:
##    print('\taHref "%s" not found in topics' %url_find)
##else:
##    for dic in li:
##        print('\t', dic['title'])
##        print('\t', dic['aHref'])
##        print('\t', dic['aTitle'])
##    print('Also:')
##    print("\ttopics.title: %s" % topics.title)
##    print("\ttopics.ahref: %s" % topics.ahref)
##    print("\ttopics.atitle: %s" % topics.atitle)

	
class XmlTopics:
    'Class for reading topics.xml'

    # topics.xml
    # <topics>
    #   <topic>
    #       <aHref>url-to-follow</aHref>
    #       <aTitle>title for url</aTitle>
    #       <title>Topic Title</title>
    #       <text>
    #           <![CDATA[
    #           ]]>
    #       </text>
    #   </topic>
    #   <topic>
    #   ..
    #   </topic>
    # </topics>

    def __init__(self, sFilePathXml):
        self.clear()
        self.filepathxml = sFilePathXml
        # minidom method
        from xml.dom import minidom
        myminidom = minidom.parse(sFilePathXml)
        self.topics = myminidom.getElementsByTagName('topic')
        #print(type(self.topics), ' # items ', len(self.topics))
        #print('XmlTopics initialized for ', sFilePathXml)

    def clear(self):
        self.title=''; self.ahref=''; self.atitle=''; self.imgsrc=''; self.text=''
        
    def get(self, url_find=None):
        #Returns a list of dictionary objects.
        #If url_find arg is passed, returns only that item.
        i = 0
        li = []
        for topic in self.topics:
            ahref = topic.getElementsByTagName('aHref')[0]
            self.ahref = ahref.childNodes[0].data

            if url_find:
                if self.ahref == url_find:
                    title = topic.getElementsByTagName('title')[0]
                    self.title = title.childNodes[0].data

                    atitle = topic.getElementsByTagName('aTitle')[0]
                    self.atitle = atitle.childNodes[0].data

                    imgsrc = topic.getElementsByTagName('imgSrc')[0]
                    self.imgsrc = imgsrc.childNodes[0].data

                    text = topic.getElementsByTagName('text')[0]
                    self.text = text.childNodes[0].data

                    li.append({'title': self.title, 'aHref': self.ahref, 'imgSrc': self.imgsrc, 'aTitle': self.atitle, 'text': self.text})
                    i += 1
                    return li
            else:
                title = topic.getElementsByTagName('title')[0]
                self.title = title.childNodes[0].data

                atitle = topic.getElementsByTagName('aTitle')[0]
                self.atitle = atitle.childNodes[0].data

                imgsrc = topic.getElementsByTagName('imgSrc')[0]
                self.imgsrc = imgsrc.childNodes[0].data

                text = topic.getElementsByTagName('text')[0]
                self.text = text.childNodes[0].data

                li.append({'title': self.title, 'aHref': self.ahref, 'imgSrc': self.imgsrc, 'aTitle': self.atitle, 'text': self.text})
                i += 1
        self.clear()
        return li

"""
def testXmlTopics():    
    # Usage test & demonstration
    topics = XmlTopics('topics.xml')
    print('\nGet all topics:')
    li = topics.get()
    for dic in li:
        print('\t', dic['title'])

    url_find = 'url-topic-two'
    print('\nGet topic aHref = "%s" :' %url_find)
    li = topics.get(url_find)
    if len(li) == 0:
        print('\tTitle "%s" not found in topics' %url_find)
    else:
        for dic in li:
            print('\t', dic['title'])
            print('\t', dic['aHref'])
            print('\t', dic['aTitle'])
        print('Also:')
        print("\ttopics.title: %s" % topics.title)
        print("\ttopics.ahref: %s" % topics.ahref)
        print("\ttopics.atitle: %s" % topics.atitle)

    url_find = 'Not Found'
    print('\nGet topic url = "%s" :' %url_find)
    li = topics.get(url_find)
    if len(li) == 0:
        print('\taHref "%s" not found in topics' %url_find)
    else:
        for dic in li:
            print('\t', dic['title'])
            print('\t', dic['aHref'])
            print('\t', dic['aTitle'])
        print('Also:')
        print("\ttopics.title: %s" % topics.title)
        print("\ttopics.ahref: %s" % topics.ahref)
        print("\ttopics.atitle: %s" % topics.atitle)

testXmlTopics()
"""
