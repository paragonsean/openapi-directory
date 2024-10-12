QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIError_Source.h \
    $${PWD}/OAIGeoCode.h \
    $${PWD}/OAIGetRecommendedLocation_200_response.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMeta.h \
    $${PWD}/OAIRecommendedLocation.h \
    $${PWD}/OAIWarning.h \
    $${PWD}/OAIWarning_Source.h \
# APIs
    $${PWD}/OAIRecommendedLocationsApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIError_Source.cpp \
    $${PWD}/OAIGeoCode.cpp \
    $${PWD}/OAIGetRecommendedLocation_200_response.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMeta.cpp \
    $${PWD}/OAIRecommendedLocation.cpp \
    $${PWD}/OAIWarning.cpp \
    $${PWD}/OAIWarning_Source.cpp \
# APIs
    $${PWD}/OAIRecommendedLocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
