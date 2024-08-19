QT += network

HEADERS += \
# Models
    $${PWD}/OAIAggregateMetrics.h \
    $${PWD}/OAIBusinessCallsInsights.h \
    $${PWD}/OAIBusinessCallsSettings.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIHourlyMetrics.h \
    $${PWD}/OAIListBusinessCallsInsightsResponse.h \
    $${PWD}/OAIWeekDayMetrics.h \
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
    $${PWD}/OAIAggregateMetrics.cpp \
    $${PWD}/OAIBusinessCallsInsights.cpp \
    $${PWD}/OAIBusinessCallsSettings.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIHourlyMetrics.cpp \
    $${PWD}/OAIListBusinessCallsInsightsResponse.cpp \
    $${PWD}/OAIWeekDayMetrics.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
