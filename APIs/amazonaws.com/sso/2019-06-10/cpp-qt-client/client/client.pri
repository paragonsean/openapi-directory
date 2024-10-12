QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountInfo.h \
    $${PWD}/OAIGetRoleCredentialsResponse.h \
    $${PWD}/OAIGetRoleCredentialsResponse_roleCredentials.h \
    $${PWD}/OAIListAccountRolesResponse.h \
    $${PWD}/OAIListAccountsResponse.h \
    $${PWD}/OAIRoleCredentials.h \
    $${PWD}/OAIRoleInfo.h \
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
    $${PWD}/OAIAccountInfo.cpp \
    $${PWD}/OAIGetRoleCredentialsResponse.cpp \
    $${PWD}/OAIGetRoleCredentialsResponse_roleCredentials.cpp \
    $${PWD}/OAIListAccountRolesResponse.cpp \
    $${PWD}/OAIListAccountsResponse.cpp \
    $${PWD}/OAIRoleCredentials.cpp \
    $${PWD}/OAIRoleInfo.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
