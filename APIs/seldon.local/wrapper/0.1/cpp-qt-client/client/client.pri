QT += network

HEADERS += \
# Models
    $${PWD}/OAIDefaultData.h \
    $${PWD}/OAIFeedback.h \
    $${PWD}/OAIMeta.h \
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricType.h \
    $${PWD}/OAISeldonMessage.h \
    $${PWD}/OAISeldonMessageList.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIStatusStatusFlag.h \
    $${PWD}/OAITensor.h \
    $${PWD}/OAITensorShapeProtoDim.h \
    $${PWD}/OAITensorflowDataType.h \
    $${PWD}/OAITensorflowResourceHandleProto.h \
    $${PWD}/OAITensorflowTensorProto.h \
    $${PWD}/OAITensorflowTensorShapeProto.h \
    $${PWD}/OAITensorflowVariantTensorDataProto.h \
# APIs
    $${PWD}/OAIInternalApi.h \
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
    $${PWD}/OAIDefaultData.cpp \
    $${PWD}/OAIFeedback.cpp \
    $${PWD}/OAIMeta.cpp \
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricType.cpp \
    $${PWD}/OAISeldonMessage.cpp \
    $${PWD}/OAISeldonMessageList.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIStatusStatusFlag.cpp \
    $${PWD}/OAITensor.cpp \
    $${PWD}/OAITensorShapeProtoDim.cpp \
    $${PWD}/OAITensorflowDataType.cpp \
    $${PWD}/OAITensorflowResourceHandleProto.cpp \
    $${PWD}/OAITensorflowTensorProto.cpp \
    $${PWD}/OAITensorflowTensorShapeProto.cpp \
    $${PWD}/OAITensorflowVariantTensorDataProto.cpp \
# APIs
    $${PWD}/OAIInternalApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
