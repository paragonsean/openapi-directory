QT += network

HEADERS += \
# Models
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIEvent_metricAttribution.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIMetricAttribution.h \
    $${PWD}/OAIPutEventsRequest.h \
    $${PWD}/OAIPutEvents_request.h \
    $${PWD}/OAIPutItemsRequest.h \
    $${PWD}/OAIPutItems_request.h \
    $${PWD}/OAIPutUsersRequest.h \
    $${PWD}/OAIPutUsers_request.h \
    $${PWD}/OAIUser.h \
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
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIEvent_metricAttribution.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIMetricAttribution.cpp \
    $${PWD}/OAIPutEventsRequest.cpp \
    $${PWD}/OAIPutEvents_request.cpp \
    $${PWD}/OAIPutItemsRequest.cpp \
    $${PWD}/OAIPutItems_request.cpp \
    $${PWD}/OAIPutUsersRequest.cpp \
    $${PWD}/OAIPutUsers_request.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
