QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutoApprovedPrivateLinkService.h \
    $${PWD}/OAIAutoApprovedPrivateLinkServicesResult.h \
    $${PWD}/OAICheckPrivateLinkServiceVisibilityRequest.h \
    $${PWD}/OAIPrivateEndpointConnection.h \
    $${PWD}/OAIPrivateEndpointConnectionProperties.h \
    $${PWD}/OAIPrivateEndpointConnectionProperties_privateEndpoint.h \
    $${PWD}/OAIPrivateLinkService.h \
    $${PWD}/OAIPrivateLinkServiceConnectionState.h \
    $${PWD}/OAIPrivateLinkServiceIpConfiguration.h \
    $${PWD}/OAIPrivateLinkServiceIpConfigurationProperties.h \
    $${PWD}/OAIPrivateLinkServiceIpConfigurationProperties_subnet.h \
    $${PWD}/OAIPrivateLinkServiceListResult.h \
    $${PWD}/OAIPrivateLinkServiceProperties.h \
    $${PWD}/OAIPrivateLinkServiceProperties_loadBalancerFrontendIpConfigurations_inner.h \
    $${PWD}/OAIPrivateLinkServiceProperties_networkInterfaces_inner.h \
    $${PWD}/OAIPrivateLinkServiceVisibility.h \
    $${PWD}/OAIPrivateLinkServices_ListBySubscription_default_response.h \
    $${PWD}/OAIPrivateLinkServices_ListBySubscription_default_response_details_inner.h \
    $${PWD}/OAIResourceSet.h \
# APIs
    $${PWD}/OAIPrivateLinkServiceApi.h \
    $${PWD}/OAIPrivateLinkServicesApi.h \
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
    $${PWD}/OAIAutoApprovedPrivateLinkService.cpp \
    $${PWD}/OAIAutoApprovedPrivateLinkServicesResult.cpp \
    $${PWD}/OAICheckPrivateLinkServiceVisibilityRequest.cpp \
    $${PWD}/OAIPrivateEndpointConnection.cpp \
    $${PWD}/OAIPrivateEndpointConnectionProperties.cpp \
    $${PWD}/OAIPrivateEndpointConnectionProperties_privateEndpoint.cpp \
    $${PWD}/OAIPrivateLinkService.cpp \
    $${PWD}/OAIPrivateLinkServiceConnectionState.cpp \
    $${PWD}/OAIPrivateLinkServiceIpConfiguration.cpp \
    $${PWD}/OAIPrivateLinkServiceIpConfigurationProperties.cpp \
    $${PWD}/OAIPrivateLinkServiceIpConfigurationProperties_subnet.cpp \
    $${PWD}/OAIPrivateLinkServiceListResult.cpp \
    $${PWD}/OAIPrivateLinkServiceProperties.cpp \
    $${PWD}/OAIPrivateLinkServiceProperties_loadBalancerFrontendIpConfigurations_inner.cpp \
    $${PWD}/OAIPrivateLinkServiceProperties_networkInterfaces_inner.cpp \
    $${PWD}/OAIPrivateLinkServiceVisibility.cpp \
    $${PWD}/OAIPrivateLinkServices_ListBySubscription_default_response.cpp \
    $${PWD}/OAIPrivateLinkServices_ListBySubscription_default_response_details_inner.cpp \
    $${PWD}/OAIResourceSet.cpp \
# APIs
    $${PWD}/OAIPrivateLinkServiceApi.cpp \
    $${PWD}/OAIPrivateLinkServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
