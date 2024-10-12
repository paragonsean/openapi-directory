QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIIoTSpacesDescription.h \
    $${PWD}/OAIIoTSpacesDescriptionListResult.h \
    $${PWD}/OAIIoTSpacesNameAvailabilityInfo.h \
    $${PWD}/OAIIoTSpacesPatchDescription.h \
    $${PWD}/OAIIoTSpacesProperties.h \
    $${PWD}/OAIIoTSpacesSkuInfo.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationInputs.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIStorageContainerProperties.h \
# APIs
    $${PWD}/OAICollectionApi.h \
    $${PWD}/OAIProxyApi.h \
    $${PWD}/OAIResourceApi.h \
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
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIIoTSpacesDescription.cpp \
    $${PWD}/OAIIoTSpacesDescriptionListResult.cpp \
    $${PWD}/OAIIoTSpacesNameAvailabilityInfo.cpp \
    $${PWD}/OAIIoTSpacesPatchDescription.cpp \
    $${PWD}/OAIIoTSpacesProperties.cpp \
    $${PWD}/OAIIoTSpacesSkuInfo.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationInputs.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIStorageContainerProperties.cpp \
# APIs
    $${PWD}/OAICollectionApi.cpp \
    $${PWD}/OAIProxyApi.cpp \
    $${PWD}/OAIResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
