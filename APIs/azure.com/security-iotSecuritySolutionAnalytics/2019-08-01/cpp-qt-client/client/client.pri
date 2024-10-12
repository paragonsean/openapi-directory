QT += network

HEADERS += \
# Models
    $${PWD}/OAIIoTSecurityAggregatedAlert.h \
    $${PWD}/OAIIoTSecurityAggregatedAlertList.h \
    $${PWD}/OAIIoTSecurityAggregatedAlertProperties.h \
    $${PWD}/OAIIoTSecurityAggregatedAlertProperties_topDevicesList_inner.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendation.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationList.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationProperties.h \
    $${PWD}/OAIIoTSecurityAlertedDevice.h \
    $${PWD}/OAIIoTSecurityDeviceAlert.h \
    $${PWD}/OAIIoTSecurityDeviceRecommendation.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModel.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelList.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties_devicesMetrics_inner.h \
    $${PWD}/OAIIoTSeverityMetrics.h \
    $${PWD}/OAIIotSecuritySolutionAnalytics_List_default_response.h \
    $${PWD}/OAIIotSecuritySolutionAnalytics_List_default_response_error.h \
    $${PWD}/OAITagsResource.h \
# APIs
    $${PWD}/OAIAggregatedAlertApi.h \
    $${PWD}/OAIAggregatedRecommendationApi.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsApi.h \
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
    $${PWD}/OAIIoTSecurityAggregatedAlert.cpp \
    $${PWD}/OAIIoTSecurityAggregatedAlertList.cpp \
    $${PWD}/OAIIoTSecurityAggregatedAlertProperties.cpp \
    $${PWD}/OAIIoTSecurityAggregatedAlertProperties_topDevicesList_inner.cpp \
    $${PWD}/OAIIoTSecurityAggregatedRecommendation.cpp \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationList.cpp \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationProperties.cpp \
    $${PWD}/OAIIoTSecurityAlertedDevice.cpp \
    $${PWD}/OAIIoTSecurityDeviceAlert.cpp \
    $${PWD}/OAIIoTSecurityDeviceRecommendation.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModel.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelList.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties_devicesMetrics_inner.cpp \
    $${PWD}/OAIIoTSeverityMetrics.cpp \
    $${PWD}/OAIIotSecuritySolutionAnalytics_List_default_response.cpp \
    $${PWD}/OAIIotSecuritySolutionAnalytics_List_default_response_error.cpp \
    $${PWD}/OAITagsResource.cpp \
# APIs
    $${PWD}/OAIAggregatedAlertApi.cpp \
    $${PWD}/OAIAggregatedRecommendationApi.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
