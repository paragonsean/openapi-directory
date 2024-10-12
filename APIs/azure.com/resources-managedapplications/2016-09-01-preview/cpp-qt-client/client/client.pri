QT += network

HEADERS += \
# Models
    $${PWD}/OAIAppliance.h \
    $${PWD}/OAIApplianceArtifact.h \
    $${PWD}/OAIApplianceArtifactType.h \
    $${PWD}/OAIApplianceDefinition.h \
    $${PWD}/OAIApplianceDefinitionListResult.h \
    $${PWD}/OAIApplianceDefinitionProperties.h \
    $${PWD}/OAIApplianceListResult.h \
    $${PWD}/OAIApplianceLockLevel.h \
    $${PWD}/OAIAppliancePatchable.h \
    $${PWD}/OAIApplianceProperties.h \
    $${PWD}/OAIAppliancePropertiesPatchable.h \
    $${PWD}/OAIApplianceProviderAuthorization.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIGenericResource.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIPlanPatchable.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIApplianceDefinitionsApi.h \
    $${PWD}/OAIAppliancesApi.h \
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
    $${PWD}/OAIAppliance.cpp \
    $${PWD}/OAIApplianceArtifact.cpp \
    $${PWD}/OAIApplianceArtifactType.cpp \
    $${PWD}/OAIApplianceDefinition.cpp \
    $${PWD}/OAIApplianceDefinitionListResult.cpp \
    $${PWD}/OAIApplianceDefinitionProperties.cpp \
    $${PWD}/OAIApplianceListResult.cpp \
    $${PWD}/OAIApplianceLockLevel.cpp \
    $${PWD}/OAIAppliancePatchable.cpp \
    $${PWD}/OAIApplianceProperties.cpp \
    $${PWD}/OAIAppliancePropertiesPatchable.cpp \
    $${PWD}/OAIApplianceProviderAuthorization.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIGenericResource.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIPlanPatchable.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIApplianceDefinitionsApi.cpp \
    $${PWD}/OAIAppliancesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
