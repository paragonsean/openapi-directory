QT += network

HEADERS += \
# Models
    $${PWD}/OAIQueueService.h \
    $${PWD}/OAIQueueServiceProperties.h \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response.h \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner_name.h \
    $${PWD}/OAIQueueServices_ListMetrics_200_response.h \
    $${PWD}/OAIQueueServices_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAIQueueServices_ListMetrics_200_response_value_inner_metricValues_inner.h \
# APIs
    $${PWD}/OAIQueueServicesApi.h \
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
    $${PWD}/OAIQueueService.cpp \
    $${PWD}/OAIQueueServiceProperties.cpp \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAIQueueServices_ListMetricDefinitions_200_response_value_inner_name.cpp \
    $${PWD}/OAIQueueServices_ListMetrics_200_response.cpp \
    $${PWD}/OAIQueueServices_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAIQueueServices_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
# APIs
    $${PWD}/OAIQueueServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
