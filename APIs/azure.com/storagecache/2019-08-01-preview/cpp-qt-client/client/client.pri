QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiOperation.h \
    $${PWD}/OAIApiOperationListResult.h \
    $${PWD}/OAIApiOperation_display.h \
    $${PWD}/OAICache.h \
    $${PWD}/OAICacheHealth.h \
    $${PWD}/OAICacheUpgradeStatus.h \
    $${PWD}/OAICache_properties.h \
    $${PWD}/OAICache_sku.h \
    $${PWD}/OAICachesListResult.h \
    $${PWD}/OAIClfsTarget.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAINamespaceJunction.h \
    $${PWD}/OAINfs3Target.h \
    $${PWD}/OAIResourceSku.h \
    $${PWD}/OAIResourceSkuCapabilities.h \
    $${PWD}/OAIResourceSkuLocationInfo.h \
    $${PWD}/OAIResourceSkusResult.h \
    $${PWD}/OAIRestriction.h \
    $${PWD}/OAIStorageTarget.h \
    $${PWD}/OAIStorageTarget_properties.h \
    $${PWD}/OAIStorageTargetsResult.h \
    $${PWD}/OAIUnknownTarget.h \
    $${PWD}/OAIUsageModel.h \
    $${PWD}/OAIUsageModel_display.h \
    $${PWD}/OAIUsageModelsResult.h \
# APIs
    $${PWD}/OAICachesApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAISKUsApi.h \
    $${PWD}/OAIStorageTargetsApi.h \
    $${PWD}/OAIUsageModelsApi.h \
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
    $${PWD}/OAIApiOperation.cpp \
    $${PWD}/OAIApiOperationListResult.cpp \
    $${PWD}/OAIApiOperation_display.cpp \
    $${PWD}/OAICache.cpp \
    $${PWD}/OAICacheHealth.cpp \
    $${PWD}/OAICacheUpgradeStatus.cpp \
    $${PWD}/OAICache_properties.cpp \
    $${PWD}/OAICache_sku.cpp \
    $${PWD}/OAICachesListResult.cpp \
    $${PWD}/OAIClfsTarget.cpp \
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAINamespaceJunction.cpp \
    $${PWD}/OAINfs3Target.cpp \
    $${PWD}/OAIResourceSku.cpp \
    $${PWD}/OAIResourceSkuCapabilities.cpp \
    $${PWD}/OAIResourceSkuLocationInfo.cpp \
    $${PWD}/OAIResourceSkusResult.cpp \
    $${PWD}/OAIRestriction.cpp \
    $${PWD}/OAIStorageTarget.cpp \
    $${PWD}/OAIStorageTarget_properties.cpp \
    $${PWD}/OAIStorageTargetsResult.cpp \
    $${PWD}/OAIUnknownTarget.cpp \
    $${PWD}/OAIUsageModel.cpp \
    $${PWD}/OAIUsageModel_display.cpp \
    $${PWD}/OAIUsageModelsResult.cpp \
# APIs
    $${PWD}/OAICachesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAISKUsApi.cpp \
    $${PWD}/OAIStorageTargetsApi.cpp \
    $${PWD}/OAIUsageModelsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
