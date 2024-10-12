QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudKmsInventoryV1ListCryptoKeysResponse.h \
    $${PWD}/OAIGoogleCloudKmsInventoryV1ProtectedResource.h \
    $${PWD}/OAIGoogleCloudKmsInventoryV1ProtectedResourcesSummary.h \
    $${PWD}/OAIGoogleCloudKmsInventoryV1SearchProtectedResourcesResponse.h \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKey.h \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKeyVersion.h \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKeyVersionTemplate.h \
    $${PWD}/OAIGoogleCloudKmsV1ExternalProtectionLevelOptions.h \
    $${PWD}/OAIGoogleCloudKmsV1KeyOperationAttestation.h \
    $${PWD}/OAIGoogleCloudKmsV1KeyOperationAttestationCertificateChains.h \
# APIs
    $${PWD}/OAIOrganizationsApi.h \
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleCloudKmsInventoryV1ListCryptoKeysResponse.cpp \
    $${PWD}/OAIGoogleCloudKmsInventoryV1ProtectedResource.cpp \
    $${PWD}/OAIGoogleCloudKmsInventoryV1ProtectedResourcesSummary.cpp \
    $${PWD}/OAIGoogleCloudKmsInventoryV1SearchProtectedResourcesResponse.cpp \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKey.cpp \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKeyVersion.cpp \
    $${PWD}/OAIGoogleCloudKmsV1CryptoKeyVersionTemplate.cpp \
    $${PWD}/OAIGoogleCloudKmsV1ExternalProtectionLevelOptions.cpp \
    $${PWD}/OAIGoogleCloudKmsV1KeyOperationAttestation.cpp \
    $${PWD}/OAIGoogleCloudKmsV1KeyOperationAttestationCertificateChains.cpp \
# APIs
    $${PWD}/OAIOrganizationsApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
