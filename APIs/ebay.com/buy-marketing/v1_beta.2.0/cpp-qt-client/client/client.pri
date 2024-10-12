QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIBestSellingProductResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAIMarketPriceDetail.h \
    $${PWD}/OAIMerchandisedProduct.h \
    $${PWD}/OAIRatingAspect.h \
    $${PWD}/OAIRatingAspectDistribution.h \
# APIs
    $${PWD}/OAIMerchandisedProductApi.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIBestSellingProductResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAIMarketPriceDetail.cpp \
    $${PWD}/OAIMerchandisedProduct.cpp \
    $${PWD}/OAIRatingAspect.cpp \
    $${PWD}/OAIRatingAspectDistribution.cpp \
# APIs
    $${PWD}/OAIMerchandisedProductApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
