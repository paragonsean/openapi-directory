QT += network

HEADERS += \
# Models
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricAvailability.h \
    $${PWD}/OAIMetricDefinition.h \
    $${PWD}/OAIMetricDefinitionListResult.h \
    $${PWD}/OAIMetricListResult.h \
    $${PWD}/OAIMetricName.h \
    $${PWD}/OAIMetricValue.h \
# APIs
    $${PWD}/OAIDatabasesApi.h \
    $${PWD}/OAIElasticPoolsApi.h \
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
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricAvailability.cpp \
    $${PWD}/OAIMetricDefinition.cpp \
    $${PWD}/OAIMetricDefinitionListResult.cpp \
    $${PWD}/OAIMetricListResult.cpp \
    $${PWD}/OAIMetricName.cpp \
    $${PWD}/OAIMetricValue.cpp \
# APIs
    $${PWD}/OAIDatabasesApi.cpp \
    $${PWD}/OAIElasticPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
