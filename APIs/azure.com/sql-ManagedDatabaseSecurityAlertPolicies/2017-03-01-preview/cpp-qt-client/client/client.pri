QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedDatabaseSecurityAlertPolicy.h \
    $${PWD}/OAIManagedDatabaseSecurityAlertPolicyListResult.h \
    $${PWD}/OAISecurityAlertPolicyProperties.h \
# APIs
    $${PWD}/OAIManagedDatabaseSecurityAlertPoliciesApi.h \
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
    $${PWD}/OAIManagedDatabaseSecurityAlertPolicy.cpp \
    $${PWD}/OAIManagedDatabaseSecurityAlertPolicyListResult.cpp \
    $${PWD}/OAISecurityAlertPolicyProperties.cpp \
# APIs
    $${PWD}/OAIManagedDatabaseSecurityAlertPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
