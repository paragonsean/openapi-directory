QT += network

HEADERS += \
# Models
    $${PWD}/OAIDynamicMetricCriteria.h \
    $${PWD}/OAIDynamicThresholdFailingPeriods.h \
    $${PWD}/OAIMetricAlertAction.h \
    $${PWD}/OAIMetricAlertCriteria.h \
    $${PWD}/OAIMetricAlertMultipleResourceMultipleMetricCriteria.h \
    $${PWD}/OAIMetricAlertProperties.h \
    $${PWD}/OAIMetricAlertResource.h \
    $${PWD}/OAIMetricAlertResourceCollection.h \
    $${PWD}/OAIMetricAlertResourcePatch.h \
    $${PWD}/OAIMetricAlertSingleResourceMultipleMetricCriteria.h \
    $${PWD}/OAIMetricAlertStatus.h \
    $${PWD}/OAIMetricAlertStatusCollection.h \
    $${PWD}/OAIMetricAlertStatusProperties.h \
    $${PWD}/OAIMetricAlerts_ListBySubscription_default_response.h \
    $${PWD}/OAIMetricCriteria.h \
    $${PWD}/OAIMetricDimension.h \
    $${PWD}/OAIMultiMetricCriteria.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIMetricAlertsApi.h \
    $${PWD}/OAIMetricAlertsStatusApi.h \
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
    $${PWD}/OAIDynamicMetricCriteria.cpp \
    $${PWD}/OAIDynamicThresholdFailingPeriods.cpp \
    $${PWD}/OAIMetricAlertAction.cpp \
    $${PWD}/OAIMetricAlertCriteria.cpp \
    $${PWD}/OAIMetricAlertMultipleResourceMultipleMetricCriteria.cpp \
    $${PWD}/OAIMetricAlertProperties.cpp \
    $${PWD}/OAIMetricAlertResource.cpp \
    $${PWD}/OAIMetricAlertResourceCollection.cpp \
    $${PWD}/OAIMetricAlertResourcePatch.cpp \
    $${PWD}/OAIMetricAlertSingleResourceMultipleMetricCriteria.cpp \
    $${PWD}/OAIMetricAlertStatus.cpp \
    $${PWD}/OAIMetricAlertStatusCollection.cpp \
    $${PWD}/OAIMetricAlertStatusProperties.cpp \
    $${PWD}/OAIMetricAlerts_ListBySubscription_default_response.cpp \
    $${PWD}/OAIMetricCriteria.cpp \
    $${PWD}/OAIMetricDimension.cpp \
    $${PWD}/OAIMultiMetricCriteria.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIMetricAlertsApi.cpp \
    $${PWD}/OAIMetricAlertsStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
