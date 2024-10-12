QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedInstanceAdministrator.h \
    $${PWD}/OAIManagedInstanceAdministratorListResult.h \
    $${PWD}/OAIManagedInstanceAdministratorProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIManagedInstanceAdministratorsApi.h \
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
    $${PWD}/OAIManagedInstanceAdministrator.cpp \
    $${PWD}/OAIManagedInstanceAdministratorListResult.cpp \
    $${PWD}/OAIManagedInstanceAdministratorProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIManagedInstanceAdministratorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
