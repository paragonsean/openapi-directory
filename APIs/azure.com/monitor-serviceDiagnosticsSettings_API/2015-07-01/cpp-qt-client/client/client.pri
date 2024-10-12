QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogSettings.h \
    $${PWD}/OAIMetricSettings.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIRetentionPolicy.h \
    $${PWD}/OAIServiceDiagnosticSettings.h \
    $${PWD}/OAIServiceDiagnosticSettingsResource.h \
# APIs
    $${PWD}/OAIServiceDiagnosticSettingsApi.h \
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
    $${PWD}/OAILogSettings.cpp \
    $${PWD}/OAIMetricSettings.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIRetentionPolicy.cpp \
    $${PWD}/OAIServiceDiagnosticSettings.cpp \
    $${PWD}/OAIServiceDiagnosticSettingsResource.cpp \
# APIs
    $${PWD}/OAIServiceDiagnosticSettingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
