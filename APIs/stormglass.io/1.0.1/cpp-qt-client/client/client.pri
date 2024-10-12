QT += network

HEADERS += \
# Models
    $${PWD}/OAIForecast.h \
    $${PWD}/OAIForecast_hours_inner.h \
    $${PWD}/OAIForecast_hours_inner_airTemperature_inner.h \
    $${PWD}/OAIForecast_hours_inner_swellDirection_inner.h \
    $${PWD}/OAIForecast_hours_inner_swellHeight_inner.h \
    $${PWD}/OAIForecast_hours_inner_swellPeriod_inner.h \
    $${PWD}/OAIForecast_hours_inner_waterTemperature_inner.h \
    $${PWD}/OAIForecast_hours_inner_waveDirection_inner.h \
    $${PWD}/OAIForecast_hours_inner_waveHeight_inner.h \
    $${PWD}/OAIForecast_hours_inner_wavePeriod_inner.h \
    $${PWD}/OAIForecast_hours_inner_windDirection_inner.h \
    $${PWD}/OAIForecast_hours_inner_windSpeed_inner.h \
    $${PWD}/OAIForecast_meta.h \
# APIs
    $${PWD}/OAIForecastApi.h \
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
    $${PWD}/OAIForecast.cpp \
    $${PWD}/OAIForecast_hours_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_airTemperature_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_swellDirection_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_swellHeight_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_swellPeriod_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_waterTemperature_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_waveDirection_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_waveHeight_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_wavePeriod_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_windDirection_inner.cpp \
    $${PWD}/OAIForecast_hours_inner_windSpeed_inner.cpp \
    $${PWD}/OAIForecast_meta.cpp \
# APIs
    $${PWD}/OAIForecastApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
