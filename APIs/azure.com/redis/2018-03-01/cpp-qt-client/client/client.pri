QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityParameters.h \
    $${PWD}/OAIExportRDBParameters.h \
    $${PWD}/OAIImportRDBParameters.h \
    $${PWD}/OAINotificationListResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIRedisAccessKeys.h \
    $${PWD}/OAIRedisCommonProperties.h \
    $${PWD}/OAIRedisCreateParameters.h \
    $${PWD}/OAIRedisCreateProperties.h \
    $${PWD}/OAIRedisFirewallRule.h \
    $${PWD}/OAIRedisFirewallRuleCreateParameters.h \
    $${PWD}/OAIRedisFirewallRuleListResult.h \
    $${PWD}/OAIRedisFirewallRuleProperties.h \
    $${PWD}/OAIRedisForceRebootResponse.h \
    $${PWD}/OAIRedisLinkedServer.h \
    $${PWD}/OAIRedisLinkedServerCreateParameters.h \
    $${PWD}/OAIRedisLinkedServerCreateProperties.h \
    $${PWD}/OAIRedisLinkedServerProperties.h \
    $${PWD}/OAIRedisLinkedServerWithProperties.h \
    $${PWD}/OAIRedisLinkedServerWithPropertiesList.h \
    $${PWD}/OAIRedisListResult.h \
    $${PWD}/OAIRedisPatchSchedule.h \
    $${PWD}/OAIRedisPatchScheduleListResult.h \
    $${PWD}/OAIRedisProperties.h \
    $${PWD}/OAIRedisRebootParameters.h \
    $${PWD}/OAIRedisRegenerateKeyParameters.h \
    $${PWD}/OAIRedisResource.h \
    $${PWD}/OAIRedisUpdateParameters.h \
    $${PWD}/OAIRedisUpdateProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIScheduleEntries.h \
    $${PWD}/OAIScheduleEntry.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAIUpgradeNotification.h \
# APIs
    $${PWD}/OAIFirewallRulesApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIPatchSchedulesApi.h \
    $${PWD}/OAIRedisApi.h \
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
    $${PWD}/OAICheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIExportRDBParameters.cpp \
    $${PWD}/OAIImportRDBParameters.cpp \
    $${PWD}/OAINotificationListResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIRedisAccessKeys.cpp \
    $${PWD}/OAIRedisCommonProperties.cpp \
    $${PWD}/OAIRedisCreateParameters.cpp \
    $${PWD}/OAIRedisCreateProperties.cpp \
    $${PWD}/OAIRedisFirewallRule.cpp \
    $${PWD}/OAIRedisFirewallRuleCreateParameters.cpp \
    $${PWD}/OAIRedisFirewallRuleListResult.cpp \
    $${PWD}/OAIRedisFirewallRuleProperties.cpp \
    $${PWD}/OAIRedisForceRebootResponse.cpp \
    $${PWD}/OAIRedisLinkedServer.cpp \
    $${PWD}/OAIRedisLinkedServerCreateParameters.cpp \
    $${PWD}/OAIRedisLinkedServerCreateProperties.cpp \
    $${PWD}/OAIRedisLinkedServerProperties.cpp \
    $${PWD}/OAIRedisLinkedServerWithProperties.cpp \
    $${PWD}/OAIRedisLinkedServerWithPropertiesList.cpp \
    $${PWD}/OAIRedisListResult.cpp \
    $${PWD}/OAIRedisPatchSchedule.cpp \
    $${PWD}/OAIRedisPatchScheduleListResult.cpp \
    $${PWD}/OAIRedisProperties.cpp \
    $${PWD}/OAIRedisRebootParameters.cpp \
    $${PWD}/OAIRedisRegenerateKeyParameters.cpp \
    $${PWD}/OAIRedisResource.cpp \
    $${PWD}/OAIRedisUpdateParameters.cpp \
    $${PWD}/OAIRedisUpdateProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIScheduleEntries.cpp \
    $${PWD}/OAIScheduleEntry.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAIUpgradeNotification.cpp \
# APIs
    $${PWD}/OAIFirewallRulesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIPatchSchedulesApi.cpp \
    $${PWD}/OAIRedisApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
