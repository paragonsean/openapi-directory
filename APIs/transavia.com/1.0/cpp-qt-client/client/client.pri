QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirportDetailsDto.h \
    $${PWD}/OAIAirportDto.h \
    $${PWD}/OAIBadRequestResponse.h \
    $${PWD}/OAICountry.h \
    $${PWD}/OAIGeoCoordinates.h \
    $${PWD}/OAIInternalServerErrorResponse.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAINearestAirportDto.h \
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
    $${PWD}/OAIAirportDetailsDto.cpp \
    $${PWD}/OAIAirportDto.cpp \
    $${PWD}/OAIBadRequestResponse.cpp \
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAIGeoCoordinates.cpp \
    $${PWD}/OAIInternalServerErrorResponse.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAINearestAirportDto.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
