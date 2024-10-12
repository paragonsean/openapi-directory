QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIDeleteOperationResult.h \
    $${PWD}/OAIHeatMapEndpoint.h \
    $${PWD}/OAIHeatMapModel.h \
    $${PWD}/OAIHeatMapProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIQueryExperience.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAITrafficFlow.h \
    $${PWD}/OAITrafficManagerUserMetricsKeyModel.h \
# APIs
    $${PWD}/OAIHeatMapsApi.h \
    $${PWD}/OAIRealUserMetricsApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIDeleteOperationResult.cpp \
    $${PWD}/OAIHeatMapEndpoint.cpp \
    $${PWD}/OAIHeatMapModel.cpp \
    $${PWD}/OAIHeatMapProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIQueryExperience.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAITrafficFlow.cpp \
    $${PWD}/OAITrafficManagerUserMetricsKeyModel.cpp \
# APIs
    $${PWD}/OAIHeatMapsApi.cpp \
    $${PWD}/OAIRealUserMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
