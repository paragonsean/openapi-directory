QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataMaskingPolicy.h \
    $${PWD}/OAIDataMaskingPolicyProperties.h \
    $${PWD}/OAIDataMaskingRule.h \
    $${PWD}/OAIDataMaskingRuleListResult.h \
    $${PWD}/OAIDataMaskingRuleProperties.h \
# APIs
    $${PWD}/OAIDataMaskingPoliciesApi.h \
    $${PWD}/OAIDataMaskingRulesApi.h \
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
    $${PWD}/OAIDataMaskingPolicy.cpp \
    $${PWD}/OAIDataMaskingPolicyProperties.cpp \
    $${PWD}/OAIDataMaskingRule.cpp \
    $${PWD}/OAIDataMaskingRuleListResult.cpp \
    $${PWD}/OAIDataMaskingRuleProperties.cpp \
# APIs
    $${PWD}/OAIDataMaskingPoliciesApi.cpp \
    $${PWD}/OAIDataMaskingRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
