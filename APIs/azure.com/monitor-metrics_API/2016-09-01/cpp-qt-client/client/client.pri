QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILocalizableString.h \
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricCollection.h \
    $${PWD}/OAIMetricValue.h \
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
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricCollection.cpp \
    $${PWD}/OAIMetricValue.cpp \
    $${PWD}/OAIUnit.cpp \
# APIs
    $${PWD}/OAIMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
