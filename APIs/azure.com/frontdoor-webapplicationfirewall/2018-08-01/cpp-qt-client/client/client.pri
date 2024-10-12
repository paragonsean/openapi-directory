QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureManagedOverrideRuleGroup.h \
    $${PWD}/OAIAzureManagedRuleSet.h \
    $${PWD}/OAICustomRule.h \
    $${PWD}/OAICustomRules.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIManagedRuleSet.h \
    $${PWD}/OAIManagedRuleSets.h \
    $${PWD}/OAIMatchCondition.h \
    $${PWD}/OAIPolicySettings.h \
    $${PWD}/OAITransform.h \
    $${PWD}/OAIWebApplicationFirewallPolicy.h \
    $${PWD}/OAIWebApplicationFirewallPolicyListResult.h \
    $${PWD}/OAIWebApplicationFirewallPolicyPropertiesFormat.h \
# APIs
    $${PWD}/OAICreateOrUpdateWebApplicationFirewallPolicyApi.h \
    $${PWD}/OAIDeleteWebApplicationFirewallPolicyApi.h \
    $${PWD}/OAIGetWebapplicationfirewallPolicyApi.h \
    $${PWD}/OAIListWebApplicationFirewallPoliciesApi.h \
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
    $${PWD}/OAIAzureManagedOverrideRuleGroup.cpp \
    $${PWD}/OAIAzureManagedRuleSet.cpp \
    $${PWD}/OAICustomRule.cpp \
    $${PWD}/OAICustomRules.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIManagedRuleSet.cpp \
    $${PWD}/OAIManagedRuleSets.cpp \
    $${PWD}/OAIMatchCondition.cpp \
    $${PWD}/OAIPolicySettings.cpp \
    $${PWD}/OAITransform.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicy.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicyListResult.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicyPropertiesFormat.cpp \
# APIs
    $${PWD}/OAICreateOrUpdateWebApplicationFirewallPolicyApi.cpp \
    $${PWD}/OAIDeleteWebApplicationFirewallPolicyApi.cpp \
    $${PWD}/OAIGetWebapplicationfirewallPolicyApi.cpp \
    $${PWD}/OAIListWebApplicationFirewallPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
