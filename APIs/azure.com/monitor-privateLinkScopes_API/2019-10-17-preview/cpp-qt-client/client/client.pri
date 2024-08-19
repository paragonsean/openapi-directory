QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureMonitorPrivateLinkScope.h \
    $${PWD}/OAIAzureMonitorPrivateLinkScopeListResult.h \
    $${PWD}/OAIAzureMonitorPrivateLinkScopeProperties.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPrivateEndpointConnection.h \
    $${PWD}/OAIPrivateEndpointConnectionListResult.h \
    $${PWD}/OAIPrivateEndpointConnectionProperties.h \
    $${PWD}/OAIPrivateEndpointProperty.h \
    $${PWD}/OAIPrivateLinkResource.h \
    $${PWD}/OAIPrivateLinkResourceListResult.h \
    $${PWD}/OAIPrivateLinkResourceProperties.h \
    $${PWD}/OAIPrivateLinkScopesResource.h \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIScopedResource.h \
    $${PWD}/OAIScopedResourceListResult.h \
    $${PWD}/OAIScopedResourceProperties.h \
    $${PWD}/OAITagsResource.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIPrivateEndpointConnectionsApi.h \
    $${PWD}/OAIPrivateLinkResourcesApi.h \
    $${PWD}/OAIPrivateLinkScopedResourcesApi.h \
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
    $${PWD}/OAIAzureMonitorPrivateLinkScope.cpp \
    $${PWD}/OAIAzureMonitorPrivateLinkScopeListResult.cpp \
    $${PWD}/OAIAzureMonitorPrivateLinkScopeProperties.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPrivateEndpointConnection.cpp \
    $${PWD}/OAIPrivateEndpointConnectionListResult.cpp \
    $${PWD}/OAIPrivateEndpointConnectionProperties.cpp \
    $${PWD}/OAIPrivateEndpointProperty.cpp \
    $${PWD}/OAIPrivateLinkResource.cpp \
    $${PWD}/OAIPrivateLinkResourceListResult.cpp \
    $${PWD}/OAIPrivateLinkResourceProperties.cpp \
    $${PWD}/OAIPrivateLinkScopesResource.cpp \
    $${PWD}/OAIPrivateLinkServiceConnectionStateProperty.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIScopedResource.cpp \
    $${PWD}/OAIScopedResourceListResult.cpp \
    $${PWD}/OAIScopedResourceProperties.cpp \
    $${PWD}/OAITagsResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIPrivateEndpointConnectionsApi.cpp \
    $${PWD}/OAIPrivateLinkResourcesApi.cpp \
    $${PWD}/OAIPrivateLinkScopedResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
