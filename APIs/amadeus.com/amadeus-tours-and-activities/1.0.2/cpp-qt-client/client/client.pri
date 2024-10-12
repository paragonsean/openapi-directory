QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivity.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIElementaryPrice.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_404.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIGeoCode.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAISuccessful_Search.h \
    $${PWD}/OAISuccessful_Search_1.h \
# APIs
    $${PWD}/OAIRetrieveApi.h \
    $${PWD}/OAISearchApi.h \
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
    $${PWD}/OAIActivity.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIElementaryPrice.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_404.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIGeoCode.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAISuccessful_Search.cpp \
    $${PWD}/OAISuccessful_Search_1.cpp \
# APIs
    $${PWD}/OAIRetrieveApi.cpp \
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
