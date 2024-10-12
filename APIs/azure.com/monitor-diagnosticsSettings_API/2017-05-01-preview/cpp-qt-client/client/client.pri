QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiagnosticSettings.h \
    $${PWD}/OAIDiagnosticSettingsResource.h \
    $${PWD}/OAIDiagnosticSettingsResourceCollection.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogSettings.h \
    $${PWD}/OAIMetricSettings.h \
    $${PWD}/OAIProxyOnlyResource.h \
    $${PWD}/OAIRetentionPolicy.h \
# APIs
    $${PWD}/OAIDiagnosticSettingsApi.h \
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
    $${PWD}/OAIDiagnosticSettings.cpp \
    $${PWD}/OAIDiagnosticSettingsResource.cpp \
    $${PWD}/OAIDiagnosticSettingsResourceCollection.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogSettings.cpp \
    $${PWD}/OAIMetricSettings.cpp \
    $${PWD}/OAIProxyOnlyResource.cpp \
    $${PWD}/OAIRetentionPolicy.cpp \
# APIs
    $${PWD}/OAIDiagnosticSettingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
