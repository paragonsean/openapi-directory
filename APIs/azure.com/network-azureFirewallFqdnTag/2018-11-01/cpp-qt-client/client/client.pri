QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureFirewallFqdnTag.h \
    $${PWD}/OAIAzureFirewallFqdnTagListResult.h \
    $${PWD}/OAIAzureFirewallFqdnTagPropertiesFormat.h \
# APIs
    $${PWD}/OAIAzureFirewallFqdnTagsApi.h \
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
    $${PWD}/OAIAzureFirewallFqdnTag.cpp \
    $${PWD}/OAIAzureFirewallFqdnTagListResult.cpp \
    $${PWD}/OAIAzureFirewallFqdnTagPropertiesFormat.cpp \
# APIs
    $${PWD}/OAIAzureFirewallFqdnTagsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
