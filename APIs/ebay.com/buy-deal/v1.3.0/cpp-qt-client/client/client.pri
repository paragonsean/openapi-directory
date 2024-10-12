QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAICoupon.h \
    $${PWD}/OAIDealItem.h \
    $${PWD}/OAIDealItemSearchResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIEventItem.h \
    $${PWD}/OAIEventItemSearchResponse.h \
    $${PWD}/OAIEventSearchResponse.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAIMarketingPrice.h \
    $${PWD}/OAIShippingOption.h \
    $${PWD}/OAITerms.h \
# APIs
    $${PWD}/OAIDealItemApi.h \
    $${PWD}/OAIEventApi.h \
    $${PWD}/OAIEventItemApi.h \
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
    $${PWD}/OAICoupon.cpp \
    $${PWD}/OAIDealItem.cpp \
    $${PWD}/OAIDealItemSearchResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIEventItem.cpp \
    $${PWD}/OAIEventItemSearchResponse.cpp \
    $${PWD}/OAIEventSearchResponse.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAIMarketingPrice.cpp \
    $${PWD}/OAIShippingOption.cpp \
    $${PWD}/OAITerms.cpp \
# APIs
    $${PWD}/OAIDealItemApi.cpp \
    $${PWD}/OAIEventApi.cpp \
    $${PWD}/OAIEventItemApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
