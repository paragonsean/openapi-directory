QT += network

HEADERS += \
# Models
    $${PWD}/OAIAction.h \
    $${PWD}/OAIAlertSeverity.h \
    $${PWD}/OAIAlertingAction.h \
    $${PWD}/OAIAzNsActionGroup.h \
    $${PWD}/OAIConditionalOperator.h \
    $${PWD}/OAICriteria.h \
    $${PWD}/OAIDimension.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogMetricTrigger.h \
    $${PWD}/OAILogSearchRule.h \
    $${PWD}/OAILogSearchRulePatch.h \
    $${PWD}/OAILogSearchRuleResource.h \
    $${PWD}/OAILogSearchRuleResourceCollection.h \
    $${PWD}/OAILogSearchRuleResourcePatch.h \
    $${PWD}/OAILogToMetricAction.h \
    $${PWD}/OAIMetricTriggerType.h \
    $${PWD}/OAIQueryType.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISchedule.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAITriggerCondition.h \
# APIs
    $${PWD}/OAIScheduledQueryRulesApi.h \
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
    $${PWD}/OAIAction.cpp \
    $${PWD}/OAIAlertSeverity.cpp \
    $${PWD}/OAIAlertingAction.cpp \
    $${PWD}/OAIAzNsActionGroup.cpp \
    $${PWD}/OAIConditionalOperator.cpp \
    $${PWD}/OAICriteria.cpp \
    $${PWD}/OAIDimension.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogMetricTrigger.cpp \
    $${PWD}/OAILogSearchRule.cpp \
    $${PWD}/OAILogSearchRulePatch.cpp \
    $${PWD}/OAILogSearchRuleResource.cpp \
    $${PWD}/OAILogSearchRuleResourceCollection.cpp \
    $${PWD}/OAILogSearchRuleResourcePatch.cpp \
    $${PWD}/OAILogToMetricAction.cpp \
    $${PWD}/OAIMetricTriggerType.cpp \
    $${PWD}/OAIQueryType.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISchedule.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAITriggerCondition.cpp \
# APIs
    $${PWD}/OAIScheduledQueryRulesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
