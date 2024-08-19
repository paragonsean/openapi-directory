QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQueryContext.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchResponse.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAIThing.h \
    $${PWD}/OAIWebMetaTag.h \
    $${PWD}/OAIWebPage.h \
    $${PWD}/OAIWebWebAnswer.h \
# APIs
    $${PWD}/OAICustomSearchApi.h \
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
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAICreativeWork.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQueryContext.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchResponse.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAIThing.cpp \
    $${PWD}/OAIWebMetaTag.cpp \
    $${PWD}/OAIWebPage.cpp \
    $${PWD}/OAIWebWebAnswer.cpp \
# APIs
    $${PWD}/OAICustomSearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
