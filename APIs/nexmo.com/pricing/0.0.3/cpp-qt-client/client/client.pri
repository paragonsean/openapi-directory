QT += network

HEADERS += \
# Models
    $${PWD}/OAICountryObject.h \
    $${PWD}/OAINetworkObject.h \
    $${PWD}/OAIPricingCountriesResponse.h \
    $${PWD}/OAIPricingCountryResponse.h \
    $${PWD}/OAIRetrievePricingAllCountries_400_response.h \
    $${PWD}/OAIRetrievePricingAllCountries_400_response_invalid_parameters.h \
    $${PWD}/OAIRetrievePricingAllCountries_401_response.h \
# APIs
    $${PWD}/OAIPricingApi.h \
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
    $${PWD}/OAICountryObject.cpp \
    $${PWD}/OAINetworkObject.cpp \
    $${PWD}/OAIPricingCountriesResponse.cpp \
    $${PWD}/OAIPricingCountryResponse.cpp \
    $${PWD}/OAIRetrievePricingAllCountries_400_response.cpp \
    $${PWD}/OAIRetrievePricingAllCountries_400_response_invalid_parameters.cpp \
    $${PWD}/OAIRetrievePricingAllCountries_401_response.cpp \
# APIs
    $${PWD}/OAIPricingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
