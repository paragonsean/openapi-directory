QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchMeterUsageRequest.h \
    $${PWD}/OAIBatchMeterUsageResult.h \
    $${PWD}/OAIMeterUsageRequest.h \
    $${PWD}/OAIMeterUsageResult.h \
    $${PWD}/OAIRegisterUsageRequest.h \
    $${PWD}/OAIRegisterUsageResult.h \
    $${PWD}/OAIResolveCustomerRequest.h \
    $${PWD}/OAIResolveCustomerResult.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAIUsageAllocation.h \
    $${PWD}/OAIUsageRecord.h \
    $${PWD}/OAIUsageRecordResult.h \
    $${PWD}/OAIUsageRecordResultStatus.h \
    $${PWD}/OAIUsageRecordResult_UsageRecord.h \
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
    $${PWD}/OAIBatchMeterUsageRequest.cpp \
    $${PWD}/OAIBatchMeterUsageResult.cpp \
    $${PWD}/OAIMeterUsageRequest.cpp \
    $${PWD}/OAIMeterUsageResult.cpp \
    $${PWD}/OAIRegisterUsageRequest.cpp \
    $${PWD}/OAIRegisterUsageResult.cpp \
    $${PWD}/OAIResolveCustomerRequest.cpp \
    $${PWD}/OAIResolveCustomerResult.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAIUsageAllocation.cpp \
    $${PWD}/OAIUsageRecord.cpp \
    $${PWD}/OAIUsageRecordResult.cpp \
    $${PWD}/OAIUsageRecordResultStatus.cpp \
    $${PWD}/OAIUsageRecordResult_UsageRecord.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
