QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckZappitiServiceRequest.h \
    $${PWD}/OAICheckZappitiServiceResult.h \
    $${PWD}/OAIConnectionDetailsRequest.h \
    $${PWD}/OAIConnectionDetailsResult.h \
    $${PWD}/OAIErrorCode.h \
    $${PWD}/OAIInstallZappitiServiceRequest.h \
    $${PWD}/OAIInstallZappitiServiceResult.h \
    $${PWD}/OAIIsAliveRequest.h \
    $${PWD}/OAIIsAliveResult.h \
    $${PWD}/OAILastMediaRequest.h \
    $${PWD}/OAILastMediaResult.h \
    $${PWD}/OAIStartVideoRequest.h \
    $${PWD}/OAIStartVideoResult.h \
    $${PWD}/OAIStartZappitiServiceRequest.h \
    $${PWD}/OAIStartZappitiServiceResult.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
    $${PWD}/OAIPlaybackApi.h \
    $${PWD}/OAIZappitiServiceApi.h \
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
    $${PWD}/OAICheckZappitiServiceRequest.cpp \
    $${PWD}/OAICheckZappitiServiceResult.cpp \
    $${PWD}/OAIConnectionDetailsRequest.cpp \
    $${PWD}/OAIConnectionDetailsResult.cpp \
    $${PWD}/OAIErrorCode.cpp \
    $${PWD}/OAIInstallZappitiServiceRequest.cpp \
    $${PWD}/OAIInstallZappitiServiceResult.cpp \
    $${PWD}/OAIIsAliveRequest.cpp \
    $${PWD}/OAIIsAliveResult.cpp \
    $${PWD}/OAILastMediaRequest.cpp \
    $${PWD}/OAILastMediaResult.cpp \
    $${PWD}/OAIStartVideoRequest.cpp \
    $${PWD}/OAIStartVideoResult.cpp \
    $${PWD}/OAIStartZappitiServiceRequest.cpp \
    $${PWD}/OAIStartZappitiServiceResult.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
    $${PWD}/OAIPlaybackApi.cpp \
    $${PWD}/OAIZappitiServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
