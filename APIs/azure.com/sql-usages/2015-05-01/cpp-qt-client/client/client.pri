QT += network

HEADERS += \
# Models
    $${PWD}/OAISubscriptionUsage.h \
    $${PWD}/OAISubscriptionUsageListResult.h \
    $${PWD}/OAISubscriptionUsageProperties.h \
# APIs
    $${PWD}/OAISubscriptionUsagesApi.h \
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
    $${PWD}/OAISubscriptionUsage.cpp \
    $${PWD}/OAISubscriptionUsageListResult.cpp \
    $${PWD}/OAISubscriptionUsageProperties.cpp \
# APIs
    $${PWD}/OAISubscriptionUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
