QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirport.h \
    $${PWD}/OAIAirportResource.h \
    $${PWD}/OAIAirportResource_Airports.h \
    $${PWD}/OAIAirportResource_Meta.h \
    $${PWD}/OAIAirportResponse.h \
    $${PWD}/OAIAirport_Names.h \
    $${PWD}/OAIAirport_Position.h \
    $${PWD}/OAICoordinate.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAIName.h \
# APIs
    $${PWD}/OAICargoApi.h \
    $${PWD}/OAIOffersApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIReferenceDataApi.h \
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
    $${PWD}/OAIAirport.cpp \
    $${PWD}/OAIAirportResource.cpp \
    $${PWD}/OAIAirportResource_Airports.cpp \
    $${PWD}/OAIAirportResource_Meta.cpp \
    $${PWD}/OAIAirportResponse.cpp \
    $${PWD}/OAIAirport_Names.cpp \
    $${PWD}/OAIAirport_Position.cpp \
    $${PWD}/OAICoordinate.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAIName.cpp \
# APIs
    $${PWD}/OAICargoApi.cpp \
    $${PWD}/OAIOffersApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIReferenceDataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
