QT += network

HEADERS += \
# Models
    $${PWD}/OAIDailyMetricTimeSeries.h \
    $${PWD}/OAIDailySubEntityType.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIDatedValue.h \
    $${PWD}/OAIFetchMultiDailyMetricsTimeSeriesResponse.h \
    $${PWD}/OAIGetDailyMetricsTimeSeriesResponse.h \
    $${PWD}/OAIInsightsValue.h \
    $${PWD}/OAIListSearchKeywordImpressionsMonthlyResponse.h \
    $${PWD}/OAIMultiDailyMetricTimeSeries.h \
    $${PWD}/OAISearchKeywordCount.h \
    $${PWD}/OAITimeOfDay.h \
    $${PWD}/OAITimeSeries.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIDailyMetricTimeSeries.cpp \
    $${PWD}/OAIDailySubEntityType.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIDatedValue.cpp \
    $${PWD}/OAIFetchMultiDailyMetricsTimeSeriesResponse.cpp \
    $${PWD}/OAIGetDailyMetricsTimeSeriesResponse.cpp \
    $${PWD}/OAIInsightsValue.cpp \
    $${PWD}/OAIListSearchKeywordImpressionsMonthlyResponse.cpp \
    $${PWD}/OAIMultiDailyMetricTimeSeries.cpp \
    $${PWD}/OAISearchKeywordCount.cpp \
    $${PWD}/OAITimeOfDay.cpp \
    $${PWD}/OAITimeSeries.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
