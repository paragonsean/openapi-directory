QT += network

HEADERS += \
# Models
    $${PWD}/OAIIpPool.h \
    $${PWD}/OAIIpPoolList.h \
    $${PWD}/OAIIpPoolModel.h \
# APIs
    $${PWD}/OAIIpPoolsApi.h \
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
    $${PWD}/OAIIpPool.cpp \
    $${PWD}/OAIIpPoolList.cpp \
    $${PWD}/OAIIpPoolModel.cpp \
# APIs
    $${PWD}/OAIIpPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
