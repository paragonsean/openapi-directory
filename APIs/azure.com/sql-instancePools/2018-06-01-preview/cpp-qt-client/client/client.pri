QT += network

HEADERS += \
# Models
    $${PWD}/OAIInstancePool.h \
    $${PWD}/OAIInstancePoolListResult.h \
    $${PWD}/OAIInstancePoolProperties.h \
    $${PWD}/OAIInstancePoolUpdate.h \
# APIs
    $${PWD}/OAIInstancePoolsApi.h \
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
    $${PWD}/OAIInstancePool.cpp \
    $${PWD}/OAIInstancePoolListResult.cpp \
    $${PWD}/OAIInstancePoolProperties.cpp \
    $${PWD}/OAIInstancePoolUpdate.cpp \
# APIs
    $${PWD}/OAIInstancePoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
