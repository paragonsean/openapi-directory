QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIApiFailureResponse.h \
    $${PWD}/OAIAzureMetricsBaseData.h \
    $${PWD}/OAIAzureMetricsData.h \
    $${PWD}/OAIAzureMetricsDocument.h \
    $${PWD}/OAIAzureMetricsResult.h \
    $${PWD}/OAIAzureTimeSeriesData.h \
# APIs
    $${PWD}/OAIMetricsApi.h \
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
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIApiFailureResponse.cpp \
    $${PWD}/OAIAzureMetricsBaseData.cpp \
    $${PWD}/OAIAzureMetricsData.cpp \
    $${PWD}/OAIAzureMetricsDocument.cpp \
    $${PWD}/OAIAzureMetricsResult.cpp \
    $${PWD}/OAIAzureTimeSeriesData.cpp \
# APIs
    $${PWD}/OAIMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
