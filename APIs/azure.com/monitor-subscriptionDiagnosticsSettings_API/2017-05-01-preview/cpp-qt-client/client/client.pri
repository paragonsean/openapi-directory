QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAISubscriptionDiagnosticSettings.h \
    $${PWD}/OAISubscriptionDiagnosticSettingsResource.h \
    $${PWD}/OAISubscriptionDiagnosticSettingsResourceCollection.h \
    $${PWD}/OAISubscriptionLogSettings.h \
    $${PWD}/OAISubscriptionProxyOnlyResource.h \
# APIs
    $${PWD}/OAISubscriptionDiagnosticSettingsApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAISubscriptionDiagnosticSettings.cpp \
    $${PWD}/OAISubscriptionDiagnosticSettingsResource.cpp \
    $${PWD}/OAISubscriptionDiagnosticSettingsResourceCollection.cpp \
    $${PWD}/OAISubscriptionLogSettings.cpp \
    $${PWD}/OAISubscriptionProxyOnlyResource.cpp \
# APIs
    $${PWD}/OAISubscriptionDiagnosticSettingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
