QT += network

HEADERS += \
# Models
    $${PWD}/OAIEntitlement.h \
    $${PWD}/OAIReader.h \
    $${PWD}/OAIReaderEntitlements.h \
# APIs
    $${PWD}/OAIPublicationsApi.h \
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
    $${PWD}/OAIEntitlement.cpp \
    $${PWD}/OAIReader.cpp \
    $${PWD}/OAIReaderEntitlements.cpp \
# APIs
    $${PWD}/OAIPublicationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
