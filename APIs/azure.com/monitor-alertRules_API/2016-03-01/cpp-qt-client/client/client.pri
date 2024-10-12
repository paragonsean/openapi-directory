QT += network

HEADERS += \
# Models
    $${PWD}/OAIAlertRule.h \
    $${PWD}/OAIAlertRuleResource.h \
    $${PWD}/OAIAlertRuleResourceCollection.h \
    $${PWD}/OAIAlertRuleResourcePatch.h \
    $${PWD}/OAIConditionOperator.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILocationThresholdRuleCondition.h \
    $${PWD}/OAIManagementEventAggregationCondition.h \
    $${PWD}/OAIManagementEventRuleCondition.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIRuleAction.h \
    $${PWD}/OAIRuleCondition.h \
    $${PWD}/OAIRuleDataSource.h \
    $${PWD}/OAIRuleEmailAction.h \
    $${PWD}/OAIRuleManagementEventClaimsDataSource.h \
    $${PWD}/OAIRuleManagementEventDataSource.h \
    $${PWD}/OAIRuleMetricDataSource.h \
    $${PWD}/OAIRuleWebhookAction.h \
    $${PWD}/OAIThresholdRuleCondition.h \
    $${PWD}/OAITimeAggregationOperator.h \
# APIs
    $${PWD}/OAIAlertRulesApi.h \
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAlertRule.cpp \
    $${PWD}/OAIAlertRuleResource.cpp \
    $${PWD}/OAIAlertRuleResourceCollection.cpp \
    $${PWD}/OAIAlertRuleResourcePatch.cpp \
    $${PWD}/OAIConditionOperator.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILocationThresholdRuleCondition.cpp \
    $${PWD}/OAIManagementEventAggregationCondition.cpp \
    $${PWD}/OAIManagementEventRuleCondition.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIRuleAction.cpp \
    $${PWD}/OAIRuleCondition.cpp \
    $${PWD}/OAIRuleDataSource.cpp \
    $${PWD}/OAIRuleEmailAction.cpp \
    $${PWD}/OAIRuleManagementEventClaimsDataSource.cpp \
    $${PWD}/OAIRuleManagementEventDataSource.cpp \
    $${PWD}/OAIRuleMetricDataSource.cpp \
    $${PWD}/OAIRuleWebhookAction.cpp \
    $${PWD}/OAIThresholdRuleCondition.cpp \
    $${PWD}/OAITimeAggregationOperator.cpp \
# APIs
    $${PWD}/OAIAlertRulesApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
