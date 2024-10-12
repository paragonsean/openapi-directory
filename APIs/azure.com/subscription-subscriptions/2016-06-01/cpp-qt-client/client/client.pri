QT += network

HEADERS += \
# Models
    $${PWD}/OAILocation.h \
    $${PWD}/OAILocationListResult.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAISubscriptionListResult.h \
    $${PWD}/OAISubscriptionPolicies.h \
    $${PWD}/OAITenantIdDescription.h \
    $${PWD}/OAITenantListResult.h \
# APIs
    $${PWD}/OAISubscriptionsApi.h \
    $${PWD}/OAITenantsApi.h \
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
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILocationListResult.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAISubscriptionListResult.cpp \
    $${PWD}/OAISubscriptionPolicies.cpp \
    $${PWD}/OAITenantIdDescription.cpp \
    $${PWD}/OAITenantListResult.cpp \
# APIs
    $${PWD}/OAISubscriptionsApi.cpp \
    $${PWD}/OAITenantsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
