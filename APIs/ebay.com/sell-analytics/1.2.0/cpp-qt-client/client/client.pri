QT += network

HEADERS += \
# Models
    $${PWD}/OAIBenchmarkMetadata.h \
    $${PWD}/OAICycle.h \
    $${PWD}/OAIDefinition.h \
    $${PWD}/OAIDimension.h \
    $${PWD}/OAIDimensionMetric.h \
    $${PWD}/OAIDistribution.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIEvaluationCycle.h \
    $${PWD}/OAIFindSellerStandardsProfilesResponse.h \
    $${PWD}/OAIGetCustomerServiceMetricResponse.h \
    $${PWD}/OAIHeader.h \
    $${PWD}/OAIMetadata.h \
    $${PWD}/OAIMetadataHeader.h \
    $${PWD}/OAIMetadataRecord.h \
    $${PWD}/OAIMetric.h \
    $${PWD}/OAIMetricBenchmark.h \
    $${PWD}/OAIMetricDistribution.h \
    $${PWD}/OAIRecord.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIStandardsProfile.h \
    $${PWD}/OAIValue.h \
# APIs
    $${PWD}/OAICustomerServiceMetricApi.h \
    $${PWD}/OAISellerStandardsProfileApi.h \
    $${PWD}/OAITrafficReportApi.h \
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
    $${PWD}/OAIBenchmarkMetadata.cpp \
    $${PWD}/OAICycle.cpp \
    $${PWD}/OAIDefinition.cpp \
    $${PWD}/OAIDimension.cpp \
    $${PWD}/OAIDimensionMetric.cpp \
    $${PWD}/OAIDistribution.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIEvaluationCycle.cpp \
    $${PWD}/OAIFindSellerStandardsProfilesResponse.cpp \
    $${PWD}/OAIGetCustomerServiceMetricResponse.cpp \
    $${PWD}/OAIHeader.cpp \
    $${PWD}/OAIMetadata.cpp \
    $${PWD}/OAIMetadataHeader.cpp \
    $${PWD}/OAIMetadataRecord.cpp \
    $${PWD}/OAIMetric.cpp \
    $${PWD}/OAIMetricBenchmark.cpp \
    $${PWD}/OAIMetricDistribution.cpp \
    $${PWD}/OAIRecord.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIStandardsProfile.cpp \
    $${PWD}/OAIValue.cpp \
# APIs
    $${PWD}/OAICustomerServiceMetricApi.cpp \
    $${PWD}/OAISellerStandardsProfileApi.cpp \
    $${PWD}/OAITrafficReportApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
