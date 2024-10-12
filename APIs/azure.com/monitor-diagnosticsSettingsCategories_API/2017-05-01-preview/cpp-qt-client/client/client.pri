QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiagnosticSettingsCategory.h \
    $${PWD}/OAIDiagnosticSettingsCategoryResource.h \
    $${PWD}/OAIDiagnosticSettingsCategoryResourceCollection.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIProxyOnlyResource.h \
# APIs
    $${PWD}/OAIDiagnosticSettingsCategoriesApi.h \
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
    $${PWD}/OAIDiagnosticSettingsCategory.cpp \
    $${PWD}/OAIDiagnosticSettingsCategoryResource.cpp \
    $${PWD}/OAIDiagnosticSettingsCategoryResourceCollection.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIProxyOnlyResource.cpp \
# APIs
    $${PWD}/OAIDiagnosticSettingsCategoriesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
