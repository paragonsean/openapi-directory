QT += network

HEADERS += \
# Models
    $${PWD}/OAIInvokeEndpointAsyncOutput.h \
    $${PWD}/OAIInvokeEndpointInput.h \
    $${PWD}/OAIInvokeEndpointOutput.h \
    $${PWD}/OAIInvokeEndpoint_request.h \
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
    $${PWD}/OAIInvokeEndpointAsyncOutput.cpp \
    $${PWD}/OAIInvokeEndpointInput.cpp \
    $${PWD}/OAIInvokeEndpointOutput.cpp \
    $${PWD}/OAIInvokeEndpoint_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
