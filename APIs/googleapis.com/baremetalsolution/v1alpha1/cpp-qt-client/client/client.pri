QT += network

HEADERS += \
# Models
    $${PWD}/OAIInstanceConfig.h \
    $${PWD}/OAIInstanceQuota.h \
    $${PWD}/OAIListProvisioningQuotasResponse.h \
    $${PWD}/OAILunRange.h \
    $${PWD}/OAINetworkAddress.h \
    $${PWD}/OAINetworkConfig.h \
    $${PWD}/OAINfsExport.h \
    $${PWD}/OAIProvisioningConfig.h \
    $${PWD}/OAIProvisioningQuota.h \
    $${PWD}/OAISubmitProvisioningConfigRequest.h \
    $${PWD}/OAIVlanAttachment.h \
    $${PWD}/OAIVolumeConfig.h \
# APIs
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
    $${PWD}/OAIInstanceConfig.cpp \
    $${PWD}/OAIInstanceQuota.cpp \
    $${PWD}/OAIListProvisioningQuotasResponse.cpp \
    $${PWD}/OAILunRange.cpp \
    $${PWD}/OAINetworkAddress.cpp \
    $${PWD}/OAINetworkConfig.cpp \
    $${PWD}/OAINfsExport.cpp \
    $${PWD}/OAIProvisioningConfig.cpp \
    $${PWD}/OAIProvisioningQuota.cpp \
    $${PWD}/OAISubmitProvisioningConfigRequest.cpp \
    $${PWD}/OAIVlanAttachment.cpp \
    $${PWD}/OAIVolumeConfig.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
