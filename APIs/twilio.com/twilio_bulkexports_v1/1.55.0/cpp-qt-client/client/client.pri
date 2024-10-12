QT += network

HEADERS += \
# Models
    $${PWD}/OAIBulkexports_v1_export.h \
    $${PWD}/OAIBulkexports_v1_export_configuration.h \
    $${PWD}/OAIBulkexports_v1_export_day.h \
    $${PWD}/OAIBulkexports_v1_export_day_instance.h \
    $${PWD}/OAIBulkexports_v1_export_export_custom_job.h \
    $${PWD}/OAIBulkexports_v1_export_job.h \
    $${PWD}/OAIExport_custom_job_enum_status.h \
    $${PWD}/OAIJob_enum_status.h \
    $${PWD}/OAIListDayResponse.h \
    $${PWD}/OAIListDayResponse_meta.h \
    $${PWD}/OAIListExportCustomJobResponse.h \
# APIs
    $${PWD}/OAIBulkexportsV1DayApi.h \
    $${PWD}/OAIBulkexportsV1ExportApi.h \
    $${PWD}/OAIBulkexportsV1ExportConfigurationApi.h \
    $${PWD}/OAIBulkexportsV1ExportCustomJobApi.h \
    $${PWD}/OAIBulkexportsV1JobApi.h \
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
    $${PWD}/OAIBulkexports_v1_export.cpp \
    $${PWD}/OAIBulkexports_v1_export_configuration.cpp \
    $${PWD}/OAIBulkexports_v1_export_day.cpp \
    $${PWD}/OAIBulkexports_v1_export_day_instance.cpp \
    $${PWD}/OAIBulkexports_v1_export_export_custom_job.cpp \
    $${PWD}/OAIBulkexports_v1_export_job.cpp \
    $${PWD}/OAIExport_custom_job_enum_status.cpp \
    $${PWD}/OAIJob_enum_status.cpp \
    $${PWD}/OAIListDayResponse.cpp \
    $${PWD}/OAIListDayResponse_meta.cpp \
    $${PWD}/OAIListExportCustomJobResponse.cpp \
# APIs
    $${PWD}/OAIBulkexportsV1DayApi.cpp \
    $${PWD}/OAIBulkexportsV1ExportApi.cpp \
    $${PWD}/OAIBulkexportsV1ExportConfigurationApi.cpp \
    $${PWD}/OAIBulkexportsV1ExportCustomJobApi.cpp \
    $${PWD}/OAIBulkexportsV1JobApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
