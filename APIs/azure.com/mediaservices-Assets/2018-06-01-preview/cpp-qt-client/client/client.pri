QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIAssetCollection.h \
    $${PWD}/OAIAssetContainerSas.h \
    $${PWD}/OAIAssetProperties.h \
    $${PWD}/OAIAssetStorageEncryptionKey.h \
    $${PWD}/OAIListContainerSasInput.h \
    $${PWD}/OAIODataError.h \
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
    $${PWD}/OAIAssetProperties.cpp \
    $${PWD}/OAIAssetStorageEncryptionKey.cpp \
    $${PWD}/OAIListContainerSasInput.cpp \
    $${PWD}/OAIODataError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
