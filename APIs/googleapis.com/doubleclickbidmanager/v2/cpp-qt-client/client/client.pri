QT += network

HEADERS += \
# Models
    $${PWD}/OAIChannelGrouping.h \
    $${PWD}/OAIDataRange.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIDisjunctiveMatchStatement.h \
    $${PWD}/OAIEventFilter.h \
    $${PWD}/OAIFilterPair.h \
    $${PWD}/OAIListQueriesResponse.h \
    $${PWD}/OAIListReportsResponse.h \
    $${PWD}/OAIOptions.h \
    $${PWD}/OAIParameters.h \
    $${PWD}/OAIPathFilter.h \
    $${PWD}/OAIPathQueryOptions.h \
    $${PWD}/OAIPathQueryOptionsFilter.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIQueryMetadata.h \
    $${PWD}/OAIQuerySchedule.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportKey.h \
    $${PWD}/OAIReportMetadata.h \
    $${PWD}/OAIReportStatus.h \
    $${PWD}/OAIRule.h \
    $${PWD}/OAIRunQueryRequest.h \
# APIs
    $${PWD}/OAIQueriesApi.h \
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
    $${PWD}/OAIChannelGrouping.cpp \
    $${PWD}/OAIDataRange.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIDisjunctiveMatchStatement.cpp \
    $${PWD}/OAIEventFilter.cpp \
    $${PWD}/OAIFilterPair.cpp \
    $${PWD}/OAIListQueriesResponse.cpp \
    $${PWD}/OAIListReportsResponse.cpp \
    $${PWD}/OAIOptions.cpp \
    $${PWD}/OAIParameters.cpp \
    $${PWD}/OAIPathFilter.cpp \
    $${PWD}/OAIPathQueryOptions.cpp \
    $${PWD}/OAIPathQueryOptionsFilter.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIQueryMetadata.cpp \
    $${PWD}/OAIQuerySchedule.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportKey.cpp \
    $${PWD}/OAIReportMetadata.cpp \
    $${PWD}/OAIReportStatus.cpp \
    $${PWD}/OAIRule.cpp \
    $${PWD}/OAIRunQueryRequest.cpp \
# APIs
    $${PWD}/OAIQueriesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
