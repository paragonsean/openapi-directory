QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirportsAPI_Controllers_AirportDetailsController_Response.h \
    $${PWD}/OAIAirportsAPI_Controllers_AirportIATAController_Response.h \
    $${PWD}/OAIAirportsAPI_Controllers_AutoCompleteAirportNameController_Response.h \
    $${PWD}/OAIAirportsAPI_Controllers_CountryAirportListController_AirportListResponse.h \
    $${PWD}/OAIAirportsAPI_Controllers_CountryListController_CountryListResponse.h \
    $${PWD}/OAIAirportsAPI_Controllers_NearestAirportsController_Response.h \
    $${PWD}/OAIAirportsAPI_Models_Airport.h \
    $${PWD}/OAIAirportsAPI_Models_AirportList.h \
    $${PWD}/OAIAirportsAPI_Models_AirportListAutocomplete.h \
    $${PWD}/OAIAirportsAPI_Models_Country.h \
    $${PWD}/OAIAirportsAPI_Models_Frequency.h \
    $${PWD}/OAIAirportsAPI_Models_Location_Country.h \
    $${PWD}/OAIAirportsAPI_Models_Location_Region.h \
    $${PWD}/OAIAirportsAPI_Models_Runway.h \
# APIs
    $${PWD}/OAIAirportDetailsApi.h \
    $${PWD}/OAIAirportIATAApi.h \
    $${PWD}/OAIAutoCompleteAirportNameApi.h \
    $${PWD}/OAICountryAirportListApi.h \
    $${PWD}/OAICountryListApi.h \
    $${PWD}/OAINearestAirportsApi.h \
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
    $${PWD}/OAIAirportsAPI_Controllers_AirportDetailsController_Response.cpp \
    $${PWD}/OAIAirportsAPI_Controllers_AirportIATAController_Response.cpp \
    $${PWD}/OAIAirportsAPI_Controllers_AutoCompleteAirportNameController_Response.cpp \
    $${PWD}/OAIAirportsAPI_Controllers_CountryAirportListController_AirportListResponse.cpp \
    $${PWD}/OAIAirportsAPI_Controllers_CountryListController_CountryListResponse.cpp \
    $${PWD}/OAIAirportsAPI_Controllers_NearestAirportsController_Response.cpp \
    $${PWD}/OAIAirportsAPI_Models_Airport.cpp \
    $${PWD}/OAIAirportsAPI_Models_AirportList.cpp \
    $${PWD}/OAIAirportsAPI_Models_AirportListAutocomplete.cpp \
    $${PWD}/OAIAirportsAPI_Models_Country.cpp \
    $${PWD}/OAIAirportsAPI_Models_Frequency.cpp \
    $${PWD}/OAIAirportsAPI_Models_Location_Country.cpp \
    $${PWD}/OAIAirportsAPI_Models_Location_Region.cpp \
    $${PWD}/OAIAirportsAPI_Models_Runway.cpp \
# APIs
    $${PWD}/OAIAirportDetailsApi.cpp \
    $${PWD}/OAIAirportIATAApi.cpp \
    $${PWD}/OAIAutoCompleteAirportNameApi.cpp \
    $${PWD}/OAICountryAirportListApi.cpp \
    $${PWD}/OAICountryListApi.cpp \
    $${PWD}/OAINearestAirportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
