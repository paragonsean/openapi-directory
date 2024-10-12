QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAICreateOffersRequest.h \
    $${PWD}/OAIEligibleItem.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIOffer.h \
    $${PWD}/OAIOfferedItem.h \
    $${PWD}/OAIPagedEligibleItemCollection.h \
    $${PWD}/OAISendOfferToInterestedBuyersCollectionResponse.h \
    $${PWD}/OAITimeDuration.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAIOfferApi.h \
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
    $${PWD}/OAICreateOffersRequest.cpp \
    $${PWD}/OAIEligibleItem.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIOffer.cpp \
    $${PWD}/OAIOfferedItem.cpp \
    $${PWD}/OAIPagedEligibleItemCollection.cpp \
    $${PWD}/OAISendOfferToInterestedBuyersCollectionResponse.cpp \
    $${PWD}/OAITimeDuration.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIOfferApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
