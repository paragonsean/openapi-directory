QT += network

HEADERS += \
# Models
    $${PWD}/OAIListSubscriptionsResponse.h \
    $${PWD}/OAINotificationEndpoint.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPayloadOptions.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISubscription.h \
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
    $${PWD}/OAIListSubscriptionsResponse.cpp \
    $${PWD}/OAINotificationEndpoint.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPayloadOptions.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISubscription.cpp \
# APIs
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
