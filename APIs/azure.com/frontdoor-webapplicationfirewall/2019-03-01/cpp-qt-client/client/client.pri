QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionType.h \
    $${PWD}/OAICustomRule.h \
    $${PWD}/OAICustomRuleList.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIFrontendEndpointLink.h \
    $${PWD}/OAIManagedRuleDefinition.h \
    $${PWD}/OAIManagedRuleEnabledState.h \
    $${PWD}/OAIManagedRuleGroupDefinition.h \
    $${PWD}/OAIManagedRuleGroupOverride.h \
    $${PWD}/OAIManagedRuleOverride.h \
    $${PWD}/OAIManagedRuleSet.h \
    $${PWD}/OAIManagedRuleSetDefinition.h \
    $${PWD}/OAIManagedRuleSetDefinitionList.h \
    $${PWD}/OAIManagedRuleSetDefinitionProperties.h \
    $${PWD}/OAIManagedRuleSetList.h \
    $${PWD}/OAIMatchCondition.h \
    $${PWD}/OAIPolicySettings.h \
    $${PWD}/OAITransformType.h \
    $${PWD}/OAIWebApplicationFirewallPolicy.h \
    $${PWD}/OAIWebApplicationFirewallPolicyList.h \
    $${PWD}/OAIWebApplicationFirewallPolicyProperties.h \
# APIs
    $${PWD}/OAIWebApplicationFirewallManagedRuleSetsApi.h \
    $${PWD}/OAIWebApplicationFirewallPoliciesApi.h \
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
    $${PWD}/OAIActionType.cpp \
    $${PWD}/OAICustomRule.cpp \
    $${PWD}/OAICustomRuleList.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIFrontendEndpointLink.cpp \
    $${PWD}/OAIManagedRuleDefinition.cpp \
    $${PWD}/OAIManagedRuleEnabledState.cpp \
    $${PWD}/OAIManagedRuleGroupDefinition.cpp \
    $${PWD}/OAIManagedRuleGroupOverride.cpp \
    $${PWD}/OAIManagedRuleOverride.cpp \
    $${PWD}/OAIManagedRuleSet.cpp \
    $${PWD}/OAIManagedRuleSetDefinition.cpp \
    $${PWD}/OAIManagedRuleSetDefinitionList.cpp \
    $${PWD}/OAIManagedRuleSetDefinitionProperties.cpp \
    $${PWD}/OAIManagedRuleSetList.cpp \
    $${PWD}/OAIMatchCondition.cpp \
    $${PWD}/OAIPolicySettings.cpp \
    $${PWD}/OAITransformType.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicy.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicyList.cpp \
    $${PWD}/OAIWebApplicationFirewallPolicyProperties.cpp \
# APIs
    $${PWD}/OAIWebApplicationFirewallManagedRuleSetsApi.cpp \
    $${PWD}/OAIWebApplicationFirewallPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
