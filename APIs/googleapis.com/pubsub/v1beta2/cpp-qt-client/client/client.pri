QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcknowledgeRequest.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListSubscriptionsResponse.h \
    $${PWD}/OAIListTopicSubscriptionsResponse.h \
    $${PWD}/OAIListTopicsResponse.h \
    $${PWD}/OAIModifyAckDeadlineRequest.h \
    $${PWD}/OAIModifyPushConfigRequest.h \
    $${PWD}/OAIOidcToken.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIPublishRequest.h \
    $${PWD}/OAIPublishResponse.h \
    $${PWD}/OAIPubsubMessage.h \
    $${PWD}/OAIPullRequest.h \
    $${PWD}/OAIPullResponse.h \
    $${PWD}/OAIPushConfig.h \
    $${PWD}/OAIReceivedMessage.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAITopic.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIListSubscriptionsResponse.cpp \
    $${PWD}/OAIListTopicSubscriptionsResponse.cpp \
    $${PWD}/OAIListTopicsResponse.cpp \
    $${PWD}/OAIModifyAckDeadlineRequest.cpp \
    $${PWD}/OAIModifyPushConfigRequest.cpp \
    $${PWD}/OAIOidcToken.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIPublishRequest.cpp \
    $${PWD}/OAIPublishResponse.cpp \
    $${PWD}/OAIPubsubMessage.cpp \
    $${PWD}/OAIPullRequest.cpp \
    $${PWD}/OAIPullResponse.cpp \
    $${PWD}/OAIPushConfig.cpp \
    $${PWD}/OAIReceivedMessage.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAITopic.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
