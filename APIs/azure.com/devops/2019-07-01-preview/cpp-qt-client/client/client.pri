QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorization.h \
    $${PWD}/OAIBootstrapConfiguration.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAICodeRepository.h \
    $${PWD}/OAIInputDescriptor.h \
    $${PWD}/OAIInputValue.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplayValue.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOrganizationReference.h \
    $${PWD}/OAIPipeline.h \
    $${PWD}/OAIPipelineListResult.h \
    $${PWD}/OAIPipelineProperties.h \
    $${PWD}/OAIPipelineTemplate.h \
    $${PWD}/OAIPipelineTemplateDefinition.h \
    $${PWD}/OAIPipelineTemplateDefinitionListResult.h \
    $${PWD}/OAIPipelineUpdateParameters.h \
    $${PWD}/OAIProjectReference.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIPipelineTemplateDefinitionsApi.h \
    $${PWD}/OAIPipelinesApi.h \
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
    $${PWD}/OAIAuthorization.cpp \
    $${PWD}/OAIBootstrapConfiguration.cpp \
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAICodeRepository.cpp \
    $${PWD}/OAIInputDescriptor.cpp \
    $${PWD}/OAIInputValue.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplayValue.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOrganizationReference.cpp \
    $${PWD}/OAIPipeline.cpp \
    $${PWD}/OAIPipelineListResult.cpp \
    $${PWD}/OAIPipelineProperties.cpp \
    $${PWD}/OAIPipelineTemplate.cpp \
    $${PWD}/OAIPipelineTemplateDefinition.cpp \
    $${PWD}/OAIPipelineTemplateDefinitionListResult.cpp \
    $${PWD}/OAIPipelineUpdateParameters.cpp \
    $${PWD}/OAIProjectReference.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIPipelineTemplateDefinitionsApi.cpp \
    $${PWD}/OAIPipelinesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
