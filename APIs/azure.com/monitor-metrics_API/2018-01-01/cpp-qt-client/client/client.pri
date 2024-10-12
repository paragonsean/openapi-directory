QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILocalizableString.h \
    $${PWD}/OAIMetadataValue.h \
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricValue.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAITimeSeriesElement.h \
    $${PWD}/OAIUnit.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILocalizableString.cpp \
    $${PWD}/OAIMetadataValue.cpp \
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricValue.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAITimeSeriesElement.cpp \
    $${PWD}/OAIUnit.cpp \
# APIs
    $${PWD}/OAIMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
