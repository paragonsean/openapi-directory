QT += network

HEADERS += \
# Models
    $${PWD}/OAIConfig.h \
    $${PWD}/OAIDiscordMessageRequest.h \
    $${PWD}/OAIHTTPValidationError.h \
    $${PWD}/OAISlackMessageRequest.h \
    $${PWD}/OAISnsMessageRequest.h \
    $${PWD}/OAITwilioMessageRequest.h \
    $${PWD}/OAIValidationError.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIDiscordApi.h \
    $${PWD}/OAISlackApi.h \
    $${PWD}/OAISnsApi.h \
    $${PWD}/OAITwilioApi.h \
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
    $${PWD}/OAIConfig.cpp \
    $${PWD}/OAIDiscordMessageRequest.cpp \
    $${PWD}/OAIHTTPValidationError.cpp \
    $${PWD}/OAISlackMessageRequest.cpp \
    $${PWD}/OAISnsMessageRequest.cpp \
    $${PWD}/OAITwilioMessageRequest.cpp \
    $${PWD}/OAIValidationError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIDiscordApi.cpp \
    $${PWD}/OAISlackApi.cpp \
    $${PWD}/OAISnsApi.cpp \
    $${PWD}/OAITwilioApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
