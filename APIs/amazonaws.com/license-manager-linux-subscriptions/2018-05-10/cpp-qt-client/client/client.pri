QT += network

HEADERS += \
# Models
    $${PWD}/OAIFilter.h \
    $${PWD}/OAIGetServiceSettingsResponse.h \
    $${PWD}/OAIGetServiceSettingsResponse_LinuxSubscriptionsDiscoverySettings.h \
    $${PWD}/OAIInstance.h \
    $${PWD}/OAILinuxSubscriptionsDiscovery.h \
    $${PWD}/OAILinuxSubscriptionsDiscoverySettings.h \
    $${PWD}/OAIListLinuxSubscriptionInstancesRequest.h \
    $${PWD}/OAIListLinuxSubscriptionInstancesResponse.h \
    $${PWD}/OAIListLinuxSubscriptionInstances_request.h \
    $${PWD}/OAIListLinuxSubscriptionsRequest.h \
    $${PWD}/OAIListLinuxSubscriptionsResponse.h \
    $${PWD}/OAIListLinuxSubscriptions_request.h \
    $${PWD}/OAIOperator.h \
    $${PWD}/OAIOrganizationIntegration.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAIUpdateServiceSettingsRequest.h \
    $${PWD}/OAIUpdateServiceSettingsResponse.h \
    $${PWD}/OAIUpdateServiceSettingsResponse_LinuxSubscriptionsDiscoverySettings.h \
    $${PWD}/OAIUpdateServiceSettings_request.h \
    $${PWD}/OAIUpdateServiceSettings_request_LinuxSubscriptionsDiscoverySettings.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIFilter.cpp \
    $${PWD}/OAIGetServiceSettingsResponse.cpp \
    $${PWD}/OAIGetServiceSettingsResponse_LinuxSubscriptionsDiscoverySettings.cpp \
    $${PWD}/OAIInstance.cpp \
    $${PWD}/OAILinuxSubscriptionsDiscovery.cpp \
    $${PWD}/OAILinuxSubscriptionsDiscoverySettings.cpp \
    $${PWD}/OAIListLinuxSubscriptionInstancesRequest.cpp \
    $${PWD}/OAIListLinuxSubscriptionInstancesResponse.cpp \
    $${PWD}/OAIListLinuxSubscriptionInstances_request.cpp \
    $${PWD}/OAIListLinuxSubscriptionsRequest.cpp \
    $${PWD}/OAIListLinuxSubscriptionsResponse.cpp \
    $${PWD}/OAIListLinuxSubscriptions_request.cpp \
    $${PWD}/OAIOperator.cpp \
    $${PWD}/OAIOrganizationIntegration.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAIUpdateServiceSettingsRequest.cpp \
    $${PWD}/OAIUpdateServiceSettingsResponse.cpp \
    $${PWD}/OAIUpdateServiceSettingsResponse_LinuxSubscriptionsDiscoverySettings.cpp \
    $${PWD}/OAIUpdateServiceSettings_request.cpp \
    $${PWD}/OAIUpdateServiceSettings_request_LinuxSubscriptionsDiscoverySettings.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
