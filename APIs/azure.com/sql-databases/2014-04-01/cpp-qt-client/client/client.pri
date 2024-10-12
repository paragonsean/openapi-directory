QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabase.h \
    $${PWD}/OAIDatabaseListResult.h \
    $${PWD}/OAIDatabaseProperties.h \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner.h \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner_properties.h \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner_properties_estimatedImpact_inner.h \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner.h \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner_properties.h \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner_properties_serviceLevelObjectiveUsageMetrics_inner.h \
    $${PWD}/OAIDatabaseProperties_transparentDataEncryption_inner.h \
    $${PWD}/OAIDatabaseProperties_transparentDataEncryption_inner_properties.h \
    $${PWD}/OAIDatabaseUpdate.h \
# APIs
    $${PWD}/OAIDatabaseActivationApi.h \
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
    $${PWD}/OAIDatabase.cpp \
    $${PWD}/OAIDatabaseListResult.cpp \
    $${PWD}/OAIDatabaseProperties.cpp \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner.cpp \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner_properties.cpp \
    $${PWD}/OAIDatabaseProperties_recommendedIndex_inner_properties_estimatedImpact_inner.cpp \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner.cpp \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner_properties.cpp \
    $${PWD}/OAIDatabaseProperties_serviceTierAdvisors_inner_properties_serviceLevelObjectiveUsageMetrics_inner.cpp \
    $${PWD}/OAIDatabaseProperties_transparentDataEncryption_inner.cpp \
    $${PWD}/OAIDatabaseProperties_transparentDataEncryption_inner_properties.cpp \
    $${PWD}/OAIDatabaseUpdate.cpp \
# APIs
    $${PWD}/OAIDatabaseActivationApi.cpp \
    $${PWD}/OAIDatabasesApi.cpp \
    $${PWD}/OAIElasticPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
