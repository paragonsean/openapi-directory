QT += network

HEADERS += \
# Models
    $${PWD}/OAICapabilityStatus.h \
    $${PWD}/OAIEditionCapability.h \
    $${PWD}/OAIElasticPoolDtuCapability.h \
    $${PWD}/OAIElasticPoolEditionCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMaxDtuCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMinDtuCapability.h \
    $${PWD}/OAILocationCapabilities.h \
    $${PWD}/OAIMaxSizeCapability.h \
    $${PWD}/OAIPerformanceLevel.h \
    $${PWD}/OAIServerVersionCapability.h \
    $${PWD}/OAIServiceObjectiveCapability.h \
# APIs
    $${PWD}/OAICapabilitiesApi.h \
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
    $${PWD}/OAICapabilityStatus.cpp \
    $${PWD}/OAIEditionCapability.cpp \
    $${PWD}/OAIElasticPoolDtuCapability.cpp \
    $${PWD}/OAIElasticPoolEditionCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMaxDtuCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMinDtuCapability.cpp \
    $${PWD}/OAILocationCapabilities.cpp \
    $${PWD}/OAIMaxSizeCapability.cpp \
    $${PWD}/OAIPerformanceLevel.cpp \
    $${PWD}/OAIServerVersionCapability.cpp \
    $${PWD}/OAIServiceObjectiveCapability.cpp \
# APIs
    $${PWD}/OAICapabilitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
