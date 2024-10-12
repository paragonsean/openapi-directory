QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIErrorResponse_error.h \
    $${PWD}/OAIOffer.h \
    $${PWD}/OAIOfferListResponse.h \
    $${PWD}/OAIOfferObject.h \
    $${PWD}/OAIOfferSkuObject.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIPrivateStoreList.h \
    $${PWD}/OAIPrivateStoreProperties.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIPrivateStoresApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIErrorResponse_error.cpp \
    $${PWD}/OAIOffer.cpp \
    $${PWD}/OAIOfferListResponse.cpp \
    $${PWD}/OAIOfferObject.cpp \
    $${PWD}/OAIOfferSkuObject.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIPrivateStoreList.cpp \
    $${PWD}/OAIPrivateStoreProperties.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIPrivateStoresApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
