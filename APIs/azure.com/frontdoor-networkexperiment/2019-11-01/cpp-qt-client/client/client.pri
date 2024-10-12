QT += network

HEADERS += \
# Models
    $${PWD}/OAIEndpoint.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIExperiment.h \
    $${PWD}/OAIExperimentList.h \
    $${PWD}/OAIExperimentProperties.h \
    $${PWD}/OAIExperimentUpdateModel.h \
    $${PWD}/OAIExperimentUpdateProperties.h \
    $${PWD}/OAILatencyMetric.h \
    $${PWD}/OAILatencyScorecard.h \
    $${PWD}/OAILatencyScorecardProperties.h \
    $${PWD}/OAINetworkExperimentResourceState.h \
    $${PWD}/OAIPreconfiguredEndpoint.h \
    $${PWD}/OAIPreconfiguredEndpointList.h \
    $${PWD}/OAIPreconfiguredEndpointProperties.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAIProfileList.h \
    $${PWD}/OAIProfileProperties.h \
    $${PWD}/OAIProfileUpdateModel.h \
    $${PWD}/OAIProfileUpdateProperties.h \
    $${PWD}/OAITimeseries.h \
    $${PWD}/OAITimeseriesDataPoint.h \
    $${PWD}/OAITimeseriesProperties.h \
# APIs
    $${PWD}/OAIExperimentsApi.h \
    $${PWD}/OAINetworkExperimentProfilesApi.h \
    $${PWD}/OAIPreconfiguredEndpointsApi.h \
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIEndpoint.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIExperiment.cpp \
    $${PWD}/OAIExperimentList.cpp \
    $${PWD}/OAIExperimentProperties.cpp \
    $${PWD}/OAIExperimentUpdateModel.cpp \
    $${PWD}/OAIExperimentUpdateProperties.cpp \
    $${PWD}/OAILatencyMetric.cpp \
    $${PWD}/OAILatencyScorecard.cpp \
    $${PWD}/OAILatencyScorecardProperties.cpp \
    $${PWD}/OAINetworkExperimentResourceState.cpp \
    $${PWD}/OAIPreconfiguredEndpoint.cpp \
    $${PWD}/OAIPreconfiguredEndpointList.cpp \
    $${PWD}/OAIPreconfiguredEndpointProperties.cpp \
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAIProfileList.cpp \
    $${PWD}/OAIProfileProperties.cpp \
    $${PWD}/OAIProfileUpdateModel.cpp \
    $${PWD}/OAIProfileUpdateProperties.cpp \
    $${PWD}/OAITimeseries.cpp \
    $${PWD}/OAITimeseriesDataPoint.cpp \
    $${PWD}/OAITimeseriesProperties.cpp \
# APIs
    $${PWD}/OAIExperimentsApi.cpp \
    $${PWD}/OAINetworkExperimentProfilesApi.cpp \
    $${PWD}/OAIPreconfiguredEndpointsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
