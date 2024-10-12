QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiKey.h \
    $${PWD}/OAIApiKeyListResult.h \
    $${PWD}/OAICheckNameAvailabilityParameters.h \
    $${PWD}/OAIConfigurationStore.h \
    $${PWD}/OAIConfigurationStoreListResult.h \
    $${PWD}/OAIConfigurationStoreProperties.h \
    $${PWD}/OAIConfigurationStoreUpdateParameters.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIKeyValue.h \
    $${PWD}/OAIListKeyValueParameters.h \
    $${PWD}/OAINameAvailabilityStatus.h \
    $${PWD}/OAIOperationDefinition.h \
    $${PWD}/OAIOperationDefinitionDisplay.h \
    $${PWD}/OAIOperationDefinitionListResult.h \
    $${PWD}/OAIRegenerateKeyParameters.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceIdentity.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAIUserIdentity.h \
# APIs
    $${PWD}/OAIConfigurationStoresApi.h \
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
    $${PWD}/OAIApiKey.cpp \
    $${PWD}/OAIApiKeyListResult.cpp \
    $${PWD}/OAICheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIConfigurationStore.cpp \
    $${PWD}/OAIConfigurationStoreListResult.cpp \
    $${PWD}/OAIConfigurationStoreProperties.cpp \
    $${PWD}/OAIConfigurationStoreUpdateParameters.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIKeyValue.cpp \
    $${PWD}/OAIListKeyValueParameters.cpp \
    $${PWD}/OAINameAvailabilityStatus.cpp \
    $${PWD}/OAIOperationDefinition.cpp \
    $${PWD}/OAIOperationDefinitionDisplay.cpp \
    $${PWD}/OAIOperationDefinitionListResult.cpp \
    $${PWD}/OAIRegenerateKeyParameters.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceIdentity.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAIUserIdentity.cpp \
# APIs
    $${PWD}/OAIConfigurationStoresApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
