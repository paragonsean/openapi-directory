QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutomation.h \
    $${PWD}/OAIAutomationAction.h \
    $${PWD}/OAIAutomationActionEventHub.h \
    $${PWD}/OAIAutomationActionLogicApp.h \
    $${PWD}/OAIAutomationActionWorkspace.h \
    $${PWD}/OAIAutomationList.h \
    $${PWD}/OAIAutomationProperties.h \
    $${PWD}/OAIAutomationRuleSet.h \
    $${PWD}/OAIAutomationScope.h \
    $${PWD}/OAIAutomationSource.h \
    $${PWD}/OAIAutomationTriggeringRule.h \
    $${PWD}/OAIAutomationValidationStatus.h \
    $${PWD}/OAIAutomations_List_default_response.h \
    $${PWD}/OAIAutomations_List_default_response_error.h \
# APIs
    $${PWD}/OAIAutomationsApi.h \
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
    $${PWD}/OAIAutomation.cpp \
    $${PWD}/OAIAutomationAction.cpp \
    $${PWD}/OAIAutomationActionEventHub.cpp \
    $${PWD}/OAIAutomationActionLogicApp.cpp \
    $${PWD}/OAIAutomationActionWorkspace.cpp \
    $${PWD}/OAIAutomationList.cpp \
    $${PWD}/OAIAutomationProperties.cpp \
    $${PWD}/OAIAutomationRuleSet.cpp \
    $${PWD}/OAIAutomationScope.cpp \
    $${PWD}/OAIAutomationSource.cpp \
    $${PWD}/OAIAutomationTriggeringRule.cpp \
    $${PWD}/OAIAutomationValidationStatus.cpp \
    $${PWD}/OAIAutomations_List_default_response.cpp \
    $${PWD}/OAIAutomations_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIAutomationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
