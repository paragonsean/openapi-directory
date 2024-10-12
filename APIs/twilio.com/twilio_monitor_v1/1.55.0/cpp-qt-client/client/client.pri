QT += network

HEADERS += \
# Models
    $${PWD}/OAIListAlertResponse.h \
    $${PWD}/OAIListAlertResponse_meta.h \
    $${PWD}/OAIListEventResponse.h \
    $${PWD}/OAIMonitor_v1_alert.h \
    $${PWD}/OAIMonitor_v1_alert_instance.h \
    $${PWD}/OAIMonitor_v1_event.h \
# APIs
    $${PWD}/OAIMonitorV1AlertApi.h \
    $${PWD}/OAIMonitorV1EventApi.h \
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
    $${PWD}/OAIListAlertResponse.cpp \
    $${PWD}/OAIListAlertResponse_meta.cpp \
    $${PWD}/OAIListEventResponse.cpp \
    $${PWD}/OAIMonitor_v1_alert.cpp \
    $${PWD}/OAIMonitor_v1_alert_instance.cpp \
    $${PWD}/OAIMonitor_v1_event.cpp \
# APIs
    $${PWD}/OAIMonitorV1AlertApi.cpp \
    $${PWD}/OAIMonitorV1EventApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
