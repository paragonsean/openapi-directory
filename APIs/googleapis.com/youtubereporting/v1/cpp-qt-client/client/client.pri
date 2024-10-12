QT += network

HEADERS += \
# Models
    $${PWD}/OAIGdataBlobstore2Info.h \
    $${PWD}/OAIGdataCompositeMedia.h \
    $${PWD}/OAIGdataContentTypeInfo.h \
    $${PWD}/OAIGdataDiffChecksumsResponse.h \
    $${PWD}/OAIGdataDiffDownloadResponse.h \
    $${PWD}/OAIGdataDiffUploadRequest.h \
    $${PWD}/OAIGdataDiffUploadResponse.h \
    $${PWD}/OAIGdataDiffVersionResponse.h \
    $${PWD}/OAIGdataDownloadParameters.h \
    $${PWD}/OAIGdataMedia.h \
    $${PWD}/OAIGdataObjectId.h \
    $${PWD}/OAIJob.h \
    $${PWD}/OAIListJobsResponse.h \
    $${PWD}/OAIListReportTypesResponse.h \
    $${PWD}/OAIListReportsResponse.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportType.h \
# APIs
    $${PWD}/OAIJobsApi.h \
    $${PWD}/OAIMediaApi.h \
    $${PWD}/OAIReportTypesApi.h \
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
    $${PWD}/OAIGdataBlobstore2Info.cpp \
    $${PWD}/OAIGdataCompositeMedia.cpp \
    $${PWD}/OAIGdataContentTypeInfo.cpp \
    $${PWD}/OAIGdataDiffChecksumsResponse.cpp \
    $${PWD}/OAIGdataDiffDownloadResponse.cpp \
    $${PWD}/OAIGdataDiffUploadRequest.cpp \
    $${PWD}/OAIGdataDiffUploadResponse.cpp \
    $${PWD}/OAIGdataDiffVersionResponse.cpp \
    $${PWD}/OAIGdataDownloadParameters.cpp \
    $${PWD}/OAIGdataMedia.cpp \
    $${PWD}/OAIGdataObjectId.cpp \
    $${PWD}/OAIJob.cpp \
    $${PWD}/OAIListJobsResponse.cpp \
    $${PWD}/OAIListReportTypesResponse.cpp \
    $${PWD}/OAIListReportsResponse.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportType.cpp \
# APIs
    $${PWD}/OAIJobsApi.cpp \
    $${PWD}/OAIMediaApi.cpp \
    $${PWD}/OAIReportTypesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
