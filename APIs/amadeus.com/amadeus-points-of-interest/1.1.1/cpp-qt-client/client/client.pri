QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_404.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIGeoCode.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAISuccess_1.h \
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
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_404.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIGeoCode.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAISuccess_1.cpp \
# APIs
    $${PWD}/OAIRetrieveApi.cpp \
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
