QT += network

HEADERS += \
# Models
    $${PWD}/OAIEditionCapability.h \
    $${PWD}/OAIElasticPoolDtuCapability.h \
    $${PWD}/OAIElasticPoolEditionCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMaxDtuCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMinDtuCapability.h \
    $${PWD}/OAILocationCapabilities.h \
    $${PWD}/OAIMaxSizeCapability.h \
    $${PWD}/OAIPerformanceLevelCapability.h \
    $${PWD}/OAIServerVersionCapability.h \
    $${PWD}/OAIServiceLevelObjectiveCapability.h \
# APIs
    $${PWD}/OAILocationCapabilitiesApi.h \
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
    $${PWD}/OAIEditionCapability.cpp \
    $${PWD}/OAIElasticPoolDtuCapability.cpp \
    $${PWD}/OAIElasticPoolEditionCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMaxDtuCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMinDtuCapability.cpp \
    $${PWD}/OAILocationCapabilities.cpp \
    $${PWD}/OAIMaxSizeCapability.cpp \
    $${PWD}/OAIPerformanceLevelCapability.cpp \
    $${PWD}/OAIServerVersionCapability.cpp \
    $${PWD}/OAIServiceLevelObjectiveCapability.cpp \
# APIs
    $${PWD}/OAILocationCapabilitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
