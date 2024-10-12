QT += network

HEADERS += \
# Models
    $${PWD}/OAICatalogSku.h \
    $${PWD}/OAICommitmentAssociation.h \
    $${PWD}/OAICommitmentAssociationListResult.h \
    $${PWD}/OAICommitmentAssociationProperties.h \
    $${PWD}/OAICommitmentPlan.h \
    $${PWD}/OAICommitmentPlanListResult.h \
    $${PWD}/OAICommitmentPlanPatchPayload.h \
    $${PWD}/OAICommitmentPlanProperties.h \
    $${PWD}/OAIMoveCommitmentAssociationRequest.h \
    $${PWD}/OAIOperationDisplayInfo.h \
    $${PWD}/OAIOperationEntity.h \
    $${PWD}/OAIOperationEntityListResult.h \
    $${PWD}/OAIPlanQuantity.h \
    $${PWD}/OAIPlanUsageHistory.h \
    $${PWD}/OAIPlanUsageHistoryListResult.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceSku.h \
    $${PWD}/OAISkuCapability.h \
    $${PWD}/OAISkuCapacity.h \
    $${PWD}/OAISkuCost.h \
    $${PWD}/OAISkuListResult.h \
    $${PWD}/OAISkuRestrictions.h \
# APIs
    $${PWD}/OAICommitmentAssociationsApi.h \
    $${PWD}/OAICommitmentPlansApi.h \
    $${PWD}/OAIOperationApi.h \
    $${PWD}/OAISkusApi.h \
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
    $${PWD}/OAICatalogSku.cpp \
    $${PWD}/OAICommitmentAssociation.cpp \
    $${PWD}/OAICommitmentAssociationListResult.cpp \
    $${PWD}/OAICommitmentAssociationProperties.cpp \
    $${PWD}/OAICommitmentPlan.cpp \
    $${PWD}/OAICommitmentPlanListResult.cpp \
    $${PWD}/OAICommitmentPlanPatchPayload.cpp \
    $${PWD}/OAICommitmentPlanProperties.cpp \
    $${PWD}/OAIMoveCommitmentAssociationRequest.cpp \
    $${PWD}/OAIOperationDisplayInfo.cpp \
    $${PWD}/OAIOperationEntity.cpp \
    $${PWD}/OAIOperationEntityListResult.cpp \
    $${PWD}/OAIPlanQuantity.cpp \
    $${PWD}/OAIPlanUsageHistory.cpp \
    $${PWD}/OAIPlanUsageHistoryListResult.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceSku.cpp \
    $${PWD}/OAISkuCapability.cpp \
    $${PWD}/OAISkuCapacity.cpp \
    $${PWD}/OAISkuCost.cpp \
    $${PWD}/OAISkuListResult.cpp \
    $${PWD}/OAISkuRestrictions.cpp \
# APIs
    $${PWD}/OAICommitmentAssociationsApi.cpp \
    $${PWD}/OAICommitmentPlansApi.cpp \
    $${PWD}/OAIOperationApi.cpp \
    $${PWD}/OAISkusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
