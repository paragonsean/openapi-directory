QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcceleratorType.h \
    $${PWD}/OAIListAcceleratorTypesResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListNodesResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAIListTensorFlowVersionsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAINetworkEndpoint.h \
    $${PWD}/OAINode.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIReimageNodeRequest.h \
    $${PWD}/OAISchedulingConfig.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISymptom.h \
    $${PWD}/OAITensorFlowVersion.h \
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
    $${PWD}/OAIAcceleratorType.cpp \
    $${PWD}/OAIListAcceleratorTypesResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListNodesResponse.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAIListTensorFlowVersionsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAINetworkEndpoint.cpp \
    $${PWD}/OAINode.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIReimageNodeRequest.cpp \
    $${PWD}/OAISchedulingConfig.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISymptom.cpp \
    $${PWD}/OAITensorFlowVersion.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
