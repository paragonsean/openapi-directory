QT += network

HEADERS += \
# Models
    $${PWD}/OAIIoTSecurityAggregatedAlert.h \
    $${PWD}/OAIIoTSecurityAggregatedAlertList.h \
    $${PWD}/OAIIoTSecurityAggregatedAlertProperties.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendation.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationList.h \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationProperties.h \
    $${PWD}/OAIIoTSecurityAlertedDevice.h \
    $${PWD}/OAIIoTSecurityAlertedDevicesList.h \
    $${PWD}/OAIIoTSecurityDeviceAlert.h \
    $${PWD}/OAIIoTSecurityDeviceAlertsList.h \
    $${PWD}/OAIIoTSecurityDeviceRecommendation.h \
    $${PWD}/OAIIoTSecurityDeviceRecommendationsList.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModel.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelList.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties.h \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties_devicesMetrics_inner.h \
    $${PWD}/OAIIoTSecuritySolutionsAnalytics_GetAll_default_response.h \
    $${PWD}/OAIIoTSecuritySolutionsAnalytics_GetAll_default_response_error.h \
    $${PWD}/OAIIoTSeverityMetrics.h \
    $${PWD}/OAITagsResource.h \
# APIs
    $${PWD}/OAIIoTSecuritySolutionsAnalyticsApi.h \
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
    $${PWD}/OAIIoTSecurityAggregatedRecommendation.cpp \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationList.cpp \
    $${PWD}/OAIIoTSecurityAggregatedRecommendationProperties.cpp \
    $${PWD}/OAIIoTSecurityAlertedDevice.cpp \
    $${PWD}/OAIIoTSecurityAlertedDevicesList.cpp \
    $${PWD}/OAIIoTSecurityDeviceAlert.cpp \
    $${PWD}/OAIIoTSecurityDeviceAlertsList.cpp \
    $${PWD}/OAIIoTSecurityDeviceRecommendation.cpp \
    $${PWD}/OAIIoTSecurityDeviceRecommendationsList.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModel.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelList.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties.cpp \
    $${PWD}/OAIIoTSecuritySolutionAnalyticsModelProperties_devicesMetrics_inner.cpp \
    $${PWD}/OAIIoTSecuritySolutionsAnalytics_GetAll_default_response.cpp \
    $${PWD}/OAIIoTSecuritySolutionsAnalytics_GetAll_default_response_error.cpp \
    $${PWD}/OAIIoTSeverityMetrics.cpp \
    $${PWD}/OAITagsResource.cpp \
# APIs
    $${PWD}/OAIIoTSecuritySolutionsAnalyticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
