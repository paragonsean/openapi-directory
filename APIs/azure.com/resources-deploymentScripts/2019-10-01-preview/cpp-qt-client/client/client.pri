QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureCliScript.h \
    $${PWD}/OAIAzureCliScriptProperties.h \
    $${PWD}/OAIAzurePowerShellScript.h \
    $${PWD}/OAIAzurePowerShellScriptProperties.h \
    $${PWD}/OAIAzureResourceBase.h \
    $${PWD}/OAIDefaultErrorResponse.h \
    $${PWD}/OAIDeploymentScript.h \
    $${PWD}/OAIDeploymentScriptListResult.h \
    $${PWD}/OAIDeploymentScriptPropertiesBase.h \
    $${PWD}/OAIDeploymentScriptUpdateParameter.h \
    $${PWD}/OAIEnvironmentVariable.h \
    $${PWD}/OAILogProperties.h \
    $${PWD}/OAIManagedServiceIdentity.h \
    $${PWD}/OAIScriptConfigurationBase.h \
    $${PWD}/OAIScriptLog.h \
    $${PWD}/OAIScriptLogsList.h \
    $${PWD}/OAIScriptStatus.h \
    $${PWD}/OAIUserAssignedIdentity.h \
# APIs
    $${PWD}/OAIDeploymentScriptsApi.h \
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
    $${PWD}/OAIAzureCliScript.cpp \
    $${PWD}/OAIAzureCliScriptProperties.cpp \
    $${PWD}/OAIAzurePowerShellScript.cpp \
    $${PWD}/OAIAzurePowerShellScriptProperties.cpp \
    $${PWD}/OAIAzureResourceBase.cpp \
    $${PWD}/OAIDefaultErrorResponse.cpp \
    $${PWD}/OAIDeploymentScript.cpp \
    $${PWD}/OAIDeploymentScriptListResult.cpp \
    $${PWD}/OAIDeploymentScriptPropertiesBase.cpp \
    $${PWD}/OAIDeploymentScriptUpdateParameter.cpp \
    $${PWD}/OAIEnvironmentVariable.cpp \
    $${PWD}/OAILogProperties.cpp \
    $${PWD}/OAIManagedServiceIdentity.cpp \
    $${PWD}/OAIScriptConfigurationBase.cpp \
    $${PWD}/OAIScriptLog.cpp \
    $${PWD}/OAIScriptLogsList.cpp \
    $${PWD}/OAIScriptStatus.cpp \
    $${PWD}/OAIUserAssignedIdentity.cpp \
# APIs
    $${PWD}/OAIDeploymentScriptsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
