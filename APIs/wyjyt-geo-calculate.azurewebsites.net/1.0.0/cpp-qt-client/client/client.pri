QT += network

HEADERS += \
# Models
    $${PWD}/OAIGeoConvertRequest.h \
    $${PWD}/OAIGeoConvertResponse.h \
    $${PWD}/OAIGeoDistanceRequest.h \
    $${PWD}/OAIGeoDistanceResponse.h \
    $${PWD}/OAIGeoEventDto.h \
    $${PWD}/OAIGeoFenceRequest.h \
    $${PWD}/OAIGeoFenceResponse.h \
    $${PWD}/OAIGeoMoonDto.h \
    $${PWD}/OAIGeoSkyRequest.h \
    $${PWD}/OAIGeoSkyResponse.h \
    $${PWD}/OAIGeoSunDto.h \
    $${PWD}/OAILunarEclipseDetails.h \
    $${PWD}/OAIMoonIllum.h \
    $${PWD}/OAISolarEclipseDetails.h \
    $${PWD}/OAIWyjytErrorResponse.h \
# APIs
    $${PWD}/OAIGeoCalculateApi.h \
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
    $${PWD}/OAIGeoConvertRequest.cpp \
    $${PWD}/OAIGeoConvertResponse.cpp \
    $${PWD}/OAIGeoDistanceRequest.cpp \
    $${PWD}/OAIGeoDistanceResponse.cpp \
    $${PWD}/OAIGeoEventDto.cpp \
    $${PWD}/OAIGeoFenceRequest.cpp \
    $${PWD}/OAIGeoFenceResponse.cpp \
    $${PWD}/OAIGeoMoonDto.cpp \
    $${PWD}/OAIGeoSkyRequest.cpp \
    $${PWD}/OAIGeoSkyResponse.cpp \
    $${PWD}/OAIGeoSunDto.cpp \
    $${PWD}/OAILunarEclipseDetails.cpp \
    $${PWD}/OAIMoonIllum.cpp \
    $${PWD}/OAISolarEclipseDetails.cpp \
    $${PWD}/OAIWyjytErrorResponse.cpp \
# APIs
    $${PWD}/OAIGeoCalculateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
