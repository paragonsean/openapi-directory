QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationSecurityGroup.h \
    $${PWD}/OAIApplicationSecurityGroupListResult.h \
    $${PWD}/OAIApplicationSecurityGroupPropertiesFormat.h \
    $${PWD}/OAIApplicationSecurityGroups_UpdateTags_request.h \
# APIs
    $${PWD}/OAIApplicationSecurityGroupsApi.h \
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
    $${PWD}/OAIApplicationSecurityGroup.cpp \
    $${PWD}/OAIApplicationSecurityGroupListResult.cpp \
    $${PWD}/OAIApplicationSecurityGroupPropertiesFormat.cpp \
    $${PWD}/OAIApplicationSecurityGroups_UpdateTags_request.cpp \
# APIs
    $${PWD}/OAIApplicationSecurityGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
