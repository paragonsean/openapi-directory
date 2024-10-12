QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttestedData.h \
    $${PWD}/OAICompute.h \
    $${PWD}/OAIDataDisk.h \
    $${PWD}/OAIDiskImage.h \
    $${PWD}/OAIEncryptionSettings.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentityErrorResponse.h \
    $${PWD}/OAIIdentityInfoResponse.h \
    $${PWD}/OAIIdentityTokenResponse.h \
    $${PWD}/OAIImageReference.h \
    $${PWD}/OAIInstance.h \
    $${PWD}/OAIIpv4Properties.h \
    $${PWD}/OAIIpv6Properties.h \
    $${PWD}/OAIManagedDisk.h \
    $${PWD}/OAINetwork.h \
    $${PWD}/OAINetworkInterface.h \
    $${PWD}/OAINetworkInterface_ipv4.h \
    $${PWD}/OAINetworkInterface_ipv6.h \
    $${PWD}/OAIOsDisk.h \
    $${PWD}/OAIPlanProperties.h \
    $${PWD}/OAIPublicKeysProperties.h \
    $${PWD}/OAIStorageProfile.h \
    $${PWD}/OAISubnetProperties.h \
    $${PWD}/OAIVirtualHardDisk.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIGetMetadataInformationApi.h \
    $${PWD}/OAIGetTokenApi.h \
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
    $${PWD}/OAIAttestedData.cpp \
    $${PWD}/OAICompute.cpp \
    $${PWD}/OAIDataDisk.cpp \
    $${PWD}/OAIDiskImage.cpp \
    $${PWD}/OAIEncryptionSettings.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentityErrorResponse.cpp \
    $${PWD}/OAIIdentityInfoResponse.cpp \
    $${PWD}/OAIIdentityTokenResponse.cpp \
    $${PWD}/OAIImageReference.cpp \
    $${PWD}/OAIInstance.cpp \
    $${PWD}/OAIIpv4Properties.cpp \
    $${PWD}/OAIIpv6Properties.cpp \
    $${PWD}/OAIManagedDisk.cpp \
    $${PWD}/OAINetwork.cpp \
    $${PWD}/OAINetworkInterface.cpp \
    $${PWD}/OAINetworkInterface_ipv4.cpp \
    $${PWD}/OAINetworkInterface_ipv6.cpp \
    $${PWD}/OAIOsDisk.cpp \
    $${PWD}/OAIPlanProperties.cpp \
    $${PWD}/OAIPublicKeysProperties.cpp \
    $${PWD}/OAIStorageProfile.cpp \
    $${PWD}/OAISubnetProperties.cpp \
    $${PWD}/OAIVirtualHardDisk.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIGetMetadataInformationApi.cpp \
    $${PWD}/OAIGetTokenApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
