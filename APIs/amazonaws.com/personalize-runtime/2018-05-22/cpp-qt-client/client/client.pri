QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetPersonalizedRankingRequest.h \
    $${PWD}/OAIGetPersonalizedRankingResponse.h \
    $${PWD}/OAIGetPersonalizedRanking_request.h \
    $${PWD}/OAIGetRecommendationsRequest.h \
    $${PWD}/OAIGetRecommendationsResponse.h \
    $${PWD}/OAIGetRecommendations_request.h \
    $${PWD}/OAIPredictedItem.h \
    $${PWD}/OAIPromotion.h \
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
    $${PWD}/OAIGetPersonalizedRankingRequest.cpp \
    $${PWD}/OAIGetPersonalizedRankingResponse.cpp \
    $${PWD}/OAIGetPersonalizedRanking_request.cpp \
    $${PWD}/OAIGetRecommendationsRequest.cpp \
    $${PWD}/OAIGetRecommendationsResponse.cpp \
    $${PWD}/OAIGetRecommendations_request.cpp \
    $${PWD}/OAIPredictedItem.cpp \
    $${PWD}/OAIPromotion.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
