QT += network

HEADERS += \
# Models
    $${PWD}/OAIListTracesResponse.h \
    $${PWD}/OAITrace.h \
    $${PWD}/OAITraceSpan.h \
    $${PWD}/OAITraces.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIListTracesResponse.cpp \
    $${PWD}/OAITrace.cpp \
    $${PWD}/OAITraceSpan.cpp \
    $${PWD}/OAITraces.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
