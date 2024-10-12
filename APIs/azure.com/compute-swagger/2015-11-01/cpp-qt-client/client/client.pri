QT += network

HEADERS += \
# Models
    $${PWD}/OAIBasicDependency.h \
    $${PWD}/OAIDependency.h \
    $${PWD}/OAIDeployment.h \
    $${PWD}/OAIDeploymentExtended.h \
    $${PWD}/OAIDeploymentParameters.h \
    $${PWD}/OAIDeploymentParameters_adminPassword.h \
    $${PWD}/OAIDeploymentParameters_adminUsername.h \
    $${PWD}/OAIDeploymentParameters_dnsLabelPrefix.h \
    $${PWD}/OAIDeploymentParameters_osVersion.h \
    $${PWD}/OAIDeploymentProperties.h \
    $${PWD}/OAIDeploymentPropertiesExtended.h \
    $${PWD}/OAIParametersLink.h \
    $${PWD}/OAIProvider.h \
    $${PWD}/OAIProviderResourceType.h \
    $${PWD}/OAITemplateLink.h \
# APIs
    $${PWD}/OAIDeploymentsApi.h \
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
    $${PWD}/OAIBasicDependency.cpp \
    $${PWD}/OAIDependency.cpp \
    $${PWD}/OAIDeployment.cpp \
    $${PWD}/OAIDeploymentExtended.cpp \
    $${PWD}/OAIDeploymentParameters.cpp \
    $${PWD}/OAIDeploymentParameters_adminPassword.cpp \
    $${PWD}/OAIDeploymentParameters_adminUsername.cpp \
    $${PWD}/OAIDeploymentParameters_dnsLabelPrefix.cpp \
    $${PWD}/OAIDeploymentParameters_osVersion.cpp \
    $${PWD}/OAIDeploymentProperties.cpp \
    $${PWD}/OAIDeploymentPropertiesExtended.cpp \
    $${PWD}/OAIParametersLink.cpp \
    $${PWD}/OAIProvider.cpp \
    $${PWD}/OAIProviderResourceType.cpp \
    $${PWD}/OAITemplateLink.cpp \
# APIs
    $${PWD}/OAIDeploymentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
