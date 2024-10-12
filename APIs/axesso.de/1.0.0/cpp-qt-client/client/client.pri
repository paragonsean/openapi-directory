QT += network

HEADERS += \
# Models
    $${PWD}/OAIBuyRecommendationResponse.h \
    $${PWD}/OAIKeywordSearchResponse.h \
    $${PWD}/OAIProductDetailsResponse.h \
    $${PWD}/OAISortOptionResponse.h \
    $${PWD}/OAISortOptionResponse_sortOptions_inner.h \
# APIs
    $${PWD}/OAIAmzApi.h \
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
    $${PWD}/OAIBuyRecommendationResponse.cpp \
    $${PWD}/OAIKeywordSearchResponse.cpp \
    $${PWD}/OAIProductDetailsResponse.cpp \
    $${PWD}/OAISortOptionResponse.cpp \
    $${PWD}/OAISortOptionResponse_sortOptions_inner.cpp \
# APIs
    $${PWD}/OAIAmzApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
