QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataPoint.h \
    $${PWD}/OAIForecast.h \
    $${PWD}/OAIQueryForecastRequest.h \
    $${PWD}/OAIQueryForecastResponse.h \
    $${PWD}/OAIQueryForecastResponse_Forecast.h \
    $${PWD}/OAIQueryWhatIfForecastRequest.h \
    $${PWD}/OAIQueryWhatIfForecastResponse.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIDataPoint.cpp \
    $${PWD}/OAIForecast.cpp \
    $${PWD}/OAIQueryForecastRequest.cpp \
    $${PWD}/OAIQueryForecastResponse.cpp \
    $${PWD}/OAIQueryForecastResponse_Forecast.cpp \
    $${PWD}/OAIQueryWhatIfForecastRequest.cpp \
    $${PWD}/OAIQueryWhatIfForecastResponse.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
