QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionGroupsInformation.h \
    $${PWD}/OAIAlertRule.h \
    $${PWD}/OAIAlertRulePatchObject.h \
    $${PWD}/OAIAlertRulePatchProperties.h \
    $${PWD}/OAIAlertRuleProperties.h \
    $${PWD}/OAIAlertRulesList.h \
    $${PWD}/OAIAzureResource.h \
    $${PWD}/OAIDetector.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIThrottlingInformation.h \
# APIs
    $${PWD}/OAISmartDetectorAlertRulesApi.h \
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
    $${PWD}/OAIActionGroupsInformation.cpp \
    $${PWD}/OAIAlertRule.cpp \
    $${PWD}/OAIAlertRulePatchObject.cpp \
    $${PWD}/OAIAlertRulePatchProperties.cpp \
    $${PWD}/OAIAlertRuleProperties.cpp \
    $${PWD}/OAIAlertRulesList.cpp \
    $${PWD}/OAIAzureResource.cpp \
    $${PWD}/OAIDetector.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIThrottlingInformation.cpp \
# APIs
    $${PWD}/OAISmartDetectorAlertRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
