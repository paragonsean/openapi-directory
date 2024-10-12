QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateEndpointRequest.h \
    $${PWD}/OAICreateEndpointResult.h \
    $${PWD}/OAICreateEndpoint_request.h \
    $${PWD}/OAIEndpoint.h \
    $${PWD}/OAIEndpointAccessType.h \
    $${PWD}/OAIEndpointStatus.h \
    $${PWD}/OAIEndpoint_FailedReason.h \
    $${PWD}/OAIFailedReason.h \
    $${PWD}/OAIListEndpointsResult.h \
    $${PWD}/OAIListOutpostsWithS3Result.h \
    $${PWD}/OAIListSharedEndpointsResult.h \
    $${PWD}/OAINetworkInterface.h \
    $${PWD}/OAIOutpost.h \
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
    $${PWD}/OAICreateEndpointRequest.cpp \
    $${PWD}/OAICreateEndpointResult.cpp \
    $${PWD}/OAICreateEndpoint_request.cpp \
    $${PWD}/OAIEndpoint.cpp \
    $${PWD}/OAIEndpointAccessType.cpp \
    $${PWD}/OAIEndpointStatus.cpp \
    $${PWD}/OAIEndpoint_FailedReason.cpp \
    $${PWD}/OAIFailedReason.cpp \
    $${PWD}/OAIListEndpointsResult.cpp \
    $${PWD}/OAIListOutpostsWithS3Result.cpp \
    $${PWD}/OAIListSharedEndpointsResult.cpp \
    $${PWD}/OAINetworkInterface.cpp \
    $${PWD}/OAIOutpost.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
