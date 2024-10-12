QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcknowledgeRequest.h \
    $${PWD}/OAILabel.h \
    $${PWD}/OAIListSubscriptionsResponse.h \
    $${PWD}/OAIListTopicsResponse.h \
    $${PWD}/OAIModifyAckDeadlineRequest.h \
    $${PWD}/OAIModifyPushConfigRequest.h \
    $${PWD}/OAIPublishBatchRequest.h \
    $${PWD}/OAIPublishBatchResponse.h \
    $${PWD}/OAIPublishRequest.h \
    $${PWD}/OAIPubsubEvent.h \
    $${PWD}/OAIPubsubMessage.h \
    $${PWD}/OAIPullBatchRequest.h \
    $${PWD}/OAIPullBatchResponse.h \
    $${PWD}/OAIPullRequest.h \
    $${PWD}/OAIPullResponse.h \
    $${PWD}/OAIPushConfig.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAITopic.h \
# APIs
    $${PWD}/OAISubscriptionsApi.h \
    $${PWD}/OAITopicsApi.h \
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
    $${PWD}/OAIAcknowledgeRequest.cpp \
    $${PWD}/OAILabel.cpp \
    $${PWD}/OAIListSubscriptionsResponse.cpp \
    $${PWD}/OAIListTopicsResponse.cpp \
    $${PWD}/OAIModifyAckDeadlineRequest.cpp \
    $${PWD}/OAIModifyPushConfigRequest.cpp \
    $${PWD}/OAIPublishBatchRequest.cpp \
    $${PWD}/OAIPublishBatchResponse.cpp \
    $${PWD}/OAIPublishRequest.cpp \
    $${PWD}/OAIPubsubEvent.cpp \
    $${PWD}/OAIPubsubMessage.cpp \
    $${PWD}/OAIPullBatchRequest.cpp \
    $${PWD}/OAIPullBatchResponse.cpp \
    $${PWD}/OAIPullRequest.cpp \
    $${PWD}/OAIPullResponse.cpp \
    $${PWD}/OAIPushConfig.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAITopic.cpp \
# APIs
    $${PWD}/OAISubscriptionsApi.cpp \
    $${PWD}/OAITopicsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
