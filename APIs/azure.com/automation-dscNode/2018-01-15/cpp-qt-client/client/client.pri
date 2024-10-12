QT += network

HEADERS += \
# Models
    $${PWD}/OAIAgentRegistration.h \
    $${PWD}/OAIAgentRegistrationInformation_Get_default_response.h \
    $${PWD}/OAIAgentRegistrationKeys.h \
    $${PWD}/OAIAgentRegistrationRegenerateKeyParameter.h \
    $${PWD}/OAIDscMetaConfiguration.h \
    $${PWD}/OAIDscNode.h \
    $${PWD}/OAIDscNodeConfigurationAssociationProperty.h \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.h \
    $${PWD}/OAIDscNodeListResult.h \
    $${PWD}/OAIDscNodeProperties.h \
    $${PWD}/OAIDscNodeReport.h \
    $${PWD}/OAIDscNodeReportListResult.h \
    $${PWD}/OAIDscNodeUpdateParameters.h \
    $${PWD}/OAIDscNodeUpdateParameters_properties.h \
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
    $${PWD}/OAIDscMetaConfiguration.cpp \
    $${PWD}/OAIDscNode.cpp \
    $${PWD}/OAIDscNodeConfigurationAssociationProperty.cpp \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.cpp \
    $${PWD}/OAIDscNodeListResult.cpp \
    $${PWD}/OAIDscNodeProperties.cpp \
    $${PWD}/OAIDscNodeReport.cpp \
    $${PWD}/OAIDscNodeReportListResult.cpp \
    $${PWD}/OAIDscNodeUpdateParameters.cpp \
    $${PWD}/OAIDscNodeUpdateParameters_properties.cpp \
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
