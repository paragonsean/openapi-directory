QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIPrivateEndpointConnection.h \
    $${PWD}/OAIPrivateEndpointConnectionListResult.h \
    $${PWD}/OAIPrivateEndpointConnectionProperties.h \
    $${PWD}/OAIPrivateEndpointProperty.h \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITagsObject.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIPrivateEndpointConnection.cpp \
    $${PWD}/OAIPrivateEndpointConnectionListResult.cpp \
    $${PWD}/OAIPrivateEndpointConnectionProperties.cpp \
    $${PWD}/OAIPrivateEndpointProperty.cpp \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITagsObject.cpp \
# APIs
    $${PWD}/OAIPrivateEndpointConnectionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
