QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountType.h \
    $${PWD}/OAICreateSlackChannelConfigurationRequest.h \
    $${PWD}/OAICreateSlackChannelConfiguration_request.h \
    $${PWD}/OAIDeleteSlackChannelConfigurationRequest.h \
    $${PWD}/OAIDeleteSlackChannelConfiguration_request.h \
    $${PWD}/OAIDeleteSlackWorkspaceConfigurationRequest.h \
    $${PWD}/OAIDeleteSlackWorkspaceConfiguration_request.h \
    $${PWD}/OAIGetAccountAliasResult.h \
    $${PWD}/OAIListSlackChannelConfigurationsRequest.h \
    $${PWD}/OAIListSlackChannelConfigurationsResult.h \
    $${PWD}/OAIListSlackChannelConfigurations_request.h \
    $${PWD}/OAIListSlackWorkspaceConfigurationsRequest.h \
    $${PWD}/OAIListSlackWorkspaceConfigurationsResult.h \
    $${PWD}/OAINotificationSeverityLevel.h \
    $${PWD}/OAIPutAccountAliasRequest.h \
    $${PWD}/OAIPutAccountAlias_request.h \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganizationRequest.h \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganizationResult.h \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganization_request.h \
    $${PWD}/OAISlackChannelConfiguration.h \
    $${PWD}/OAISlackWorkspaceConfiguration.h \
    $${PWD}/OAIUpdateSlackChannelConfigurationRequest.h \
    $${PWD}/OAIUpdateSlackChannelConfigurationResult.h \
    $${PWD}/OAIUpdateSlackChannelConfiguration_request.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAccountType.cpp \
    $${PWD}/OAICreateSlackChannelConfigurationRequest.cpp \
    $${PWD}/OAICreateSlackChannelConfiguration_request.cpp \
    $${PWD}/OAIDeleteSlackChannelConfigurationRequest.cpp \
    $${PWD}/OAIDeleteSlackChannelConfiguration_request.cpp \
    $${PWD}/OAIDeleteSlackWorkspaceConfigurationRequest.cpp \
    $${PWD}/OAIDeleteSlackWorkspaceConfiguration_request.cpp \
    $${PWD}/OAIGetAccountAliasResult.cpp \
    $${PWD}/OAIListSlackChannelConfigurationsRequest.cpp \
    $${PWD}/OAIListSlackChannelConfigurationsResult.cpp \
    $${PWD}/OAIListSlackChannelConfigurations_request.cpp \
    $${PWD}/OAIListSlackWorkspaceConfigurationsRequest.cpp \
    $${PWD}/OAIListSlackWorkspaceConfigurationsResult.cpp \
    $${PWD}/OAINotificationSeverityLevel.cpp \
    $${PWD}/OAIPutAccountAliasRequest.cpp \
    $${PWD}/OAIPutAccountAlias_request.cpp \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganizationRequest.cpp \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganizationResult.cpp \
    $${PWD}/OAIRegisterSlackWorkspaceForOrganization_request.cpp \
    $${PWD}/OAISlackChannelConfiguration.cpp \
    $${PWD}/OAISlackWorkspaceConfiguration.cpp \
    $${PWD}/OAIUpdateSlackChannelConfigurationRequest.cpp \
    $${PWD}/OAIUpdateSlackChannelConfigurationResult.cpp \
    $${PWD}/OAIUpdateSlackChannelConfiguration_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
