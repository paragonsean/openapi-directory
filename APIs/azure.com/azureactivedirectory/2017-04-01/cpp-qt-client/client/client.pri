QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiagnosticSettings.h \
    $${PWD}/OAIDiagnosticSettingsCategory.h \
    $${PWD}/OAIDiagnosticSettingsCategoryResource.h \
    $${PWD}/OAIDiagnosticSettingsCategoryResourceCollection.h \
    $${PWD}/OAIDiagnosticSettingsResource.h \
    $${PWD}/OAIDiagnosticSettingsResourceCollection.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogSettings.h \
    $${PWD}/OAIOperationsDiscovery.h \
    $${PWD}/OAIOperationsDiscoveryCollection.h \
    $${PWD}/OAIProxyOnlyResource.h \
    $${PWD}/OAIRetentionPolicy.h \
# APIs
    $${PWD}/OAIDiagnosticSettingsApi.h \
    $${PWD}/OAIDiagnosticSettingsCategoriesApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIDiagnosticSettingsCategory.cpp \
    $${PWD}/OAIDiagnosticSettingsCategoryResource.cpp \
    $${PWD}/OAIDiagnosticSettingsCategoryResourceCollection.cpp \
    $${PWD}/OAIDiagnosticSettingsResource.cpp \
    $${PWD}/OAIDiagnosticSettingsResourceCollection.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogSettings.cpp \
    $${PWD}/OAIOperationsDiscovery.cpp \
    $${PWD}/OAIOperationsDiscoveryCollection.cpp \
    $${PWD}/OAIProxyOnlyResource.cpp \
    $${PWD}/OAIRetentionPolicy.cpp \
# APIs
    $${PWD}/OAIDiagnosticSettingsApi.cpp \
    $${PWD}/OAIDiagnosticSettingsCategoriesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
