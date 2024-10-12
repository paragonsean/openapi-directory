QT += network

HEADERS += \
# Models
    $${PWD}/OAILogicalServerSecurityAlertPolicyListResult.h \
    $${PWD}/OAISecurityAlertPolicyProperties.h \
    $${PWD}/OAIServerSecurityAlertPolicy.h \
# APIs
    $${PWD}/OAIServerSecurityAlertPoliciesApi.h \
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
    $${PWD}/OAILogicalServerSecurityAlertPolicyListResult.cpp \
    $${PWD}/OAISecurityAlertPolicyProperties.cpp \
    $${PWD}/OAIServerSecurityAlertPolicy.cpp \
# APIs
    $${PWD}/OAIServerSecurityAlertPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
