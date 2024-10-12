QT += network

HEADERS += \
# Models
    $${PWD}/OAIOrchestratorProfile.h \
    $${PWD}/OAIOrchestratorVersionProfile.h \
    $${PWD}/OAIOrchestratorVersionProfileListResult.h \
    $${PWD}/OAIOrchestratorVersionProfileProperties.h \
# APIs
    $${PWD}/OAIContainerServicesApi.h \
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
    $${PWD}/OAIOrchestratorProfile.cpp \
    $${PWD}/OAIOrchestratorVersionProfile.cpp \
    $${PWD}/OAIOrchestratorVersionProfileListResult.cpp \
    $${PWD}/OAIOrchestratorVersionProfileProperties.cpp \
# APIs
    $${PWD}/OAIContainerServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
