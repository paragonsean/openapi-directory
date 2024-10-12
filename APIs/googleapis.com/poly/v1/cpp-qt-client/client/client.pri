QT += network

HEADERS += \
# Models
    $${PWD}/OAIAsset.h \
    $${PWD}/OAIAssetImportMessage.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIFormat.h \
    $${PWD}/OAIFormatComplexity.h \
    $${PWD}/OAIImageError.h \
    $${PWD}/OAIListAssetsResponse.h \
    $${PWD}/OAIListLikedAssetsResponse.h \
    $${PWD}/OAIListUserAssetsResponse.h \
    $${PWD}/OAIObjParseError.h \
    $${PWD}/OAIPresentationParams.h \
    $${PWD}/OAIQuaternion.h \
    $${PWD}/OAIRemixInfo.h \
    $${PWD}/OAIStartAssetImportResponse.h \
    $${PWD}/OAIUserAsset.h \
# APIs
    $${PWD}/OAIAssetsApi.h \
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIAssetImportMessage.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIFormat.cpp \
    $${PWD}/OAIFormatComplexity.cpp \
    $${PWD}/OAIImageError.cpp \
    $${PWD}/OAIListAssetsResponse.cpp \
    $${PWD}/OAIListLikedAssetsResponse.cpp \
    $${PWD}/OAIListUserAssetsResponse.cpp \
    $${PWD}/OAIObjParseError.cpp \
    $${PWD}/OAIPresentationParams.cpp \
    $${PWD}/OAIQuaternion.cpp \
    $${PWD}/OAIRemixInfo.cpp \
    $${PWD}/OAIStartAssetImportResponse.cpp \
    $${PWD}/OAIUserAsset.cpp \
# APIs
    $${PWD}/OAIAssetsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
