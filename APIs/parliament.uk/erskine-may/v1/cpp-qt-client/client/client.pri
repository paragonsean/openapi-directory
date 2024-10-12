QT += network

HEADERS += \
# Models
    $${PWD}/OAIErskineMayChapterOverview.h \
    $${PWD}/OAIErskineMayFootnote.h \
    $${PWD}/OAIErskineMayIndexTerm.h \
    $${PWD}/OAIErskineMayIndexTermSearchResult.h \
    $${PWD}/OAIErskineMayIndexTermSearchResultErskineMaySearch.h \
    $${PWD}/OAIErskineMayIndexTermSeeLink.h \
    $${PWD}/OAIErskineMayParagraphSearchResult.h \
    $${PWD}/OAIErskineMayParagraphSearchResultErskineMaySearch.h \
    $${PWD}/OAIErskineMayPart.h \
    $${PWD}/OAIErskineMaySectionDetail.h \
    $${PWD}/OAIErskineMaySectionOverview.h \
    $${PWD}/OAIErskineMaySectionSearchResult.h \
    $${PWD}/OAIErskineMaySectionSearchResultErskineMaySearch.h \
# APIs
    $${PWD}/OAIChapterApi.h \
    $${PWD}/OAIIndexTermApi.h \
    $${PWD}/OAIPartApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAISectionApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIErskineMayChapterOverview.cpp \
    $${PWD}/OAIErskineMayFootnote.cpp \
    $${PWD}/OAIErskineMayIndexTerm.cpp \
    $${PWD}/OAIErskineMayIndexTermSearchResult.cpp \
    $${PWD}/OAIErskineMayIndexTermSearchResultErskineMaySearch.cpp \
    $${PWD}/OAIErskineMayIndexTermSeeLink.cpp \
    $${PWD}/OAIErskineMayParagraphSearchResult.cpp \
    $${PWD}/OAIErskineMayParagraphSearchResultErskineMaySearch.cpp \
    $${PWD}/OAIErskineMayPart.cpp \
    $${PWD}/OAIErskineMaySectionDetail.cpp \
    $${PWD}/OAIErskineMaySectionOverview.cpp \
    $${PWD}/OAIErskineMaySectionSearchResult.cpp \
    $${PWD}/OAIErskineMaySectionSearchResultErskineMaySearch.cpp \
# APIs
    $${PWD}/OAIChapterApi.cpp \
    $${PWD}/OAIIndexTermApi.cpp \
    $${PWD}/OAIPartApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAISectionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
