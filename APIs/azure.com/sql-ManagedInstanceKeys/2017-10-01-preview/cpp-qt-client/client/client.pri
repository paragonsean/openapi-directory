QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedInstanceKey.h \
    $${PWD}/OAIManagedInstanceKeyListResult.h \
    $${PWD}/OAIManagedInstanceKeyProperties.h \
# APIs
    $${PWD}/OAIManagedInstanceKeysApi.h \
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
    $${PWD}/OAIManagedInstanceKey.cpp \
    $${PWD}/OAIManagedInstanceKeyListResult.cpp \
    $${PWD}/OAIManagedInstanceKeyProperties.cpp \
# APIs
    $${PWD}/OAIManagedInstanceKeysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
