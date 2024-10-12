QT += network

HEADERS += \
# Models
    $${PWD}/OAIColor.h \
    $${PWD}/OAIFileResponse.h \
    $${PWD}/OAIPreviewResponse.h \
    $${PWD}/OAIProcess.h \
    $${PWD}/OAIProject.h \
    $${PWD}/OAIProjectRequest.h \
    $${PWD}/OAIProjectResponse.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportRequest.h \
    $${PWD}/OAIReportResponse.h \
    $${PWD}/OAIResult.h \
    $${PWD}/OAIResultResponse.h \
# APIs
    $${PWD}/OAIPreviewsApi.h \
    $${PWD}/OAIProcessesApi.h \
    $${PWD}/OAIProjectsApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAIResultsApi.h \
    $${PWD}/OAIUploadsApi.h \
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
    $${PWD}/OAIColor.cpp \
    $${PWD}/OAIFileResponse.cpp \
    $${PWD}/OAIPreviewResponse.cpp \
    $${PWD}/OAIProcess.cpp \
    $${PWD}/OAIProject.cpp \
    $${PWD}/OAIProjectRequest.cpp \
    $${PWD}/OAIProjectResponse.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportRequest.cpp \
    $${PWD}/OAIReportResponse.cpp \
    $${PWD}/OAIResult.cpp \
    $${PWD}/OAIResultResponse.cpp \
# APIs
    $${PWD}/OAIPreviewsApi.cpp \
    $${PWD}/OAIProcessesApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAIResultsApi.cpp \
    $${PWD}/OAIUploadsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
