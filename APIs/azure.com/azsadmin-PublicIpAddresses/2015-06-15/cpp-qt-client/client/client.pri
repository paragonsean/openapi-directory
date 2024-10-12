QT += network

HEADERS += \
# Models
    $${PWD}/OAIPublicIPAddressProperties.h \
    $${PWD}/OAIPublicIpAddress.h \
    $${PWD}/OAIPublicIpAddressList.h \
# APIs
    $${PWD}/OAIPublicIpAddressesApi.h \
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
    $${PWD}/OAIPublicIPAddressProperties.cpp \
    $${PWD}/OAIPublicIpAddress.cpp \
    $${PWD}/OAIPublicIpAddressList.cpp \
# APIs
    $${PWD}/OAIPublicIpAddressesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
