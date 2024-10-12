QT += network

HEADERS += \
# Models
    $${PWD}/OAIARMErrorResponseBody.h \
    $${PWD}/OAIArmErrorResponse.h \
    $${PWD}/OAIConfigData.h \
    $${PWD}/OAIConfigDataProperties.h \
    $${PWD}/OAIConfigurationListResult.h \
    $${PWD}/OAIDigestConfig.h \
    $${PWD}/OAIMetadataEntity.h \
    $${PWD}/OAIMetadataEntityListResult.h \
    $${PWD}/OAIMetadataEntityProperties.h \
    $${PWD}/OAIMetadataSupportedValueDetail.h \
    $${PWD}/OAIOperationDisplayInfo.h \
    $${PWD}/OAIOperationEntity.h \
    $${PWD}/OAIOperationEntityListResult.h \
    $${PWD}/OAIRecommendationProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceRecommendationBase.h \
    $${PWD}/OAIResourceRecommendationBaseListResult.h \
    $${PWD}/OAIShortDescription.h \
    $${PWD}/OAISuppressionContract.h \
    $${PWD}/OAISuppressionContractListResult.h \
    $${PWD}/OAISuppressionProperties.h \
# APIs
    $${PWD}/OAIConfigurationsApi.h \
    $${PWD}/OAIGenerateRecommendationsApi.h \
    $${PWD}/OAIGetRecommendationsApi.h \
    $${PWD}/OAIMetadataApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAISuppressionsApi.h \
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
    $${PWD}/OAIARMErrorResponseBody.cpp \
    $${PWD}/OAIArmErrorResponse.cpp \
    $${PWD}/OAIConfigData.cpp \
    $${PWD}/OAIConfigDataProperties.cpp \
    $${PWD}/OAIConfigurationListResult.cpp \
    $${PWD}/OAIDigestConfig.cpp \
    $${PWD}/OAIMetadataEntity.cpp \
    $${PWD}/OAIMetadataEntityListResult.cpp \
    $${PWD}/OAIMetadataEntityProperties.cpp \
    $${PWD}/OAIMetadataSupportedValueDetail.cpp \
    $${PWD}/OAIOperationDisplayInfo.cpp \
    $${PWD}/OAIOperationEntity.cpp \
    $${PWD}/OAIOperationEntityListResult.cpp \
    $${PWD}/OAIRecommendationProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceRecommendationBase.cpp \
    $${PWD}/OAIResourceRecommendationBaseListResult.cpp \
    $${PWD}/OAIShortDescription.cpp \
    $${PWD}/OAISuppressionContract.cpp \
    $${PWD}/OAISuppressionContractListResult.cpp \
    $${PWD}/OAISuppressionProperties.cpp \
# APIs
    $${PWD}/OAIConfigurationsApi.cpp \
    $${PWD}/OAIGenerateRecommendationsApi.cpp \
    $${PWD}/OAIGetRecommendationsApi.cpp \
    $${PWD}/OAIMetadataApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAISuppressionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
