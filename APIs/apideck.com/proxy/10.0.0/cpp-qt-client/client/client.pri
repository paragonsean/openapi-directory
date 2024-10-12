QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetProxy_401_response.h \
    $${PWD}/OAIPostProxy_request.h \
    $${PWD}/OAIPutProxy_request.h \
# APIs
    $${PWD}/OAIExecuteApi.h \
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
    $${PWD}/OAIGetProxy_401_response.cpp \
    $${PWD}/OAIPostProxy_request.cpp \
    $${PWD}/OAIPutProxy_request.cpp \
# APIs
    $${PWD}/OAIExecuteApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
