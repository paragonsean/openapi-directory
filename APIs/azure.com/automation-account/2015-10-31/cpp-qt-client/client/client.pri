QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutomationAccount.h \
    $${PWD}/OAIAutomationAccountCreateOrUpdateParameters.h \
    $${PWD}/OAIAutomationAccountCreateOrUpdateProperties.h \
    $${PWD}/OAIAutomationAccountListResult.h \
    $${PWD}/OAIAutomationAccountProperties.h \
    $${PWD}/OAIAutomationAccountUpdateParameters.h \
    $${PWD}/OAIAutomationAccountUpdateProperties.h \
    $${PWD}/OAIKey.h \
    $${PWD}/OAIKeyListResult.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIOperations_List_default_response.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAIStatistics.h \
    $${PWD}/OAIStatisticsListResult.h \
    $${PWD}/OAIUsage.h \
    $${PWD}/OAIUsageCounterName.h \
    $${PWD}/OAIUsageListResult.h \
# APIs
    $${PWD}/OAIAutomationAccountApi.h \
    $${PWD}/OAIListKeysApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIStatisticsApi.h \
    $${PWD}/OAIUsagesApi.h \
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
    $${PWD}/OAIAutomationAccount.cpp \
    $${PWD}/OAIAutomationAccountCreateOrUpdateParameters.cpp \
    $${PWD}/OAIAutomationAccountCreateOrUpdateProperties.cpp \
    $${PWD}/OAIAutomationAccountListResult.cpp \
    $${PWD}/OAIAutomationAccountProperties.cpp \
    $${PWD}/OAIAutomationAccountUpdateParameters.cpp \
    $${PWD}/OAIAutomationAccountUpdateProperties.cpp \
    $${PWD}/OAIKey.cpp \
    $${PWD}/OAIKeyListResult.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIOperations_List_default_response.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAIStatistics.cpp \
    $${PWD}/OAIStatisticsListResult.cpp \
    $${PWD}/OAIUsage.cpp \
    $${PWD}/OAIUsageCounterName.cpp \
    $${PWD}/OAIUsageListResult.cpp \
# APIs
    $${PWD}/OAIAutomationAccountApi.cpp \
    $${PWD}/OAIListKeysApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIStatisticsApi.cpp \
    $${PWD}/OAIUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
