QT += network

HEADERS += \
# Models
    $${PWD}/OAIFirewallRule.h \
    $${PWD}/OAIFirewallRuleList.h \
    $${PWD}/OAIFirewallRuleListResult.h \
    $${PWD}/OAIProxyResourceWithWritableName.h \
    $${PWD}/OAIResourceWithWritableName.h \
    $${PWD}/OAIServerFirewallRuleProperties.h \
# APIs
    $${PWD}/OAIFirewallRulesApi.h \
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
    $${PWD}/OAIFirewallRule.cpp \
    $${PWD}/OAIFirewallRuleList.cpp \
    $${PWD}/OAIFirewallRuleListResult.cpp \
    $${PWD}/OAIProxyResourceWithWritableName.cpp \
    $${PWD}/OAIResourceWithWritableName.cpp \
    $${PWD}/OAIServerFirewallRuleProperties.cpp \
# APIs
    $${PWD}/OAIFirewallRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
