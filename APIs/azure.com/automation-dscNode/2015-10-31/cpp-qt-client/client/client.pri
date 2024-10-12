QT += network

HEADERS += \
# Models
    $${PWD}/OAIAgentRegistration.h \
    $${PWD}/OAIAgentRegistrationInformation_Get_default_response.h \
    $${PWD}/OAIAgentRegistrationKeys.h \
    $${PWD}/OAIAgentRegistrationRegenerateKeyParameter.h \
    $${PWD}/OAIDscConfigurationAssociationProperty.h \
    $${PWD}/OAIDscMetaConfiguration.h \
    $${PWD}/OAIDscNode.h \
    $${PWD}/OAIDscNodeConfigurationAssociationProperty.h \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.h \
    $${PWD}/OAIDscNodeListResult.h \
    $${PWD}/OAIDscNodeReport.h \
    $${PWD}/OAIDscNodeReportListResult.h \
    $${PWD}/OAIDscNodeUpdateParameters.h \
    $${PWD}/OAIDscReportError.h \
    $${PWD}/OAIDscReportResource.h \
    $${PWD}/OAIDscReportResourceNavigation.h \
# APIs
    $${PWD}/OAIAgentRegistrationInformationApi.h \
    $${PWD}/OAIDscNodeApi.h \
    $${PWD}/OAINodeReportsApi.h \
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
    $${PWD}/OAIAgentRegistration.cpp \
    $${PWD}/OAIAgentRegistrationInformation_Get_default_response.cpp \
    $${PWD}/OAIAgentRegistrationKeys.cpp \
    $${PWD}/OAIAgentRegistrationRegenerateKeyParameter.cpp \
    $${PWD}/OAIDscConfigurationAssociationProperty.cpp \
    $${PWD}/OAIDscMetaConfiguration.cpp \
    $${PWD}/OAIDscNode.cpp \
    $${PWD}/OAIDscNodeConfigurationAssociationProperty.cpp \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.cpp \
    $${PWD}/OAIDscNodeListResult.cpp \
    $${PWD}/OAIDscNodeReport.cpp \
    $${PWD}/OAIDscNodeReportListResult.cpp \
    $${PWD}/OAIDscNodeUpdateParameters.cpp \
    $${PWD}/OAIDscReportError.cpp \
    $${PWD}/OAIDscReportResource.cpp \
    $${PWD}/OAIDscReportResourceNavigation.cpp \
# APIs
    $${PWD}/OAIAgentRegistrationInformationApi.cpp \
    $${PWD}/OAIDscNodeApi.cpp \
    $${PWD}/OAINodeReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
