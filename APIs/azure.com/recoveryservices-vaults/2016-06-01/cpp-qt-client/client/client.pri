QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityParameters.h \
    $${PWD}/OAICheckNameAvailabilityResult.h \
    $${PWD}/OAICheckNameAvailabilityResultResource.h \
    $${PWD}/OAIClientDiscoveryDisplay.h \
    $${PWD}/OAIClientDiscoveryForLogSpecification.h \
    $${PWD}/OAIClientDiscoveryForProperties.h \
    $${PWD}/OAIClientDiscoveryForServiceSpecification.h \
    $${PWD}/OAIClientDiscoveryResponse.h \
    $${PWD}/OAIClientDiscoveryValueForSingleApi.h \
    $${PWD}/OAIPatchTrackedResource.h \
    $${PWD}/OAIPatchVault.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAIUpgradeDetails.h \
    $${PWD}/OAIVault.h \
    $${PWD}/OAIVaultExtendedInfo.h \
    $${PWD}/OAIVaultExtendedInfoResource.h \
    $${PWD}/OAIVaultList.h \
    $${PWD}/OAIVaultProperties.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIRecoveryServicesApi.h \
    $${PWD}/OAIVaultExtendedInfoApi.h \
    $${PWD}/OAIVaultsApi.h \
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
    $${PWD}/OAICheckNameAvailabilityParameters.cpp \
    $${PWD}/OAICheckNameAvailabilityResult.cpp \
    $${PWD}/OAICheckNameAvailabilityResultResource.cpp \
    $${PWD}/OAIClientDiscoveryDisplay.cpp \
    $${PWD}/OAIClientDiscoveryForLogSpecification.cpp \
    $${PWD}/OAIClientDiscoveryForProperties.cpp \
    $${PWD}/OAIClientDiscoveryForServiceSpecification.cpp \
    $${PWD}/OAIClientDiscoveryResponse.cpp \
    $${PWD}/OAIClientDiscoveryValueForSingleApi.cpp \
    $${PWD}/OAIPatchTrackedResource.cpp \
    $${PWD}/OAIPatchVault.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAIUpgradeDetails.cpp \
    $${PWD}/OAIVault.cpp \
    $${PWD}/OAIVaultExtendedInfo.cpp \
    $${PWD}/OAIVaultExtendedInfoResource.cpp \
    $${PWD}/OAIVaultList.cpp \
    $${PWD}/OAIVaultProperties.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIRecoveryServicesApi.cpp \
    $${PWD}/OAIVaultExtendedInfoApi.cpp \
    $${PWD}/OAIVaultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
