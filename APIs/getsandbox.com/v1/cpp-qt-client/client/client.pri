QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivityMessage.h \
    $${PWD}/OAIConfiguredRouteDetails.h \
    $${PWD}/OAICreateSandbox.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIRouteConfig.h \
    $${PWD}/OAIRuntimeRequest.h \
    $${PWD}/OAIRuntimeResponse.h \
    $${PWD}/OAIRuntimeTransaction.h \
    $${PWD}/OAISandbox.h \
# APIs
    $${PWD}/OAIActivityApi.h \
    $${PWD}/OAISandboxApi.h \
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
    $${PWD}/OAIActivityMessage.cpp \
    $${PWD}/OAIConfiguredRouteDetails.cpp \
    $${PWD}/OAICreateSandbox.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIRouteConfig.cpp \
    $${PWD}/OAIRuntimeRequest.cpp \
    $${PWD}/OAIRuntimeResponse.cpp \
    $${PWD}/OAIRuntimeTransaction.cpp \
    $${PWD}/OAISandbox.cpp \
# APIs
    $${PWD}/OAIActivityApi.cpp \
    $${PWD}/OAISandboxApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
