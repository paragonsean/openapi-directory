QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIHistoricalWeatherApi.h \
    $${PWD}/OAITimelineWeatherAPI15DayForecastRequestApi.h \
    $${PWD}/OAITimelineWeatherAPIDateRangeRequestApi.h \
    $${PWD}/OAITimelineWeatherAPISingleDateRequestApi.h \
    $${PWD}/OAIWeatherForecastApi.h \
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
# APIs
    $${PWD}/OAIHistoricalWeatherApi.cpp \
    $${PWD}/OAITimelineWeatherAPI15DayForecastRequestApi.cpp \
    $${PWD}/OAITimelineWeatherAPIDateRangeRequestApi.cpp \
    $${PWD}/OAITimelineWeatherAPISingleDateRequestApi.cpp \
    $${PWD}/OAIWeatherForecastApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
