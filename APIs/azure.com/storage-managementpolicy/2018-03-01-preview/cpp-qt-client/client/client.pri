QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagementPoliciesRules.h \
    $${PWD}/OAIManagementPoliciesRulesSetParameter.h \
    $${PWD}/OAIStorageAccountManagementPolicies.h \
    $${PWD}/OAIStorageAccountManagementPoliciesRulesProperty.h \
# APIs
    $${PWD}/OAIManagementPoliciesApi.h \
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
    $${PWD}/OAIManagementPoliciesRules.cpp \
    $${PWD}/OAIManagementPoliciesRulesSetParameter.cpp \
    $${PWD}/OAIStorageAccountManagementPolicies.cpp \
    $${PWD}/OAIStorageAccountManagementPoliciesRulesProperty.cpp \
# APIs
    $${PWD}/OAIManagementPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
