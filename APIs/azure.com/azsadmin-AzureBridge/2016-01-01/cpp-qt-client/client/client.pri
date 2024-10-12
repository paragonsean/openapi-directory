QT += network

HEADERS += \
# Models
    $${PWD}/OAICompatibility.h \
    $${PWD}/OAICompatibilityIssue.h \
    $${PWD}/OAIComputeRole.h \
    $${PWD}/OAIDataDiskImage.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIDownloadedProduct.h \
    $${PWD}/OAIDownloadedProductResource.h \
    $${PWD}/OAIDownloadedProduct_allOf_compatibility.h \
    $${PWD}/OAIDownloadedProduct_allOf_iconUris.h \
    $${PWD}/OAIDownloadedProduct_allOf_productProperties.h \
    $${PWD}/OAIExtendedProductProperties.h \
    $${PWD}/OAIGalleryIcons.h \
    $${PWD}/OAIOperatingSystem.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIOsDiskImage.h \
    $${PWD}/OAIProductBase.h \
    $${PWD}/OAIProductLink.h \
    $${PWD}/OAIProductLinks_inner.h \
    $${PWD}/OAIProductProperties.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIUri.h \
    $${PWD}/OAIVirtualMachineExtensionProductProperties.h \
    $${PWD}/OAIVirtualMachineProductProperties.h \
# APIs
    $${PWD}/OAIAzureBridgeApi.h \
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
    $${PWD}/OAICompatibility.cpp \
    $${PWD}/OAICompatibilityIssue.cpp \
    $${PWD}/OAIComputeRole.cpp \
    $${PWD}/OAIDataDiskImage.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIDownloadedProduct.cpp \
    $${PWD}/OAIDownloadedProductResource.cpp \
    $${PWD}/OAIDownloadedProduct_allOf_compatibility.cpp \
    $${PWD}/OAIDownloadedProduct_allOf_iconUris.cpp \
    $${PWD}/OAIDownloadedProduct_allOf_productProperties.cpp \
    $${PWD}/OAIExtendedProductProperties.cpp \
    $${PWD}/OAIGalleryIcons.cpp \
    $${PWD}/OAIOperatingSystem.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIOsDiskImage.cpp \
    $${PWD}/OAIProductBase.cpp \
    $${PWD}/OAIProductLink.cpp \
    $${PWD}/OAIProductLinks_inner.cpp \
    $${PWD}/OAIProductProperties.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIUri.cpp \
    $${PWD}/OAIVirtualMachineExtensionProductProperties.cpp \
    $${PWD}/OAIVirtualMachineProductProperties.cpp \
# APIs
    $${PWD}/OAIAzureBridgeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
