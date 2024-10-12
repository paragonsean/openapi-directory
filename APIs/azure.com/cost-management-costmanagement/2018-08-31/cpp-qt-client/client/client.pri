QT += network

HEADERS += \
# Models
    $${PWD}/OAIDimension.h \
    $${PWD}/OAIDimensionProperties.h \
    $${PWD}/OAIDimensionsListResult.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQueryColumn.h \
    $${PWD}/OAIQueryProperties.h \
    $${PWD}/OAIQueryResult.h \
    $${PWD}/OAIReportConfigAggregation.h \
    $${PWD}/OAIReportConfigColumnType.h \
    $${PWD}/OAIReportConfigComparisonExpression.h \
    $${PWD}/OAIReportConfigDataset.h \
    $${PWD}/OAIReportConfigDatasetConfiguration.h \
    $${PWD}/OAIReportConfigDefinition.h \
    $${PWD}/OAIReportConfigFilter.h \
    $${PWD}/OAIReportConfigGrouping.h \
    $${PWD}/OAIReportConfigSorting.h \
    $${PWD}/OAIReportConfigTimePeriod.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIDimensionsApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIQueryApi.h \
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
    $${PWD}/OAIDimension.cpp \
    $${PWD}/OAIDimensionProperties.cpp \
    $${PWD}/OAIDimensionsListResult.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQueryColumn.cpp \
    $${PWD}/OAIQueryProperties.cpp \
    $${PWD}/OAIQueryResult.cpp \
    $${PWD}/OAIReportConfigAggregation.cpp \
    $${PWD}/OAIReportConfigColumnType.cpp \
    $${PWD}/OAIReportConfigComparisonExpression.cpp \
    $${PWD}/OAIReportConfigDataset.cpp \
    $${PWD}/OAIReportConfigDatasetConfiguration.cpp \
    $${PWD}/OAIReportConfigDefinition.cpp \
    $${PWD}/OAIReportConfigFilter.cpp \
    $${PWD}/OAIReportConfigGrouping.cpp \
    $${PWD}/OAIReportConfigSorting.cpp \
    $${PWD}/OAIReportConfigTimePeriod.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIDimensionsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIQueryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
