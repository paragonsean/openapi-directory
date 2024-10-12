QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbstractCDocLink.h \
    $${PWD}/OAIAbstractLink.h \
    $${PWD}/OAIAccessTokenData.h \
    $${PWD}/OAIAffiliation.h \
    $${PWD}/OAICollectionDocument.h \
    $${PWD}/OAIDeviceCodeData.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDocument.h \
    $${PWD}/OAISimpleError.h \
# APIs
    $${PWD}/OAIAuthorizationApi.h \
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
    $${PWD}/OAIAbstractCDocLink.cpp \
    $${PWD}/OAIAbstractLink.cpp \
    $${PWD}/OAIAccessTokenData.cpp \
    $${PWD}/OAIAffiliation.cpp \
    $${PWD}/OAICollectionDocument.cpp \
    $${PWD}/OAIDeviceCodeData.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDocument.cpp \
    $${PWD}/OAISimpleError.cpp \
# APIs
    $${PWD}/OAIAuthorizationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
