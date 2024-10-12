QT += network

HEADERS += \
# Models
    $${PWD}/OAIBudget.h \
    $${PWD}/OAIBudgetProperties.h \
    $${PWD}/OAIBudgetTimePeriod.h \
    $${PWD}/OAIBudgetsListResult.h \
    $${PWD}/OAICurrentSpend.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAINotification.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIProxyResource.h \
# APIs
    $${PWD}/OAIBudgetsPreviewApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIBudget.cpp \
    $${PWD}/OAIBudgetProperties.cpp \
    $${PWD}/OAIBudgetTimePeriod.cpp \
    $${PWD}/OAIBudgetsListResult.cpp \
    $${PWD}/OAICurrentSpend.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAINotification.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIProxyResource.cpp \
# APIs
    $${PWD}/OAIBudgetsPreviewApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
