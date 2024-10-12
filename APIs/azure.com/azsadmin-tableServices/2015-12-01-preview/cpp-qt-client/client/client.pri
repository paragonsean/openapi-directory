QT += network

HEADERS += \
# Models
    $${PWD}/OAITableService.h \
    $${PWD}/OAITableServiceProperties.h \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response.h \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner_name.h \
    $${PWD}/OAITableServices_ListMetrics_200_response.h \
    $${PWD}/OAITableServices_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAITableServices_ListMetrics_200_response_value_inner_metricValues_inner.h \
# APIs
    $${PWD}/OAITableServicesApi.h \
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
    $${PWD}/OAITableService.cpp \
    $${PWD}/OAITableServiceProperties.cpp \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAITableServices_ListMetricDefinitions_200_response_value_inner_name.cpp \
    $${PWD}/OAITableServices_ListMetrics_200_response.cpp \
    $${PWD}/OAITableServices_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAITableServices_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
# APIs
    $${PWD}/OAITableServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
