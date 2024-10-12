QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedServerSecurityAlertPolicy.h \
    $${PWD}/OAIManagedServerSecurityAlertPolicyListResult.h \
    $${PWD}/OAISecurityAlertPolicyProperties.h \
# APIs
    $${PWD}/OAIManagedServerSecurityAlertPoliciesApi.h \
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
    $${PWD}/OAIManagedServerSecurityAlertPolicy.cpp \
    $${PWD}/OAIManagedServerSecurityAlertPolicyListResult.cpp \
    $${PWD}/OAISecurityAlertPolicyProperties.cpp \
# APIs
    $${PWD}/OAIManagedServerSecurityAlertPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
