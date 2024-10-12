QT += network

HEADERS += \
# Models
    $${PWD}/OAIEditionCapability.h \
    $${PWD}/OAIElasticPoolEditionCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMaxPerformanceLevelCapability.h \
    $${PWD}/OAIElasticPoolPerDatabaseMinPerformanceLevelCapability.h \
    $${PWD}/OAIElasticPoolPerformanceLevelCapability.h \
    $${PWD}/OAIElasticPoolPerformanceLevelCapability_sku.h \
    $${PWD}/OAILicenseTypeCapability.h \
    $${PWD}/OAILocationCapabilities.h \
    $${PWD}/OAILogSizeCapability.h \
    $${PWD}/OAIManagedInstanceEditionCapability.h \
    $${PWD}/OAIManagedInstanceFamilyCapability.h \
    $${PWD}/OAIManagedInstanceVcoresCapability.h \
    $${PWD}/OAIManagedInstanceVersionCapability.h \
    $${PWD}/OAIMaxSizeCapability.h \
    $${PWD}/OAIMaxSizeRangeCapability.h \
    $${PWD}/OAIPerformanceLevelCapability.h \
    $${PWD}/OAIServerVersionCapability.h \
    $${PWD}/OAIServiceObjectiveCapability.h \
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
    $${PWD}/OAIElasticPoolEditionCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMaxPerformanceLevelCapability.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseMinPerformanceLevelCapability.cpp \
    $${PWD}/OAIElasticPoolPerformanceLevelCapability.cpp \
    $${PWD}/OAIElasticPoolPerformanceLevelCapability_sku.cpp \
    $${PWD}/OAILicenseTypeCapability.cpp \
    $${PWD}/OAILocationCapabilities.cpp \
    $${PWD}/OAILogSizeCapability.cpp \
    $${PWD}/OAIManagedInstanceEditionCapability.cpp \
    $${PWD}/OAIManagedInstanceFamilyCapability.cpp \
    $${PWD}/OAIManagedInstanceVcoresCapability.cpp \
    $${PWD}/OAIManagedInstanceVersionCapability.cpp \
    $${PWD}/OAIMaxSizeCapability.cpp \
    $${PWD}/OAIMaxSizeRangeCapability.cpp \
    $${PWD}/OAIPerformanceLevelCapability.cpp \
    $${PWD}/OAIServerVersionCapability.cpp \
    $${PWD}/OAIServiceObjectiveCapability.cpp \
# APIs
    $${PWD}/OAILocationCapabilitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
