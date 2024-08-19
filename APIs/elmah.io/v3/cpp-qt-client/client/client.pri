QT += network

HEADERS += \
# Models
    $${PWD}/OAIBreadcrumb.h \
    $${PWD}/OAICreateBulkMessageResult.h \
    $${PWD}/OAICreateDeployment.h \
    $${PWD}/OAICreateDeploymentResult.h \
    $${PWD}/OAICreateHeartbeat.h \
    $${PWD}/OAICreateLog.h \
    $${PWD}/OAICreateLogResult.h \
    $${PWD}/OAICreateMessage.h \
    $${PWD}/OAICreateMessageResult.h \
    $${PWD}/OAIDeployment.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAILog.h \
    $${PWD}/OAIMessage.h \
    $${PWD}/OAIMessageOverview.h \
    $${PWD}/OAIMessagesResult.h \
    $${PWD}/OAISearch.h \
    $${PWD}/OAIUptimeCheck.h \
# APIs
    $${PWD}/OAIDeploymentsApi.h \
    $${PWD}/OAIHeartbeatsApi.h \
    $${PWD}/OAILogsApi.h \
    $${PWD}/OAIMessagesApi.h \
    $${PWD}/OAISourceMapsApi.h \
    $${PWD}/OAIUptimeChecksApi.h \
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
    $${PWD}/OAIBreadcrumb.cpp \
    $${PWD}/OAICreateBulkMessageResult.cpp \
    $${PWD}/OAICreateDeployment.cpp \
    $${PWD}/OAICreateDeploymentResult.cpp \
    $${PWD}/OAICreateHeartbeat.cpp \
    $${PWD}/OAICreateLog.cpp \
    $${PWD}/OAICreateLogResult.cpp \
    $${PWD}/OAICreateMessage.cpp \
    $${PWD}/OAICreateMessageResult.cpp \
    $${PWD}/OAIDeployment.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAILog.cpp \
    $${PWD}/OAIMessage.cpp \
    $${PWD}/OAIMessageOverview.cpp \
    $${PWD}/OAIMessagesResult.cpp \
    $${PWD}/OAISearch.cpp \
    $${PWD}/OAIUptimeCheck.cpp \
# APIs
    $${PWD}/OAIDeploymentsApi.cpp \
    $${PWD}/OAIHeartbeatsApi.cpp \
    $${PWD}/OAILogsApi.cpp \
    $${PWD}/OAIMessagesApi.cpp \
    $${PWD}/OAISourceMapsApi.cpp \
    $${PWD}/OAIUptimeChecksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
