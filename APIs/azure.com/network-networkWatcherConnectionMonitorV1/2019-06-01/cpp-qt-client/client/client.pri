QT += network

HEADERS += \
# Models
    $${PWD}/OAIConnectionMonitor.h \
    $${PWD}/OAIConnectionMonitorDestination.h \
    $${PWD}/OAIConnectionMonitorListResult.h \
    $${PWD}/OAIConnectionMonitorParameters.h \
    $${PWD}/OAIConnectionMonitorQueryResult.h \
    $${PWD}/OAIConnectionMonitorResult.h \
    $${PWD}/OAIConnectionMonitorResultProperties.h \
    $${PWD}/OAIConnectionMonitorSource.h \
    $${PWD}/OAIConnectionMonitors_List_default_response.h \
    $${PWD}/OAIConnectionMonitors_List_default_response_error.h \
    $${PWD}/OAIConnectionMonitors_UpdateTags_request.h \
    $${PWD}/OAIConnectionStateSnapshot.h \
    $${PWD}/OAIConnectionStateSnapshot_hops_inner.h \
    $${PWD}/OAIConnectionStateSnapshot_hops_inner_issues_inner.h \
# APIs
    $${PWD}/OAIConnectionMonitorsApi.h \
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
    $${PWD}/OAIConnectionMonitor.cpp \
    $${PWD}/OAIConnectionMonitorDestination.cpp \
    $${PWD}/OAIConnectionMonitorListResult.cpp \
    $${PWD}/OAIConnectionMonitorParameters.cpp \
    $${PWD}/OAIConnectionMonitorQueryResult.cpp \
    $${PWD}/OAIConnectionMonitorResult.cpp \
    $${PWD}/OAIConnectionMonitorResultProperties.cpp \
    $${PWD}/OAIConnectionMonitorSource.cpp \
    $${PWD}/OAIConnectionMonitors_List_default_response.cpp \
    $${PWD}/OAIConnectionMonitors_List_default_response_error.cpp \
    $${PWD}/OAIConnectionMonitors_UpdateTags_request.cpp \
    $${PWD}/OAIConnectionStateSnapshot.cpp \
    $${PWD}/OAIConnectionStateSnapshot_hops_inner.cpp \
    $${PWD}/OAIConnectionStateSnapshot_hops_inner_issues_inner.cpp \
# APIs
    $${PWD}/OAIConnectionMonitorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
