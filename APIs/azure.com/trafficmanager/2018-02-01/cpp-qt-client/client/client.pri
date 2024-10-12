QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckTrafficManagerRelativeDnsNameAvailabilityParameters.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIDeleteOperationResult.h \
    $${PWD}/OAIDnsConfig.h \
    $${PWD}/OAIEndpoint.h \
    $${PWD}/OAIEndpointProperties.h \
    $${PWD}/OAIGeographicHierarchyProperties.h \
    $${PWD}/OAIMonitorConfig.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAIProfileListResult.h \
    $${PWD}/OAIProfileProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIRegion.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAITrafficManagerGeographicHierarchy.h \
    $${PWD}/OAITrafficManagerNameAvailability.h \
# APIs
    $${PWD}/OAIEndpointsApi.h \
    $${PWD}/OAIGeographicHierarchiesApi.h \
    $${PWD}/OAIProfilesApi.h \
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
    $${PWD}/OAICheckTrafficManagerRelativeDnsNameAvailabilityParameters.cpp \
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIDeleteOperationResult.cpp \
    $${PWD}/OAIDnsConfig.cpp \
    $${PWD}/OAIEndpoint.cpp \
    $${PWD}/OAIEndpointProperties.cpp \
    $${PWD}/OAIGeographicHierarchyProperties.cpp \
    $${PWD}/OAIMonitorConfig.cpp \
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAIProfileListResult.cpp \
    $${PWD}/OAIProfileProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIRegion.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAITrafficManagerGeographicHierarchy.cpp \
    $${PWD}/OAITrafficManagerNameAvailability.cpp \
# APIs
    $${PWD}/OAIEndpointsApi.cpp \
    $${PWD}/OAIGeographicHierarchiesApi.cpp \
    $${PWD}/OAIProfilesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
