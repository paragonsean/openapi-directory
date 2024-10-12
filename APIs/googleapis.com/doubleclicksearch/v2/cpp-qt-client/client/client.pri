QT += network

HEADERS += \
# Models
    $${PWD}/OAIAvailability.h \
    $${PWD}/OAIConversion.h \
    $${PWD}/OAIConversionList.h \
    $${PWD}/OAICustomDimension.h \
    $${PWD}/OAICustomMetric.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportApiColumnSpec.h \
    $${PWD}/OAIReportRequest.h \
    $${PWD}/OAIReportRequest_filters_inner.h \
    $${PWD}/OAIReportRequest_orderBy_inner.h \
    $${PWD}/OAIReportRequest_reportScope.h \
    $${PWD}/OAIReportRequest_timeRange.h \
    $${PWD}/OAIReport_files_inner.h \
    $${PWD}/OAISavedColumn.h \
    $${PWD}/OAISavedColumnList.h \
    $${PWD}/OAIUpdateAvailabilityRequest.h \
    $${PWD}/OAIUpdateAvailabilityResponse.h \
# APIs
    $${PWD}/OAIConversionApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAISavedColumnsApi.h \
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
    $${PWD}/OAIAvailability.cpp \
    $${PWD}/OAIConversion.cpp \
    $${PWD}/OAIConversionList.cpp \
    $${PWD}/OAICustomDimension.cpp \
    $${PWD}/OAICustomMetric.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportApiColumnSpec.cpp \
    $${PWD}/OAIReportRequest.cpp \
    $${PWD}/OAIReportRequest_filters_inner.cpp \
    $${PWD}/OAIReportRequest_orderBy_inner.cpp \
    $${PWD}/OAIReportRequest_reportScope.cpp \
    $${PWD}/OAIReportRequest_timeRange.cpp \
    $${PWD}/OAIReport_files_inner.cpp \
    $${PWD}/OAISavedColumn.cpp \
    $${PWD}/OAISavedColumnList.cpp \
    $${PWD}/OAIUpdateAvailabilityRequest.cpp \
    $${PWD}/OAIUpdateAvailabilityResponse.cpp \
# APIs
    $${PWD}/OAIConversionApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAISavedColumnsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
