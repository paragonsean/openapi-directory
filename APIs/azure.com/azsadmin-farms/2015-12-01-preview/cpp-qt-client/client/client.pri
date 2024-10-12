QT += network

HEADERS += \
# Models
    $${PWD}/OAIFarm.h \
    $${PWD}/OAIFarmCreationProperties.h \
    $${PWD}/OAIFarmList.h \
    $${PWD}/OAIFarmProperties.h \
    $${PWD}/OAIFarmSettings.h \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response.h \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner.h \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.h \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner_name.h \
    $${PWD}/OAIFarms_ListMetrics_200_response.h \
    $${PWD}/OAIFarms_ListMetrics_200_response_value_inner.h \
    $${PWD}/OAIFarms_ListMetrics_200_response_value_inner_metricValues_inner.h \
    $${PWD}/OAISettingAccessString.h \
# APIs
    $${PWD}/OAIFarmsApi.h \
    $${PWD}/OAIGCApi.h \
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
    $${PWD}/OAIFarm.cpp \
    $${PWD}/OAIFarmCreationProperties.cpp \
    $${PWD}/OAIFarmList.cpp \
    $${PWD}/OAIFarmProperties.cpp \
    $${PWD}/OAIFarmSettings.cpp \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response.cpp \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner.cpp \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner_metricAvailabilities_inner.cpp \
    $${PWD}/OAIFarms_ListMetricDefinitions_200_response_value_inner_name.cpp \
    $${PWD}/OAIFarms_ListMetrics_200_response.cpp \
    $${PWD}/OAIFarms_ListMetrics_200_response_value_inner.cpp \
    $${PWD}/OAIFarms_ListMetrics_200_response_value_inner_metricValues_inner.cpp \
    $${PWD}/OAISettingAccessString.cpp \
# APIs
    $${PWD}/OAIFarmsApi.cpp \
    $${PWD}/OAIGCApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
