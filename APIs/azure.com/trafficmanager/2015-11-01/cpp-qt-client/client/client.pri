QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckTrafficManagerRelativeDnsNameAvailabilityParameters.h \
    $${PWD}/OAIDnsConfig.h \
    $${PWD}/OAIEndpoint.h \
    $${PWD}/OAIEndpointProperties.h \
    $${PWD}/OAIMonitorConfig.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAIProfileListResult.h \
    $${PWD}/OAIProfileProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISubResource.h \
    $${PWD}/OAITrafficManagerNameAvailability.h \
# APIs
    $${PWD}/OAIEndpointsApi.h \
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
    $${PWD}/OAIDnsConfig.cpp \
    $${PWD}/OAIEndpoint.cpp \
    $${PWD}/OAIEndpointProperties.cpp \
    $${PWD}/OAIMonitorConfig.cpp \
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAIProfileListResult.cpp \
    $${PWD}/OAIProfileProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISubResource.cpp \
    $${PWD}/OAITrafficManagerNameAvailability.cpp \
# APIs
    $${PWD}/OAIEndpointsApi.cpp \
    $${PWD}/OAIProfilesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
