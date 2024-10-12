QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckErrorResponse.h \
    $${PWD}/OAICheckResponse.h \
    $${PWD}/OAIControlErrorResponse.h \
    $${PWD}/OAIControlResponse.h \
    $${PWD}/OAIErrorThrottled.h \
    $${PWD}/OAINetworkUnblock.h \
    $${PWD}/OAINetworkUnblockResponseForbidden.h \
    $${PWD}/OAINetworkUnblockResponseInvalidDuration.h \
    $${PWD}/OAINetworkUnblockResponseInvalidDuration_invalid_parameters_inner.h \
    $${PWD}/OAINetworkUnblockResponseNotFound.h \
    $${PWD}/OAINetworkUnblockResponseOk.h \
    $${PWD}/OAINetworkUnblockResponseUnprocessableNetwork.h \
    $${PWD}/OAINetworkUnblock_422_response.h \
    $${PWD}/OAIRequestErrorResponse.h \
    $${PWD}/OAIRequestResponse.h \
    $${PWD}/OAISearchErrorResponse.h \
    $${PWD}/OAISearchResponse.h \
    $${PWD}/OAISearchResponse_checks_inner.h \
    $${PWD}/OAISearchResponse_events_inner.h \
    $${PWD}/OAIVerifyCheck_200_response.h \
    $${PWD}/OAIVerifyControl_200_response.h \
    $${PWD}/OAIVerifyRequestWithPSD2_200_response.h \
    $${PWD}/OAIVerifySearch_200_response.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIFraudManagementApi.h \
    $${PWD}/OAIRequestsApi.h \
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
    $${PWD}/OAICheckErrorResponse.cpp \
    $${PWD}/OAICheckResponse.cpp \
    $${PWD}/OAIControlErrorResponse.cpp \
    $${PWD}/OAIControlResponse.cpp \
    $${PWD}/OAIErrorThrottled.cpp \
    $${PWD}/OAINetworkUnblock.cpp \
    $${PWD}/OAINetworkUnblockResponseForbidden.cpp \
    $${PWD}/OAINetworkUnblockResponseInvalidDuration.cpp \
    $${PWD}/OAINetworkUnblockResponseInvalidDuration_invalid_parameters_inner.cpp \
    $${PWD}/OAINetworkUnblockResponseNotFound.cpp \
    $${PWD}/OAINetworkUnblockResponseOk.cpp \
    $${PWD}/OAINetworkUnblockResponseUnprocessableNetwork.cpp \
    $${PWD}/OAINetworkUnblock_422_response.cpp \
    $${PWD}/OAIRequestErrorResponse.cpp \
    $${PWD}/OAIRequestResponse.cpp \
    $${PWD}/OAISearchErrorResponse.cpp \
    $${PWD}/OAISearchResponse.cpp \
    $${PWD}/OAISearchResponse_checks_inner.cpp \
    $${PWD}/OAISearchResponse_events_inner.cpp \
    $${PWD}/OAIVerifyCheck_200_response.cpp \
    $${PWD}/OAIVerifyControl_200_response.cpp \
    $${PWD}/OAIVerifyRequestWithPSD2_200_response.cpp \
    $${PWD}/OAIVerifySearch_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIFraudManagementApi.cpp \
    $${PWD}/OAIRequestsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
