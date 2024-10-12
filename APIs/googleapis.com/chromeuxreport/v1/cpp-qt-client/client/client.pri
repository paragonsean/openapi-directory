QT += network

HEADERS += \
# Models
    $${PWD}/OAIBin.h \
    $${PWD}/OAICollectionPeriod.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIFractionTimeseries.h \
    $${PWD}/OAIHistoryKey.h \
    $${PWD}/OAIHistoryRecord.h \
    $${PWD}/OAIKey.h \
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricTimeseries.h \
    $${PWD}/OAIPercentiles.h \
    $${PWD}/OAIQueryHistoryRequest.h \
    $${PWD}/OAIQueryHistoryResponse.h \
    $${PWD}/OAIQueryRequest.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIRecord.h \
    $${PWD}/OAITimeseriesBin.h \
    $${PWD}/OAITimeseriesPercentiles.h \
    $${PWD}/OAIUrlNormalization.h \
# APIs
    $${PWD}/OAIRecordsApi.h \
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
    $${PWD}/OAIBin.cpp \
    $${PWD}/OAICollectionPeriod.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIFractionTimeseries.cpp \
    $${PWD}/OAIHistoryKey.cpp \
    $${PWD}/OAIHistoryRecord.cpp \
    $${PWD}/OAIKey.cpp \
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricTimeseries.cpp \
    $${PWD}/OAIPercentiles.cpp \
    $${PWD}/OAIQueryHistoryRequest.cpp \
    $${PWD}/OAIQueryHistoryResponse.cpp \
    $${PWD}/OAIQueryRequest.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIRecord.cpp \
    $${PWD}/OAITimeseriesBin.cpp \
    $${PWD}/OAITimeseriesPercentiles.cpp \
    $${PWD}/OAIUrlNormalization.cpp \
# APIs
    $${PWD}/OAIRecordsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
