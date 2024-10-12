QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIError_Source.h \
    $${PWD}/OAIGet_itinerary_price_metrics_200_response.h \
    $${PWD}/OAIItinerary_price_metric.h \
    $${PWD}/OAIItinerary_price_metric_priceMetrics_inner.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIWarning.h \
    $${PWD}/OAIWarning_Source.h \
# APIs
    $${PWD}/OAIPriceMetricsApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIError_Source.cpp \
    $${PWD}/OAIGet_itinerary_price_metrics_200_response.cpp \
    $${PWD}/OAIItinerary_price_metric.cpp \
    $${PWD}/OAIItinerary_price_metric_priceMetrics_inner.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIWarning.cpp \
    $${PWD}/OAIWarning_Source.cpp \
# APIs
    $${PWD}/OAIPriceMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
