QT += network

HEADERS += \
# Models
    $${PWD}/OAIArtifact.h \
    $${PWD}/OAIDefinitionTemplates.h \
    $${PWD}/OAIFilter.h \
    $${PWD}/OAIGalleryItem.h \
    $${PWD}/OAIGalleryItemList.h \
    $${PWD}/OAIGalleryItemProperties.h \
    $${PWD}/OAIGalleryItemProperties_iconFileUris.h \
    $${PWD}/OAIGalleryItemUriPayload.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAIImageGroup.h \
    $${PWD}/OAILinkProperties.h \
    $${PWD}/OAIMarketingMaterial.h \
    $${PWD}/OAIOfferDetails.h \
    $${PWD}/OAIOpenProperty.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIProduct.h \
# APIs
    $${PWD}/OAIGalleryItemsApi.h \
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
    $${PWD}/OAIArtifact.cpp \
    $${PWD}/OAIDefinitionTemplates.cpp \
    $${PWD}/OAIFilter.cpp \
    $${PWD}/OAIGalleryItem.cpp \
    $${PWD}/OAIGalleryItemList.cpp \
    $${PWD}/OAIGalleryItemProperties.cpp \
    $${PWD}/OAIGalleryItemProperties_iconFileUris.cpp \
    $${PWD}/OAIGalleryItemUriPayload.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAIImageGroup.cpp \
    $${PWD}/OAILinkProperties.cpp \
    $${PWD}/OAIMarketingMaterial.cpp \
    $${PWD}/OAIOfferDetails.cpp \
    $${PWD}/OAIOpenProperty.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIProduct.cpp \
# APIs
    $${PWD}/OAIGalleryItemsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
