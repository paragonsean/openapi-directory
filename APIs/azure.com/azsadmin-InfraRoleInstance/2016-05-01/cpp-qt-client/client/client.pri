QT += network

HEADERS += \
# Models
    $${PWD}/OAIInfraRoleInstance.h \
    $${PWD}/OAIInfraRoleInstanceList.h \
    $${PWD}/OAIInfraRoleInstanceModel.h \
    $${PWD}/OAIInfraRoleInstanceSize.h \
# APIs
    $${PWD}/OAIInfraRoleInstancesApi.h \
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
    $${PWD}/OAIInfraRoleInstance.cpp \
    $${PWD}/OAIInfraRoleInstanceList.cpp \
    $${PWD}/OAIInfraRoleInstanceModel.cpp \
    $${PWD}/OAIInfraRoleInstanceSize.cpp \
# APIs
    $${PWD}/OAIInfraRoleInstancesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
