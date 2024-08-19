QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessToken.h \
    $${PWD}/OAIConnection.h \
    $${PWD}/OAIRefreshToken.h \
# APIs
    $${PWD}/OAIIdentityApi.h \
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
    $${PWD}/OAIAccessToken.cpp \
    $${PWD}/OAIConnection.cpp \
    $${PWD}/OAIRefreshToken.cpp \
# APIs
    $${PWD}/OAIIdentityApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
