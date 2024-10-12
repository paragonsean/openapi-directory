QT += network

HEADERS += \
# Models
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIAssetCollection.h \
    $${PWD}/OAIAssetContainerSas.h \
    $${PWD}/OAIAssetProperties.h \
    $${PWD}/OAIAssetStorageEncryptionKey.h \
    $${PWD}/OAIAssets_List_default_response.h \
    $${PWD}/OAIAssets_List_default_response_error.h \
    $${PWD}/OAIListContainerSasInput.h \
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
    $${PWD}/OAIAsset.cpp \
    $${PWD}/OAIAssetCollection.cpp \
    $${PWD}/OAIAssetContainerSas.cpp \
    $${PWD}/OAIAssetProperties.cpp \
    $${PWD}/OAIAssetStorageEncryptionKey.cpp \
    $${PWD}/OAIAssets_List_default_response.cpp \
    $${PWD}/OAIAssets_List_default_response_error.cpp \
    $${PWD}/OAIListContainerSasInput.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
