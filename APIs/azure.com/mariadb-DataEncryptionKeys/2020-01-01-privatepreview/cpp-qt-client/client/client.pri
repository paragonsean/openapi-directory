QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIServerKey.h \
    $${PWD}/OAIServerKeyListResult.h \
    $${PWD}/OAIServerKeyProperties.h \
# APIs
    $${PWD}/OAIServerKeysApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIServerKey.cpp \
    $${PWD}/OAIServerKeyListResult.cpp \
    $${PWD}/OAIServerKeyProperties.cpp \
# APIs
    $${PWD}/OAIServerKeysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
