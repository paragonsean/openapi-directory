QT += network

HEADERS += \
# Models
    $${PWD}/OAIAudit.h \
    $${PWD}/OAIExtension.h \
    $${PWD}/OAIFeedback.h \
    $${PWD}/OAILog.h \
    $${PWD}/OAIPostLog.h \
    $${PWD}/OAIPostSite.h \
    $${PWD}/OAISite.h \
    $${PWD}/OAISsoUsers.h \
    $${PWD}/OAITag.h \
# APIs
    $${PWD}/OAIAuditsApi.h \
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIExtensionsApi.h \
    $${PWD}/OAIFeedbacksApi.h \
    $${PWD}/OAILogsApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAISitesApi.h \
    $${PWD}/OAISsousersApi.h \
    $${PWD}/OAITagsApi.h \
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
    $${PWD}/OAIAudit.cpp \
    $${PWD}/OAIExtension.cpp \
    $${PWD}/OAIFeedback.cpp \
    $${PWD}/OAILog.cpp \
    $${PWD}/OAIPostLog.cpp \
    $${PWD}/OAIPostSite.cpp \
    $${PWD}/OAISite.cpp \
    $${PWD}/OAISsoUsers.cpp \
    $${PWD}/OAITag.cpp \
# APIs
    $${PWD}/OAIAuditsApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIExtensionsApi.cpp \
    $${PWD}/OAIFeedbacksApi.cpp \
    $${PWD}/OAILogsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAISitesApi.cpp \
    $${PWD}/OAISsousersApi.cpp \
    $${PWD}/OAITagsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
