QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIImageObject.h \
    $${PWD}/OAIImages.h \
    $${PWD}/OAIMediaObject.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAIThing.h \
    $${PWD}/OAIWebPage.h \
# APIs
    $${PWD}/OAICustomImageSearchApi.h \
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
    $${PWD}/OAIImageObject.cpp \
    $${PWD}/OAIImages.cpp \
    $${PWD}/OAIMediaObject.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAIThing.cpp \
    $${PWD}/OAIWebPage.cpp \
# APIs
    $${PWD}/OAICustomImageSearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
