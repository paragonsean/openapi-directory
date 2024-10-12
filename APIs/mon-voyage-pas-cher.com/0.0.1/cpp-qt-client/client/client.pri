QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirportsSearchResponse.h \
    $${PWD}/OAICitiesData.h \
    $${PWD}/OAICitiesResponse.h \
    $${PWD}/OAIContinentData.h \
    $${PWD}/OAIContinentsResponse.h \
    $${PWD}/OAICountriesData.h \
    $${PWD}/OAICountriesResponse.h \
    $${PWD}/OAIDataAirportsSearch.h \
    $${PWD}/OAIDistanceResponse.h \
    $${PWD}/OAIElevationData.h \
    $${PWD}/OAIElevationResponse.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPongResponse.h \
    $${PWD}/OAISunPositionData.h \
    $${PWD}/OAISunPositionResponse.h \
    $${PWD}/OAITimezoneResponse.h \
    $${PWD}/OAITimezoneResponse_data.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIGeographyAPIsApi.h \
    $${PWD}/OAIServicesAPIsApi.h \
    $${PWD}/OAIUtilitiesAPIsApi.h \
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
    $${PWD}/OAIAirportsSearchResponse.cpp \
    $${PWD}/OAICitiesData.cpp \
    $${PWD}/OAICitiesResponse.cpp \
    $${PWD}/OAIContinentData.cpp \
    $${PWD}/OAIContinentsResponse.cpp \
    $${PWD}/OAICountriesData.cpp \
    $${PWD}/OAICountriesResponse.cpp \
    $${PWD}/OAIDataAirportsSearch.cpp \
    $${PWD}/OAIDistanceResponse.cpp \
    $${PWD}/OAIElevationData.cpp \
    $${PWD}/OAIElevationResponse.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPongResponse.cpp \
    $${PWD}/OAISunPositionData.cpp \
    $${PWD}/OAISunPositionResponse.cpp \
    $${PWD}/OAITimezoneResponse.cpp \
    $${PWD}/OAITimezoneResponse_data.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIGeographyAPIsApi.cpp \
    $${PWD}/OAIServicesAPIsApi.cpp \
    $${PWD}/OAIUtilitiesAPIsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
