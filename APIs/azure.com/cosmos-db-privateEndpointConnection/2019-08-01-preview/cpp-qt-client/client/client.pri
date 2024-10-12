QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPrivateEndpointConnection.h \
    $${PWD}/OAIPrivateEndpointConnectionListResult.h \
    $${PWD}/OAIPrivateEndpointConnectionProperties.h \
    $${PWD}/OAIPrivateEndpointProperty.h \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.h \
# APIs
    $${PWD}/OAIPrivateEndpointConnectionsApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPrivateEndpointConnection.cpp \
    $${PWD}/OAIPrivateEndpointConnectionListResult.cpp \
    $${PWD}/OAIPrivateEndpointConnectionProperties.cpp \
    $${PWD}/OAIPrivateEndpointProperty.cpp \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.cpp \
# APIs
    $${PWD}/OAIPrivateEndpointConnectionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
