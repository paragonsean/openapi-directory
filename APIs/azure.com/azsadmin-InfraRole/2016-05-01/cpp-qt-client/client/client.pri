QT += network

HEADERS += \
# Models
    $${PWD}/OAIInfraRole.h \
    $${PWD}/OAIInfraRoleList.h \
    $${PWD}/OAIInfraRoleModel.h \
# APIs
    $${PWD}/OAIInfraRoleApi.h \
    $${PWD}/OAIInfraRolesApi.h \
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
    $${PWD}/OAIInfraRole.cpp \
    $${PWD}/OAIInfraRoleList.cpp \
    $${PWD}/OAIInfraRoleModel.cpp \
# APIs
    $${PWD}/OAIInfraRoleApi.cpp \
    $${PWD}/OAIInfraRolesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
