QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIError.h \
    $${PWD}/OAICrawlRun.h \
    $${PWD}/OAIInputs.h \
    $${PWD}/OAIObjectStoreSearchResult.h \
    $${PWD}/OAIObjectStoreSearchResult_hits.h \
    $${PWD}/OAIObjectStoreSearchResult_hits_hits_inner.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportRun.h \
    $${PWD}/OAISchedule.h \
    $${PWD}/OAIScheduleRequest.h \
    $${PWD}/OAISchedule_intervalData.h \
# APIs
    $${PWD}/OAIRssImportIoApi.h \
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
    $${PWD}/OAIAPIError.cpp \
    $${PWD}/OAICrawlRun.cpp \
    $${PWD}/OAIInputs.cpp \
    $${PWD}/OAIObjectStoreSearchResult.cpp \
    $${PWD}/OAIObjectStoreSearchResult_hits.cpp \
    $${PWD}/OAIObjectStoreSearchResult_hits_hits_inner.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportRun.cpp \
    $${PWD}/OAISchedule.cpp \
    $${PWD}/OAIScheduleRequest.cpp \
    $${PWD}/OAISchedule_intervalData.cpp \
# APIs
    $${PWD}/OAIRssImportIoApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
