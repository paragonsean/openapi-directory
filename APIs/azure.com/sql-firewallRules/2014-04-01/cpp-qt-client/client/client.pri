QT += network

HEADERS += \
# Models
    $${PWD}/OAIFirewallRule.h \
    $${PWD}/OAIFirewallRuleListResult.h \
    $${PWD}/OAIFirewallRuleProperties.h \
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
    $${PWD}/OAIFirewallRuleListResult.cpp \
    $${PWD}/OAIFirewallRuleProperties.cpp \
# APIs
    $${PWD}/OAIFirewallRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
