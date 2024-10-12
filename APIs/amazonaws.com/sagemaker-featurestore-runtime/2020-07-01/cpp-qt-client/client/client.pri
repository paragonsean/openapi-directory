QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchGetRecordError.h \
    $${PWD}/OAIBatchGetRecordIdentifier.h \
    $${PWD}/OAIBatchGetRecordRequest.h \
    $${PWD}/OAIBatchGetRecordResponse.h \
    $${PWD}/OAIBatchGetRecordResultDetail.h \
    $${PWD}/OAIBatchGetRecord_request.h \
    $${PWD}/OAIDeletionMode.h \
    $${PWD}/OAIExpirationTimeResponse.h \
    $${PWD}/OAIFeatureValue.h \
    $${PWD}/OAIGetRecordResponse.h \
    $${PWD}/OAIPutRecordRequest.h \
    $${PWD}/OAIPutRecordRequest_TtlDuration.h \
    $${PWD}/OAIPutRecord_request.h \
    $${PWD}/OAIPutRecord_request_TtlDuration.h \
    $${PWD}/OAITargetStore.h \
    $${PWD}/OAITtlDuration.h \
    $${PWD}/OAITtlDurationUnit.h \
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
    $${PWD}/OAIBatchGetRecordError.cpp \
    $${PWD}/OAIBatchGetRecordIdentifier.cpp \
    $${PWD}/OAIBatchGetRecordRequest.cpp \
    $${PWD}/OAIBatchGetRecordResponse.cpp \
    $${PWD}/OAIBatchGetRecordResultDetail.cpp \
    $${PWD}/OAIBatchGetRecord_request.cpp \
    $${PWD}/OAIDeletionMode.cpp \
    $${PWD}/OAIExpirationTimeResponse.cpp \
    $${PWD}/OAIFeatureValue.cpp \
    $${PWD}/OAIGetRecordResponse.cpp \
    $${PWD}/OAIPutRecordRequest.cpp \
    $${PWD}/OAIPutRecordRequest_TtlDuration.cpp \
    $${PWD}/OAIPutRecord_request.cpp \
    $${PWD}/OAIPutRecord_request_TtlDuration.cpp \
    $${PWD}/OAITargetStore.cpp \
    $${PWD}/OAITtlDuration.cpp \
    $${PWD}/OAITtlDurationUnit.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
