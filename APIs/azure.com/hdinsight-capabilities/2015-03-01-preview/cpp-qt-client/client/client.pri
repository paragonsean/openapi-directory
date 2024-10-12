QT += network

HEADERS += \
# Models
    $${PWD}/OAICapabilitiesResult.h \
    $${PWD}/OAIQuotaCapability.h \
    $${PWD}/OAIRegionalQuotaCapability.h \
    $${PWD}/OAIRegionsCapability.h \
    $${PWD}/OAIVersionSpec.h \
    $${PWD}/OAIVersionsCapability.h \
    $${PWD}/OAIVmSizeCompatibilityFilter.h \
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
    $${PWD}/OAICapabilitiesResult.cpp \
    $${PWD}/OAIQuotaCapability.cpp \
    $${PWD}/OAIRegionalQuotaCapability.cpp \
    $${PWD}/OAIRegionsCapability.cpp \
    $${PWD}/OAIVersionSpec.cpp \
    $${PWD}/OAIVersionsCapability.cpp \
    $${PWD}/OAIVmSizeCompatibilityFilter.cpp \
    $${PWD}/OAIVmSizesCapability.cpp \
# APIs
    $${PWD}/OAIRegionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
