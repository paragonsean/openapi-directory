QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIExecution.h \
    $${PWD}/OAIListExecutionsResponse.h \
    $${PWD}/OAIPosition.h \
    $${PWD}/OAIStackTrace.h \
    $${PWD}/OAIStackTraceElement.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIStep.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIExecution.cpp \
    $${PWD}/OAIListExecutionsResponse.cpp \
    $${PWD}/OAIPosition.cpp \
    $${PWD}/OAIStackTrace.cpp \
    $${PWD}/OAIStackTraceElement.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIStep.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
