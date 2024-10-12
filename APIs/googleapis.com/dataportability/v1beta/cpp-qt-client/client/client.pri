QT += network

HEADERS += \
# Models
    $${PWD}/OAIInitiatePortabilityArchiveRequest.h \
    $${PWD}/OAIInitiatePortabilityArchiveResponse.h \
    $${PWD}/OAIPortabilityArchiveState.h \
    $${PWD}/OAIRetryPortabilityArchiveResponse.h \
# APIs
    $${PWD}/OAIArchiveJobsApi.h \
    $${PWD}/OAIAuthorizationApi.h \
    $${PWD}/OAIPortabilityArchiveApi.h \
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
    $${PWD}/OAIInitiatePortabilityArchiveRequest.cpp \
    $${PWD}/OAIInitiatePortabilityArchiveResponse.cpp \
    $${PWD}/OAIPortabilityArchiveState.cpp \
    $${PWD}/OAIRetryPortabilityArchiveResponse.cpp \
# APIs
    $${PWD}/OAIArchiveJobsApi.cpp \
    $${PWD}/OAIAuthorizationApi.cpp \
    $${PWD}/OAIPortabilityArchiveApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
