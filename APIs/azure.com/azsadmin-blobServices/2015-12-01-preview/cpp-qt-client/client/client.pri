QT += network

HEADERS += \
# Models
    $${PWD}/OAIBlobService.h \
    $${PWD}/OAIBlobServiceProperties.h \
    $${PWD}/OAIBlobServiceSettings.h \
    $${PWD}/OAIBlobServiceWritableSettings.h \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response.h \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner_name.h \
    $${PWD}/OAIBlobServices_ListMetrics_200_response.h \
    $${PWD}/OAIBlobServices_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAIBlobServices_ListMetrics_200_response_value_inner_metricValues_inner.h \
# APIs
    $${PWD}/OAIBlobServicesApi.h \
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
    $${PWD}/OAIBlobService.cpp \
    $${PWD}/OAIBlobServiceProperties.cpp \
    $${PWD}/OAIBlobServiceSettings.cpp \
    $${PWD}/OAIBlobServiceWritableSettings.cpp \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAIBlobServices_ListMetricDefinitions_200_response_value_inner_name.cpp \
    $${PWD}/OAIBlobServices_ListMetrics_200_response.cpp \
    $${PWD}/OAIBlobServices_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAIBlobServices_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
# APIs
    $${PWD}/OAIBlobServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
