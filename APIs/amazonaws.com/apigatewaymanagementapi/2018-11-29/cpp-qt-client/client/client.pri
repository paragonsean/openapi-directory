QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetConnectionResponse.h \
    $${PWD}/OAIGetConnectionResponse_Identity.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIPostToConnectionRequest.h \
    $${PWD}/OAIPostToConnection_request.h \
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
    $${PWD}/OAIGetConnectionResponse.cpp \
    $${PWD}/OAIGetConnectionResponse_Identity.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIPostToConnectionRequest.cpp \
    $${PWD}/OAIPostToConnection_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
