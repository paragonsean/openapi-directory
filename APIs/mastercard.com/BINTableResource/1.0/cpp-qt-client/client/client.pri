QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinTableResponse.h \
    $${PWD}/OAINoResource.h \
# APIs
    $${PWD}/OAIBINTableListingServiceApi.h \
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
    $${PWD}/OAIBinTableResponse.cpp \
    $${PWD}/OAINoResource.cpp \
# APIs
    $${PWD}/OAIBINTableListingServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
