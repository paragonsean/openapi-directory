QT += network

HEADERS += \
# Models
    $${PWD}/OAIAlert.h \
    $${PWD}/OAIAlertConfidenceReason.h \
    $${PWD}/OAIAlertEntity.h \
    $${PWD}/OAIAlertList.h \
    $${PWD}/OAIAlertProperties.h \
    $${PWD}/OAIAlerts_List_default_response.h \
    $${PWD}/OAIAlerts_List_default_response_error.h \
# APIs
    $${PWD}/OAIAlertsApi.h \
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
    $${PWD}/OAIAlert.cpp \
    $${PWD}/OAIAlertConfidenceReason.cpp \
    $${PWD}/OAIAlertEntity.cpp \
    $${PWD}/OAIAlertList.cpp \
    $${PWD}/OAIAlertProperties.cpp \
    $${PWD}/OAIAlerts_List_default_response.cpp \
    $${PWD}/OAIAlerts_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIAlertsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
