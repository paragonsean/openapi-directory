QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationRuleCondition.h \
    $${PWD}/OAIFirewallPolicies_UpdateTags_default_response.h \
    $${PWD}/OAIFirewallPolicies_UpdateTags_default_response_details_inner.h \
    $${PWD}/OAIFirewallPolicies_UpdateTags_request.h \
    $${PWD}/OAIFirewallPolicy.h \
    $${PWD}/OAIFirewallPolicyFilterRule.h \
    $${PWD}/OAIFirewallPolicyFilterRuleAction.h \
    $${PWD}/OAIFirewallPolicyFilterRuleActionType.h \
    $${PWD}/OAIFirewallPolicyListResult.h \
    $${PWD}/OAIFirewallPolicyNatRule.h \
    $${PWD}/OAIFirewallPolicyNatRuleAction.h \
    $${PWD}/OAIFirewallPolicyNatRuleActionType.h \
    $${PWD}/OAIFirewallPolicyPropertiesFormat.h \
    $${PWD}/OAIFirewallPolicyPropertiesFormat_basePolicy.h \
    $${PWD}/OAIFirewallPolicyRule.h \
    $${PWD}/OAIFirewallPolicyRuleCondition.h \
    $${PWD}/OAIFirewallPolicyRuleConditionApplicationProtocol.h \
    $${PWD}/OAIFirewallPolicyRuleConditionApplicationProtocolType.h \
    $${PWD}/OAIFirewallPolicyRuleConditionNetworkProtocol.h \
    $${PWD}/OAIFirewallPolicyRuleGroup.h \
    $${PWD}/OAIFirewallPolicyRuleGroupListResult.h \
    $${PWD}/OAIFirewallPolicyRuleGroupProperties.h \
    $${PWD}/OAINetworkRuleCondition.h \
# APIs
    $${PWD}/OAIFirewallPoliciesApi.h \
    $${PWD}/OAIFirewallPolicyRuleGroupsApi.h \
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
    $${PWD}/OAIApplicationRuleCondition.cpp \
    $${PWD}/OAIFirewallPolicies_UpdateTags_default_response.cpp \
    $${PWD}/OAIFirewallPolicies_UpdateTags_default_response_details_inner.cpp \
    $${PWD}/OAIFirewallPolicies_UpdateTags_request.cpp \
    $${PWD}/OAIFirewallPolicy.cpp \
    $${PWD}/OAIFirewallPolicyFilterRule.cpp \
    $${PWD}/OAIFirewallPolicyFilterRuleAction.cpp \
    $${PWD}/OAIFirewallPolicyFilterRuleActionType.cpp \
    $${PWD}/OAIFirewallPolicyListResult.cpp \
    $${PWD}/OAIFirewallPolicyNatRule.cpp \
    $${PWD}/OAIFirewallPolicyNatRuleAction.cpp \
    $${PWD}/OAIFirewallPolicyNatRuleActionType.cpp \
    $${PWD}/OAIFirewallPolicyPropertiesFormat.cpp \
    $${PWD}/OAIFirewallPolicyPropertiesFormat_basePolicy.cpp \
    $${PWD}/OAIFirewallPolicyRule.cpp \
    $${PWD}/OAIFirewallPolicyRuleCondition.cpp \
    $${PWD}/OAIFirewallPolicyRuleConditionApplicationProtocol.cpp \
    $${PWD}/OAIFirewallPolicyRuleConditionApplicationProtocolType.cpp \
    $${PWD}/OAIFirewallPolicyRuleConditionNetworkProtocol.cpp \
    $${PWD}/OAIFirewallPolicyRuleGroup.cpp \
    $${PWD}/OAIFirewallPolicyRuleGroupListResult.cpp \
    $${PWD}/OAIFirewallPolicyRuleGroupProperties.cpp \
    $${PWD}/OAINetworkRuleCondition.cpp \
# APIs
    $${PWD}/OAIFirewallPoliciesApi.cpp \
    $${PWD}/OAIFirewallPolicyRuleGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
