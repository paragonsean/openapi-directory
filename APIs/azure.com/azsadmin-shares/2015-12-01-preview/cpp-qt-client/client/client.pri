QT += network

HEADERS += \
# Models
    $${PWD}/OAIShare.h \
    $${PWD}/OAIShareProperties.h \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response.h \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner_name.h \
    $${PWD}/OAIShares_ListMetrics_200_response.h \
    $${PWD}/OAIShares_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAIShares_ListMetrics_200_response_value_inner_metricValues_inner.h \
# APIs
    $${PWD}/OAISharesApi.h \
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
    $${PWD}/OAIShare.cpp \
    $${PWD}/OAIShareProperties.cpp \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAIShares_ListMetricDefinitions_200_response_value_inner_name.cpp \
    $${PWD}/OAIShares_ListMetrics_200_response.cpp \
    $${PWD}/OAIShares_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAIShares_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
# APIs
    $${PWD}/OAISharesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
