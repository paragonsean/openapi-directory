QT += network

HEADERS += \
# Models
    $${PWD}/OAIBillingMeters.h \
    $${PWD}/OAIBillingResources.h \
    $${PWD}/OAIBillingResponseListResult.h \
    $${PWD}/OAICapabilitiesResult.h \
    $${PWD}/OAIDiskBillingMeters.h \
    $${PWD}/OAILocalizedName.h \
    $${PWD}/OAILocations_ListBillingSpecs_default_response.h \
    $${PWD}/OAIQuotaCapability.h \
    $${PWD}/OAIRegionalQuotaCapability.h \
    $${PWD}/OAIRegionsCapability.h \
    $${PWD}/OAIUsage.h \
    $${PWD}/OAIUsagesListResult.h \
    $${PWD}/OAIVersionSpec.h \
    $${PWD}/OAIVersionsCapability.h \
    $${PWD}/OAIVmSizeCompatibilityFilter.h \
    $${PWD}/OAIVmSizeCompatibilityFilterV2.h \
    $${PWD}/OAIVmSizesCapability.h \
# APIs
    $${PWD}/OAIRegionsApi.h \
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
    $${PWD}/OAIBillingMeters.cpp \
    $${PWD}/OAIBillingResources.cpp \
    $${PWD}/OAIBillingResponseListResult.cpp \
    $${PWD}/OAICapabilitiesResult.cpp \
    $${PWD}/OAIDiskBillingMeters.cpp \
    $${PWD}/OAILocalizedName.cpp \
    $${PWD}/OAILocations_ListBillingSpecs_default_response.cpp \
    $${PWD}/OAIQuotaCapability.cpp \
    $${PWD}/OAIRegionalQuotaCapability.cpp \
    $${PWD}/OAIRegionsCapability.cpp \
    $${PWD}/OAIUsage.cpp \
    $${PWD}/OAIUsagesListResult.cpp \
    $${PWD}/OAIVersionSpec.cpp \
    $${PWD}/OAIVersionsCapability.cpp \
    $${PWD}/OAIVmSizeCompatibilityFilter.cpp \
    $${PWD}/OAIVmSizeCompatibilityFilterV2.cpp \
    $${PWD}/OAIVmSizesCapability.cpp \
# APIs
    $${PWD}/OAIRegionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
