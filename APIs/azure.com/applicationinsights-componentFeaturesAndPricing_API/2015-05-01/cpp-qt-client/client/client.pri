QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationInsightsComponentAvailableFeatures.h \
    $${PWD}/OAIApplicationInsightsComponentBillingFeatures.h \
    $${PWD}/OAIApplicationInsightsComponentDataVolumeCap.h \
    $${PWD}/OAIApplicationInsightsComponentFeature.h \
    $${PWD}/OAIApplicationInsightsComponentFeatureCapabilities.h \
    $${PWD}/OAIApplicationInsightsComponentFeatureCapability.h \
    $${PWD}/OAIApplicationInsightsComponentQuotaStatus.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIApplicationInsightsComponentAvailableFeatures.cpp \
    $${PWD}/OAIApplicationInsightsComponentBillingFeatures.cpp \
    $${PWD}/OAIApplicationInsightsComponentDataVolumeCap.cpp \
    $${PWD}/OAIApplicationInsightsComponentFeature.cpp \
    $${PWD}/OAIApplicationInsightsComponentFeatureCapabilities.cpp \
    $${PWD}/OAIApplicationInsightsComponentFeatureCapability.cpp \
    $${PWD}/OAIApplicationInsightsComponentQuotaStatus.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
