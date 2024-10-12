QT += network

HEADERS += \
# Models
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIPlanList.h \
    $${PWD}/OAIPlanProperties.h \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response.h \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAIPlans_ListMetrics_200_response.h \
    $${PWD}/OAIPlans_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAIPlans_ListMetrics_200_response_value_inner_metricValues_inner.h \
# APIs
    $${PWD}/OAIPlansApi.h \
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
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIPlanList.cpp \
    $${PWD}/OAIPlanProperties.cpp \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAIPlans_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAIPlans_ListMetrics_200_response.cpp \
    $${PWD}/OAIPlans_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAIPlans_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
# APIs
    $${PWD}/OAIPlansApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
