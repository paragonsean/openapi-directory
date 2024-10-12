QT += network

HEADERS += \
# Models
    $${PWD}/OAICompatibility.h \
    $${PWD}/OAICompatibilityIssue.h \
    $${PWD}/OAIComputeRole.h \
    $${PWD}/OAIDataDiskImage.h \
    $${PWD}/OAIDeviceConfiguration.h \
    $${PWD}/OAIExtendedProduct.h \
    $${PWD}/OAIExtendedProductProperties.h \
    $${PWD}/OAIIconUris.h \
    $${PWD}/OAIMarketplaceProductLogUpdate.h \
    $${PWD}/OAIOperatingSystem.h \
    $${PWD}/OAIOsDiskImage.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIProductLink.h \
    $${PWD}/OAIProductList.h \
    $${PWD}/OAIProductLog.h \
    $${PWD}/OAIProductNestedProperties.h \
    $${PWD}/OAIProductProperties.h \
    $${PWD}/OAIProducts_List_default_response.h \
    $${PWD}/OAIProducts_List_default_response_error.h \
    $${PWD}/OAIUri.h \
    $${PWD}/OAIVirtualMachineExtensionProductProperties.h \
    $${PWD}/OAIVirtualMachineProductProperties.h \
# APIs
    $${PWD}/OAIProductApi.h \
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
    $${PWD}/OAIDeviceConfiguration.cpp \
    $${PWD}/OAIExtendedProduct.cpp \
    $${PWD}/OAIExtendedProductProperties.cpp \
    $${PWD}/OAIIconUris.cpp \
    $${PWD}/OAIMarketplaceProductLogUpdate.cpp \
    $${PWD}/OAIOperatingSystem.cpp \
    $${PWD}/OAIOsDiskImage.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIProductLink.cpp \
    $${PWD}/OAIProductList.cpp \
    $${PWD}/OAIProductLog.cpp \
    $${PWD}/OAIProductNestedProperties.cpp \
    $${PWD}/OAIProductProperties.cpp \
    $${PWD}/OAIProducts_List_default_response.cpp \
    $${PWD}/OAIProducts_List_default_response_error.cpp \
    $${PWD}/OAIUri.cpp \
    $${PWD}/OAIVirtualMachineExtensionProductProperties.cpp \
    $${PWD}/OAIVirtualMachineProductProperties.cpp \
# APIs
    $${PWD}/OAIProductApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
