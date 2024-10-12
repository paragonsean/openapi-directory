QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetLatestConfigurationResponse.h \
    $${PWD}/OAIStartConfigurationSessionRequest.h \
    $${PWD}/OAIStartConfigurationSessionResponse.h \
    $${PWD}/OAIStartConfigurationSession_request.h \
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
    $${PWD}/OAIGetLatestConfigurationResponse.cpp \
    $${PWD}/OAIStartConfigurationSessionRequest.cpp \
    $${PWD}/OAIStartConfigurationSessionResponse.cpp \
    $${PWD}/OAIStartConfigurationSession_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
