QT += network

HEADERS += \
# Models
    $${PWD}/OAIEventGridEvent.h \
    $${PWD}/OAISubscriptionDeletedEventData.h \
    $${PWD}/OAISubscriptionValidationEventData.h \
    $${PWD}/OAISubscriptionValidationResponse.h \
# APIs
    $${PWD}/OAIEventsApi.h \
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
    $${PWD}/OAIEventGridEvent.cpp \
    $${PWD}/OAISubscriptionDeletedEventData.cpp \
    $${PWD}/OAISubscriptionValidationEventData.cpp \
    $${PWD}/OAISubscriptionValidationResponse.cpp \
# APIs
    $${PWD}/OAIEventsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
