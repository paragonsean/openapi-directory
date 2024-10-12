QT += network

HEADERS += \
# Models
    $${PWD}/OAIAlertSummary.h \
    $${PWD}/OAIBaseHealth.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIMetrics.h \
    $${PWD}/OAIMetricsSourceType.h \
    $${PWD}/OAIMetricsUnit.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAIUsageMetrics.h \
# APIs
    $${PWD}/OAIInfrastructureInsightsApi.h \
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
    $${PWD}/OAIAlertSummary.cpp \
    $${PWD}/OAIBaseHealth.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIMetrics.cpp \
    $${PWD}/OAIMetricsSourceType.cpp \
    $${PWD}/OAIMetricsUnit.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAIUsageMetrics.cpp \
# APIs
    $${PWD}/OAIInfrastructureInsightsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
