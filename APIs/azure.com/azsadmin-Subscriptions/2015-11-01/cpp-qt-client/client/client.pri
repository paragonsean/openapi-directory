QT += network

HEADERS += \
# Models
    $${PWD}/OAIResource.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAISubscriptionList.h \
    $${PWD}/OAISubscriptionState.h \
# APIs
    $${PWD}/OAISubscriptionsApi.h \
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
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAISubscriptionList.cpp \
    $${PWD}/OAISubscriptionState.cpp \
# APIs
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
