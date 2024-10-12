QT += network

HEADERS += \
# Models
    $${PWD}/OAIPermission.h \
    $${PWD}/OAIPermissionGetResult.h \
    $${PWD}/OAIRoleDefinition.h \
    $${PWD}/OAIRoleDefinitionFilter.h \
    $${PWD}/OAIRoleDefinitionListResult.h \
    $${PWD}/OAIRoleDefinitionProperties.h \
# APIs
    $${PWD}/OAIPermissionsApi.h \
    $${PWD}/OAIRoleDefinitionsApi.h \
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
    $${PWD}/OAIPermission.cpp \
    $${PWD}/OAIPermissionGetResult.cpp \
    $${PWD}/OAIRoleDefinition.cpp \
    $${PWD}/OAIRoleDefinitionFilter.cpp \
    $${PWD}/OAIRoleDefinitionListResult.cpp \
    $${PWD}/OAIRoleDefinitionProperties.cpp \
# APIs
    $${PWD}/OAIPermissionsApi.cpp \
    $${PWD}/OAIRoleDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
