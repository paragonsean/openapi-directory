QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeleteThingShadowResponse.h \
    $${PWD}/OAIGetRetainedMessageResponse.h \
    $${PWD}/OAIGetThingShadowResponse.h \
    $${PWD}/OAIListNamedShadowsForThingResponse.h \
    $${PWD}/OAIListRetainedMessagesResponse.h \
    $${PWD}/OAIPayloadFormatIndicator.h \
    $${PWD}/OAIPublishRequest.h \
    $${PWD}/OAIPublish_request.h \
    $${PWD}/OAIRetainedMessageSummary.h \
    $${PWD}/OAIUpdateThingShadowRequest.h \
    $${PWD}/OAIUpdateThingShadowResponse.h \
    $${PWD}/OAIUpdateThingShadow_request.h \
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
    $${PWD}/OAIDeleteThingShadowResponse.cpp \
    $${PWD}/OAIGetRetainedMessageResponse.cpp \
    $${PWD}/OAIGetThingShadowResponse.cpp \
    $${PWD}/OAIListNamedShadowsForThingResponse.cpp \
    $${PWD}/OAIListRetainedMessagesResponse.cpp \
    $${PWD}/OAIPayloadFormatIndicator.cpp \
    $${PWD}/OAIPublishRequest.cpp \
    $${PWD}/OAIPublish_request.cpp \
    $${PWD}/OAIRetainedMessageSummary.cpp \
    $${PWD}/OAIUpdateThingShadowRequest.cpp \
    $${PWD}/OAIUpdateThingShadowResponse.cpp \
    $${PWD}/OAIUpdateThingShadow_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
