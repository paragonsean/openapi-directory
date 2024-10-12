QT += network

HEADERS += \
# Models
    $${PWD}/OAICategory_rated_areas.h \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores.h \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_nightLife.h \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_restaurant.h \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_shopping.h \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_sight.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIError_Source.h \
    $${PWD}/OAIGeoCode.h \
    $${PWD}/OAIGet_category_rated_areas_200_response.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMeta.h \
    $${PWD}/OAIWarning.h \
    $${PWD}/OAIWarning_Source.h \
# APIs
    $${PWD}/OAICategoryRatedAreasApi.h \
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
    $${PWD}/OAICategory_rated_areas.cpp \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores.cpp \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_nightLife.cpp \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_restaurant.cpp \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_shopping.cpp \
    $${PWD}/OAICategory_rated_areas_allOf_categoryScores_sight.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIError_Source.cpp \
    $${PWD}/OAIGeoCode.cpp \
    $${PWD}/OAIGet_category_rated_areas_200_response.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMeta.cpp \
    $${PWD}/OAIWarning.cpp \
    $${PWD}/OAIWarning_Source.cpp \
# APIs
    $${PWD}/OAICategoryRatedAreasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
