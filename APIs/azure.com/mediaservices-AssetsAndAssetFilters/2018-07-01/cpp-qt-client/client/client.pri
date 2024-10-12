QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIAssetCollection.h \
    $${PWD}/OAIAssetContainerSas.h \
    $${PWD}/OAIAssetFileEncryptionMetadata.h \
    $${PWD}/OAIAssetFilter.h \
    $${PWD}/OAIAssetFilterCollection.h \
    $${PWD}/OAIAssetProperties.h \
    $${PWD}/OAIAssetStreamingLocator.h \
    $${PWD}/OAIFilterTrackPropertyCondition.h \
    $${PWD}/OAIFilterTrackSelection.h \
    $${PWD}/OAIFirstQuality.h \
    $${PWD}/OAIListContainerSasInput.h \
    $${PWD}/OAIListStreamingLocatorsResponse.h \
    $${PWD}/OAIMediaFilterProperties.h \
    $${PWD}/OAIODataError.h \
    $${PWD}/OAIPresentationTimeRange.h \
    $${PWD}/OAIStorageEncryptedAssetDecryptionData.h \
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
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIAsset.cpp \
    $${PWD}/OAIAssetCollection.cpp \
    $${PWD}/OAIAssetContainerSas.cpp \
    $${PWD}/OAIAssetFileEncryptionMetadata.cpp \
    $${PWD}/OAIAssetFilter.cpp \
    $${PWD}/OAIAssetFilterCollection.cpp \
    $${PWD}/OAIAssetProperties.cpp \
    $${PWD}/OAIAssetStreamingLocator.cpp \
    $${PWD}/OAIFilterTrackPropertyCondition.cpp \
    $${PWD}/OAIFilterTrackSelection.cpp \
    $${PWD}/OAIFirstQuality.cpp \
    $${PWD}/OAIListContainerSasInput.cpp \
    $${PWD}/OAIListStreamingLocatorsResponse.cpp \
    $${PWD}/OAIMediaFilterProperties.cpp \
    $${PWD}/OAIODataError.cpp \
    $${PWD}/OAIPresentationTimeRange.cpp \
    $${PWD}/OAIStorageEncryptedAssetDecryptionData.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
