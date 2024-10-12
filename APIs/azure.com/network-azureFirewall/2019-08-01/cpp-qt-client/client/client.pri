QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureFirewall.h \
    $${PWD}/OAIAzureFirewallApplicationRule.h \
    $${PWD}/OAIAzureFirewallApplicationRuleCollection.h \
    $${PWD}/OAIAzureFirewallApplicationRuleCollectionPropertiesFormat.h \
    $${PWD}/OAIAzureFirewallApplicationRuleProtocol.h \
    $${PWD}/OAIAzureFirewallApplicationRuleProtocolType.h \
    $${PWD}/OAIAzureFirewallIPConfiguration.h \
    $${PWD}/OAIAzureFirewallIPConfigurationPropertiesFormat.h \
    $${PWD}/OAIAzureFirewallIPConfigurationPropertiesFormat_publicIPAddress.h \
    $${PWD}/OAIAzureFirewallListResult.h \
    $${PWD}/OAIAzureFirewallNatRCAction.h \
    $${PWD}/OAIAzureFirewallNatRCActionType.h \
    $${PWD}/OAIAzureFirewallNatRule.h \
    $${PWD}/OAIAzureFirewallNatRuleCollection.h \
    $${PWD}/OAIAzureFirewallNatRuleCollectionProperties.h \
    $${PWD}/OAIAzureFirewallNetworkRule.h \
    $${PWD}/OAIAzureFirewallNetworkRuleCollection.h \
    $${PWD}/OAIAzureFirewallNetworkRuleCollectionPropertiesFormat.h \
    $${PWD}/OAIAzureFirewallNetworkRuleProtocol.h \
    $${PWD}/OAIAzureFirewallPropertiesFormat.h \
    $${PWD}/OAIAzureFirewallPublicIPAddress.h \
    $${PWD}/OAIAzureFirewallRCAction.h \
    $${PWD}/OAIAzureFirewallRCActionType.h \
    $${PWD}/OAIAzureFirewallSku.h \
    $${PWD}/OAIAzureFirewallThreatIntelMode.h \
    $${PWD}/OAIHubIPAddresses.h \
# APIs
    $${PWD}/OAIAzureFirewallsApi.h \
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
    $${PWD}/OAIAzureFirewall.cpp \
    $${PWD}/OAIAzureFirewallApplicationRule.cpp \
    $${PWD}/OAIAzureFirewallApplicationRuleCollection.cpp \
    $${PWD}/OAIAzureFirewallApplicationRuleCollectionPropertiesFormat.cpp \
    $${PWD}/OAIAzureFirewallApplicationRuleProtocol.cpp \
    $${PWD}/OAIAzureFirewallApplicationRuleProtocolType.cpp \
    $${PWD}/OAIAzureFirewallIPConfiguration.cpp \
    $${PWD}/OAIAzureFirewallIPConfigurationPropertiesFormat.cpp \
    $${PWD}/OAIAzureFirewallIPConfigurationPropertiesFormat_publicIPAddress.cpp \
    $${PWD}/OAIAzureFirewallListResult.cpp \
    $${PWD}/OAIAzureFirewallNatRCAction.cpp \
    $${PWD}/OAIAzureFirewallNatRCActionType.cpp \
    $${PWD}/OAIAzureFirewallNatRule.cpp \
    $${PWD}/OAIAzureFirewallNatRuleCollection.cpp \
    $${PWD}/OAIAzureFirewallNatRuleCollectionProperties.cpp \
    $${PWD}/OAIAzureFirewallNetworkRule.cpp \
    $${PWD}/OAIAzureFirewallNetworkRuleCollection.cpp \
    $${PWD}/OAIAzureFirewallNetworkRuleCollectionPropertiesFormat.cpp \
    $${PWD}/OAIAzureFirewallNetworkRuleProtocol.cpp \
    $${PWD}/OAIAzureFirewallPropertiesFormat.cpp \
    $${PWD}/OAIAzureFirewallPublicIPAddress.cpp \
    $${PWD}/OAIAzureFirewallRCAction.cpp \
    $${PWD}/OAIAzureFirewallRCActionType.cpp \
    $${PWD}/OAIAzureFirewallSku.cpp \
    $${PWD}/OAIAzureFirewallThreatIntelMode.cpp \
    $${PWD}/OAIHubIPAddresses.cpp \
# APIs
    $${PWD}/OAIAzureFirewallsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
