QT += network

HEADERS += \
# Models
    $${PWD}/OAINewQuote.h \
    $${PWD}/OAIQOD.h \
    $${PWD}/OAIQODResponse.h \
    $${PWD}/OAIQODResponse_contents.h \
    $${PWD}/OAIQuote.h \
    $${PWD}/OAIQuoteResponse.h \
    $${PWD}/OAIQuoteResponse_contents.h \
    $${PWD}/OAISuccessResponse.h \
# APIs
    $${PWD}/OAIPrivateQODApi.h \
    $${PWD}/OAIPrivateQuotesApi.h \
    $${PWD}/OAIQshowApi.h \
    $${PWD}/OAIQuoteApi.h \
    $${PWD}/OAIQuoteImagesApi.h \
    $${PWD}/OAIQuoteOfTheDayApi.h \
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
    $${PWD}/OAINewQuote.cpp \
    $${PWD}/OAIQOD.cpp \
    $${PWD}/OAIQODResponse.cpp \
    $${PWD}/OAIQODResponse_contents.cpp \
    $${PWD}/OAIQuote.cpp \
    $${PWD}/OAIQuoteResponse.cpp \
    $${PWD}/OAIQuoteResponse_contents.cpp \
    $${PWD}/OAISuccessResponse.cpp \
# APIs
    $${PWD}/OAIPrivateQODApi.cpp \
    $${PWD}/OAIPrivateQuotesApi.cpp \
    $${PWD}/OAIQshowApi.cpp \
    $${PWD}/OAIQuoteApi.cpp \
    $${PWD}/OAIQuoteImagesApi.cpp \
    $${PWD}/OAIQuoteOfTheDayApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
