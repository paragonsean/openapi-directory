QT += network

HEADERS += \
# Models
    $${PWD}/OAIContentHash.h \
    $${PWD}/OAIContentSource.h \
    $${PWD}/OAIDscConfigurationAssociationProperty.h \
    $${PWD}/OAIDscNodeConfiguration.h \
    $${PWD}/OAIDscNodeConfigurationCreateOrUpdateParameters.h \
    $${PWD}/OAIDscNodeConfigurationCreateOrUpdateParametersProperties.h \
    $${PWD}/OAIDscNodeConfigurationListResult.h \
    $${PWD}/OAIDscNodeConfigurationProperties.h \
    $${PWD}/OAIDscNodeConfiguration_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.h \
# APIs
    $${PWD}/OAIDscNodeConfigurationApi.h \
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
    $${PWD}/OAIContentHash.cpp \
    $${PWD}/OAIContentSource.cpp \
    $${PWD}/OAIDscConfigurationAssociationProperty.cpp \
    $${PWD}/OAIDscNodeConfiguration.cpp \
    $${PWD}/OAIDscNodeConfigurationCreateOrUpdateParameters.cpp \
    $${PWD}/OAIDscNodeConfigurationCreateOrUpdateParametersProperties.cpp \
    $${PWD}/OAIDscNodeConfigurationListResult.cpp \
    $${PWD}/OAIDscNodeConfigurationProperties.cpp \
    $${PWD}/OAIDscNodeConfiguration_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIDscNodeExtensionHandlerAssociationProperty.cpp \
# APIs
    $${PWD}/OAIDscNodeConfigurationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
