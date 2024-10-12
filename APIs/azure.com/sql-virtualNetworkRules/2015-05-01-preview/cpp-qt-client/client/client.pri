QT += network

HEADERS += \
# Models
    $${PWD}/OAIVirtualNetworkRule.h \
    $${PWD}/OAIVirtualNetworkRuleListResult.h \
    $${PWD}/OAIVirtualNetworkRuleProperties.h \
# APIs
    $${PWD}/OAIVirtualNetworkRulesApi.h \
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
    $${PWD}/OAIVirtualNetworkRule.cpp \
    $${PWD}/OAIVirtualNetworkRuleListResult.cpp \
    $${PWD}/OAIVirtualNetworkRuleProperties.cpp \
# APIs
    $${PWD}/OAIVirtualNetworkRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
