QT += network

HEADERS += \
# Models
    $${PWD}/OAIMacAddressPool.h \
    $${PWD}/OAIMacAddressPoolList.h \
    $${PWD}/OAIMacAddressPoolModel.h \
# APIs
    $${PWD}/OAIMacAddressPoolsApi.h \
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
    $${PWD}/OAIMacAddressPool.cpp \
    $${PWD}/OAIMacAddressPoolList.cpp \
    $${PWD}/OAIMacAddressPoolModel.cpp \
# APIs
    $${PWD}/OAIMacAddressPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
