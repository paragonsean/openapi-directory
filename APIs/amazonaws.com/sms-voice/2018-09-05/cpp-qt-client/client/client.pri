QT += network

HEADERS += \
# Models
    $${PWD}/OAICallInstructionsMessageType.h \
    $${PWD}/OAICloudWatchLogsDestination.h \
    $${PWD}/OAICreateConfigurationSetEventDestinationRequest.h \
    $${PWD}/OAICreateConfigurationSetEventDestination_request.h \
    $${PWD}/OAICreateConfigurationSetEventDestination_request_EventDestination.h \
    $${PWD}/OAICreateConfigurationSetRequest.h \
    $${PWD}/OAICreateConfigurationSet_request.h \
    $${PWD}/OAIEventDestination.h \
    $${PWD}/OAIEventDestinationDefinition.h \
    $${PWD}/OAIEventType.h \
    $${PWD}/OAIGetConfigurationSetEventDestinationsResponse.h \
    $${PWD}/OAIKinesisFirehoseDestination.h \
    $${PWD}/OAIListConfigurationSetsResponse.h \
    $${PWD}/OAIPlainTextMessageType.h \
    $${PWD}/OAISSMLMessageType.h \
    $${PWD}/OAISendVoiceMessageRequest.h \
    $${PWD}/OAISendVoiceMessageResponse.h \
    $${PWD}/OAISendVoiceMessage_request.h \
    $${PWD}/OAISendVoiceMessage_request_Content.h \
    $${PWD}/OAISnsDestination.h \
    $${PWD}/OAIUpdateConfigurationSetEventDestinationRequest.h \
    $${PWD}/OAIUpdateConfigurationSetEventDestination_request.h \
    $${PWD}/OAIVoiceMessageContent.h \
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
    $${PWD}/OAICallInstructionsMessageType.cpp \
    $${PWD}/OAICloudWatchLogsDestination.cpp \
    $${PWD}/OAICreateConfigurationSetEventDestinationRequest.cpp \
    $${PWD}/OAICreateConfigurationSetEventDestination_request.cpp \
    $${PWD}/OAICreateConfigurationSetEventDestination_request_EventDestination.cpp \
    $${PWD}/OAICreateConfigurationSetRequest.cpp \
    $${PWD}/OAICreateConfigurationSet_request.cpp \
    $${PWD}/OAIEventDestination.cpp \
    $${PWD}/OAIEventDestinationDefinition.cpp \
    $${PWD}/OAIEventType.cpp \
    $${PWD}/OAIGetConfigurationSetEventDestinationsResponse.cpp \
    $${PWD}/OAIKinesisFirehoseDestination.cpp \
    $${PWD}/OAIListConfigurationSetsResponse.cpp \
    $${PWD}/OAIPlainTextMessageType.cpp \
    $${PWD}/OAISSMLMessageType.cpp \
    $${PWD}/OAISendVoiceMessageRequest.cpp \
    $${PWD}/OAISendVoiceMessageResponse.cpp \
    $${PWD}/OAISendVoiceMessage_request.cpp \
    $${PWD}/OAISendVoiceMessage_request_Content.cpp \
    $${PWD}/OAISnsDestination.cpp \
    $${PWD}/OAIUpdateConfigurationSetEventDestinationRequest.cpp \
    $${PWD}/OAIUpdateConfigurationSetEventDestination_request.cpp \
    $${PWD}/OAIVoiceMessageContent.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
