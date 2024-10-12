QT += network

HEADERS += \
# Models
    $${PWD}/OAIClaimDevicesByClaimCodeResponse.h \
    $${PWD}/OAIDescribeDeviceResponse.h \
    $${PWD}/OAIDescribeDeviceResponse_DeviceDescription.h \
    $${PWD}/OAIDevice.h \
    $${PWD}/OAIDeviceDescription.h \
    $${PWD}/OAIDeviceEvent.h \
    $${PWD}/OAIDeviceEvent_Device.h \
    $${PWD}/OAIDeviceMethod.h \
    $${PWD}/OAIFinalizeDeviceClaimRequest.h \
    $${PWD}/OAIFinalizeDeviceClaimResponse.h \
    $${PWD}/OAIFinalizeDeviceClaim_request.h \
    $${PWD}/OAIGetDeviceMethodsResponse.h \
    $${PWD}/OAIInitiateDeviceClaimResponse.h \
    $${PWD}/OAIInvokeDeviceMethodRequest.h \
    $${PWD}/OAIInvokeDeviceMethodRequest_DeviceMethod.h \
    $${PWD}/OAIInvokeDeviceMethodResponse.h \
    $${PWD}/OAIInvokeDeviceMethod_request.h \
    $${PWD}/OAIInvokeDeviceMethod_request_deviceMethod.h \
    $${PWD}/OAIListDeviceEventsResponse.h \
    $${PWD}/OAIListDevicesResponse.h \
    $${PWD}/OAIListTagsForResourceResponse.h \
    $${PWD}/OAITagResourceRequest.h \
    $${PWD}/OAITagResource_request.h \
    $${PWD}/OAIUnclaimDeviceResponse.h \
    $${PWD}/OAIUpdateDeviceStateRequest.h \
    $${PWD}/OAIUpdateDeviceState_request.h \
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
    $${PWD}/OAIClaimDevicesByClaimCodeResponse.cpp \
    $${PWD}/OAIDescribeDeviceResponse.cpp \
    $${PWD}/OAIDescribeDeviceResponse_DeviceDescription.cpp \
    $${PWD}/OAIDevice.cpp \
    $${PWD}/OAIDeviceDescription.cpp \
    $${PWD}/OAIDeviceEvent.cpp \
    $${PWD}/OAIDeviceEvent_Device.cpp \
    $${PWD}/OAIDeviceMethod.cpp \
    $${PWD}/OAIFinalizeDeviceClaimRequest.cpp \
    $${PWD}/OAIFinalizeDeviceClaimResponse.cpp \
    $${PWD}/OAIFinalizeDeviceClaim_request.cpp \
    $${PWD}/OAIGetDeviceMethodsResponse.cpp \
    $${PWD}/OAIInitiateDeviceClaimResponse.cpp \
    $${PWD}/OAIInvokeDeviceMethodRequest.cpp \
    $${PWD}/OAIInvokeDeviceMethodRequest_DeviceMethod.cpp \
    $${PWD}/OAIInvokeDeviceMethodResponse.cpp \
    $${PWD}/OAIInvokeDeviceMethod_request.cpp \
    $${PWD}/OAIInvokeDeviceMethod_request_deviceMethod.cpp \
    $${PWD}/OAIListDeviceEventsResponse.cpp \
    $${PWD}/OAIListDevicesResponse.cpp \
    $${PWD}/OAIListTagsForResourceResponse.cpp \
    $${PWD}/OAITagResourceRequest.cpp \
    $${PWD}/OAITagResource_request.cpp \
    $${PWD}/OAIUnclaimDeviceResponse.cpp \
    $${PWD}/OAIUpdateDeviceStateRequest.cpp \
    $${PWD}/OAIUpdateDeviceState_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
