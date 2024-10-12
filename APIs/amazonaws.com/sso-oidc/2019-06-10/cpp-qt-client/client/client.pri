QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateTokenRequest.h \
    $${PWD}/OAICreateTokenResponse.h \
    $${PWD}/OAICreateToken_request.h \
    $${PWD}/OAIRegisterClientRequest.h \
    $${PWD}/OAIRegisterClientResponse.h \
    $${PWD}/OAIRegisterClient_request.h \
    $${PWD}/OAIStartDeviceAuthorizationRequest.h \
    $${PWD}/OAIStartDeviceAuthorizationResponse.h \
    $${PWD}/OAIStartDeviceAuthorization_request.h \
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
    $${PWD}/OAICreateTokenRequest.cpp \
    $${PWD}/OAICreateTokenResponse.cpp \
    $${PWD}/OAICreateToken_request.cpp \
    $${PWD}/OAIRegisterClientRequest.cpp \
    $${PWD}/OAIRegisterClientResponse.cpp \
    $${PWD}/OAIRegisterClient_request.cpp \
    $${PWD}/OAIStartDeviceAuthorizationRequest.cpp \
    $${PWD}/OAIStartDeviceAuthorizationResponse.cpp \
    $${PWD}/OAIStartDeviceAuthorization_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
