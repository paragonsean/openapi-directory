QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcceleratorType.h \
    $${PWD}/OAIAcceleratorTypeOffering.h \
    $${PWD}/OAIAcceleratorType_memoryInfo.h \
    $${PWD}/OAIDescribeAcceleratorOfferingsRequest.h \
    $${PWD}/OAIDescribeAcceleratorOfferingsResponse.h \
    $${PWD}/OAIDescribeAcceleratorOfferings_request.h \
    $${PWD}/OAIDescribeAcceleratorTypesResponse.h \
    $${PWD}/OAIDescribeAcceleratorsRequest.h \
    $${PWD}/OAIDescribeAcceleratorsResponse.h \
    $${PWD}/OAIDescribeAccelerators_request.h \
    $${PWD}/OAIElasticInferenceAccelerator.h \
    $${PWD}/OAIElasticInferenceAcceleratorHealth.h \
    $${PWD}/OAIElasticInferenceAccelerator_acceleratorHealth.h \
    $${PWD}/OAIFilter.h \
    $${PWD}/OAIKeyValuePair.h \
    $${PWD}/OAIListTagsForResourceResult.h \
    $${PWD}/OAILocationType.h \
    $${PWD}/OAIMemoryInfo.h \
    $${PWD}/OAITagResourceRequest.h \
    $${PWD}/OAITagResource_request.h \
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
    $${PWD}/OAIAcceleratorType.cpp \
    $${PWD}/OAIAcceleratorTypeOffering.cpp \
    $${PWD}/OAIAcceleratorType_memoryInfo.cpp \
    $${PWD}/OAIDescribeAcceleratorOfferingsRequest.cpp \
    $${PWD}/OAIDescribeAcceleratorOfferingsResponse.cpp \
    $${PWD}/OAIDescribeAcceleratorOfferings_request.cpp \
    $${PWD}/OAIDescribeAcceleratorTypesResponse.cpp \
    $${PWD}/OAIDescribeAcceleratorsRequest.cpp \
    $${PWD}/OAIDescribeAcceleratorsResponse.cpp \
    $${PWD}/OAIDescribeAccelerators_request.cpp \
    $${PWD}/OAIElasticInferenceAccelerator.cpp \
    $${PWD}/OAIElasticInferenceAcceleratorHealth.cpp \
    $${PWD}/OAIElasticInferenceAccelerator_acceleratorHealth.cpp \
    $${PWD}/OAIFilter.cpp \
    $${PWD}/OAIKeyValuePair.cpp \
    $${PWD}/OAIListTagsForResourceResult.cpp \
    $${PWD}/OAILocationType.cpp \
    $${PWD}/OAIMemoryInfo.cpp \
    $${PWD}/OAITagResourceRequest.cpp \
    $${PWD}/OAITagResource_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
