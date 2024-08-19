QT += network

HEADERS += \
# Models
    $${PWD}/OAIRecommendation.h \
    $${PWD}/OAIRecommendationCollection.h \
    $${PWD}/OAIRecommendationRule.h \
# APIs
    $${PWD}/OAIRecommendationsApi.h \
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
    $${PWD}/OAIRecommendation.cpp \
    $${PWD}/OAIRecommendationCollection.cpp \
    $${PWD}/OAIRecommendationRule.cpp \
# APIs
    $${PWD}/OAIRecommendationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
