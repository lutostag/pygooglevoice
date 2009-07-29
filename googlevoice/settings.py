LOGIN = 'https://www.google.com/accounts/ServiceLoginAuth?service=grandcentral'
FEEDS = ('contacts','inbox','starred','all','spam','trash','voicemail','sms','recorded','placed','recieved','missed')

BASE = 'https://www.google.com/voice/'
LOGOUT = BASE+'account/signout'
INBOX = BASE+'#inbox'
CALL = BASE+'call/connect/'
CANCEL = BASE+'call/cancel/'
DELETE = BASE+'inbox/deleteMessages/'
STAR = BASE+'inbox/star/'
SMS = BASE+'sms/send/'
DOWNLOAD = BASE+'media/send_voicemail/'
BALANCE = BASE+'settings/billingcredit/'

XML_SEARCH = BASE+'inbox/search/'
XML_CONTACTS = BASE+'contacts/'
XML_RECENT = BASE+'inbox/recent/'
XML_INBOX = XML_RECENT+'inbox/'
XML_STARRED = XML_RECENT+'starred/'
XML_ALL = XML_RECENT+'add/'
XML_SPAM = XML_RECENT+'spam/'
XML_TRASH = XML_RECENT+'trash/'
XML_VOICEMAIL = XML_RECENT+'voicemail/'
XML_SMS = XML_RECENT+'sms/'
XML_RECORDED = XML_RECENT+'recorded/'
XML_PLACED = XML_RECENT+'placed/'
XML_RECIEVED = XML_RECENT+'recieved/'
XML_MISSED = XML_RECENT+'missed/'