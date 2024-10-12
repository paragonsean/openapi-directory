QT += network

HEADERS += \
# Models
    $${PWD}/OAIAd.h \
    $${PWD}/OAIBidPercentages.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIFindListingRecommendationRequest.h \
    $${PWD}/OAIListingRecommendation.h \
    $${PWD}/OAIMarketingRecommendation.h \
    $${PWD}/OAIPagedListingRecommendationCollection.h \
# APIs
    $${PWD}/OAIListingRecommendationApi.h \
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
    $${PWD}/OAIAd.cpp \
    $${PWD}/OAIBidPercentages.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIFindListingRecommendationRequest.cpp \
    $${PWD}/OAIListingRecommendation.cpp \
    $${PWD}/OAIMarketingRecommendation.cpp \
    $${PWD}/OAIPagedListingRecommendationCollection.cpp \
# APIs
    $${PWD}/OAIListingRecommendationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
