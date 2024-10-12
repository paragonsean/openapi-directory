QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplication.h \
    $${PWD}/OAIApplicationArtifact.h \
    $${PWD}/OAIApplicationArtifactType.h \
    $${PWD}/OAIApplicationDefinition.h \
    $${PWD}/OAIApplicationDefinitionListResult.h \
    $${PWD}/OAIApplicationDefinitionProperties.h \
    $${PWD}/OAIApplicationListResult.h \
    $${PWD}/OAIApplicationLockLevel.h \
    $${PWD}/OAIApplicationPatchable.h \
    $${PWD}/OAIApplicationProperties.h \
    $${PWD}/OAIApplicationPropertiesPatchable.h \
    $${PWD}/OAIApplicationProviderAuthorization.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIGenericResource.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIPlanPatchable.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIApplicationDefinitionsApi.h \
    $${PWD}/OAIApplicationsApi.h \
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
    $${PWD}/OAIApplication.cpp \
    $${PWD}/OAIApplicationArtifact.cpp \
    $${PWD}/OAIApplicationArtifactType.cpp \
    $${PWD}/OAIApplicationDefinition.cpp \
    $${PWD}/OAIApplicationDefinitionListResult.cpp \
    $${PWD}/OAIApplicationDefinitionProperties.cpp \
    $${PWD}/OAIApplicationListResult.cpp \
    $${PWD}/OAIApplicationLockLevel.cpp \
    $${PWD}/OAIApplicationPatchable.cpp \
    $${PWD}/OAIApplicationProperties.cpp \
    $${PWD}/OAIApplicationPropertiesPatchable.cpp \
    $${PWD}/OAIApplicationProviderAuthorization.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIGenericResource.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIPlanPatchable.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIApplicationDefinitionsApi.cpp \
    $${PWD}/OAIApplicationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
