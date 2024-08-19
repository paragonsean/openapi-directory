QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchMessage.h \
    $${PWD}/OAIBatchMessageResponse.h \
    $${PWD}/OAICancelledMessageResponse.h \
    $${PWD}/OAICreditsResponse.h \
    $${PWD}/OAIDeletedMessageResponse.h \
    $${PWD}/OAIErrorModel.h \
    $${PWD}/OAIExtendedErrorModel.h \
    $${PWD}/OAIMessage.h \
    $${PWD}/OAIMessageResponse.h \
    $${PWD}/OAIMessageResponse_failurereason.h \
    $${PWD}/OAIMessage_metadata.h \
    $${PWD}/OAIMetaData.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQuery_metadata.h \
    $${PWD}/OAIScheduledBatchResponse.h \
    $${PWD}/OAIScheduledMessage.h \
    $${PWD}/OAIScheduledMessageResponse.h \
    $${PWD}/OAIScheduledMessagesResponse.h \
    $${PWD}/OAIScheduledMessagesResponse_message.h \
    $${PWD}/OAISendMessageResponse.h \
    $${PWD}/OAITestResponse.h \
# APIs
    $${PWD}/OAIBatchMessagesApi.h \
    $${PWD}/OAICreditsApi.h \
    $${PWD}/OAIMessagesApi.h \
    $${PWD}/OAIUtilsApi.h \
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
    $${PWD}/OAIBatchMessage.cpp \
    $${PWD}/OAIBatchMessageResponse.cpp \
    $${PWD}/OAICancelledMessageResponse.cpp \
    $${PWD}/OAICreditsResponse.cpp \
    $${PWD}/OAIDeletedMessageResponse.cpp \
    $${PWD}/OAIErrorModel.cpp \
    $${PWD}/OAIExtendedErrorModel.cpp \
    $${PWD}/OAIMessage.cpp \
    $${PWD}/OAIMessageResponse.cpp \
    $${PWD}/OAIMessageResponse_failurereason.cpp \
    $${PWD}/OAIMessage_metadata.cpp \
    $${PWD}/OAIMetaData.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQuery_metadata.cpp \
    $${PWD}/OAIScheduledBatchResponse.cpp \
    $${PWD}/OAIScheduledMessage.cpp \
    $${PWD}/OAIScheduledMessageResponse.cpp \
    $${PWD}/OAIScheduledMessagesResponse.cpp \
    $${PWD}/OAIScheduledMessagesResponse_message.cpp \
    $${PWD}/OAISendMessageResponse.cpp \
    $${PWD}/OAITestResponse.cpp \
# APIs
    $${PWD}/OAIBatchMessagesApi.cpp \
    $${PWD}/OAICreditsApi.cpp \
    $${PWD}/OAIMessagesApi.cpp \
    $${PWD}/OAIUtilsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
