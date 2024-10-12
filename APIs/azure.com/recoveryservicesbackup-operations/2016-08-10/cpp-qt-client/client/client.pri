QT += network

HEADERS += \
# Models
    $${PWD}/OAIClientDiscoveryDisplay.h \
    $${PWD}/OAIClientDiscoveryForLogSpecification.h \
    $${PWD}/OAIClientDiscoveryForProperties.h \
    $${PWD}/OAIClientDiscoveryForServiceSpecification.h \
    $${PWD}/OAIClientDiscoveryResponse.h \
    $${PWD}/OAIClientDiscoveryValueForSingleApi.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIClientDiscoveryDisplay.cpp \
    $${PWD}/OAIClientDiscoveryForLogSpecification.cpp \
    $${PWD}/OAIClientDiscoveryForProperties.cpp \
    $${PWD}/OAIClientDiscoveryForServiceSpecification.cpp \
    $${PWD}/OAIClientDiscoveryResponse.cpp \
    $${PWD}/OAIClientDiscoveryValueForSingleApi.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
