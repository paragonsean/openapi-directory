QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseSecurityAlertListResult.h \
    $${PWD}/OAIDatabaseSecurityAlertPolicy.h \
    $${PWD}/OAISecurityAlertPolicyProperties.h \
# APIs
    $${PWD}/OAIDatabaseSecurityAlertPoliciesApi.h \
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
    $${PWD}/OAIDatabaseSecurityAlertListResult.cpp \
    $${PWD}/OAIDatabaseSecurityAlertPolicy.cpp \
    $${PWD}/OAISecurityAlertPolicyProperties.cpp \
# APIs
    $${PWD}/OAIDatabaseSecurityAlertPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
