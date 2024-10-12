QT += network

HEADERS += \
# Models
    $${PWD}/OAIPublicIPAddresses_GetVirtualMachineScaleSetPublicIPAddress_200_response.h \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response.h \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response_value_inner.h \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response_value_inner_sku.h \
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
    $${PWD}/OAIPublicIPAddresses_GetVirtualMachineScaleSetPublicIPAddress_200_response.cpp \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response.cpp \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response_value_inner.cpp \
    $${PWD}/OAIPublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses_200_response_value_inner_sku.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
