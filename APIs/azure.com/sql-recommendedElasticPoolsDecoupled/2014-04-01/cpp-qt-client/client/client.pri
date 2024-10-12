QT += network

HEADERS += \
# Models
    $${PWD}/OAIRecommendedElasticPool.h \
    $${PWD}/OAIRecommendedElasticPoolListMetricsResult.h \
    $${PWD}/OAIRecommendedElasticPoolListResult.h \
    $${PWD}/OAIRecommendedElasticPoolMetric.h \
    $${PWD}/OAIRecommendedElasticPoolProperties.h \
    $${PWD}/OAIRecommendedElasticPoolProperties_databases_inner.h \
# APIs
    $${PWD}/OAIRecommendedElasticPoolsApi.h \
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
    $${PWD}/OAIRecommendedElasticPool.cpp \
    $${PWD}/OAIRecommendedElasticPoolListMetricsResult.cpp \
    $${PWD}/OAIRecommendedElasticPoolListResult.cpp \
    $${PWD}/OAIRecommendedElasticPoolMetric.cpp \
    $${PWD}/OAIRecommendedElasticPoolProperties.cpp \
    $${PWD}/OAIRecommendedElasticPoolProperties_databases_inner.cpp \
# APIs
    $${PWD}/OAIRecommendedElasticPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
