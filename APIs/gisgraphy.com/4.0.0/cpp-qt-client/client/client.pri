QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAddressResultsDto.h \
    $${PWD}/OAIFulltextResultsDto.h \
    $${PWD}/OAIGeolocResultsDto.h \
    $${PWD}/OAIGisFeatureDistance.h \
    $${PWD}/OAIHouseNumberDto.h \
    $${PWD}/OAISolrResponseDto.h \
    $${PWD}/OAIStreetDistance.h \
    $${PWD}/OAIStreetSearchResultsDto.h \
# APIs
    $${PWD}/OAIAddressparserStandardizerApi.h \
    $${PWD}/OAIFulltextAutocompleteApi.h \
    $${PWD}/OAIGeocodingApi.h \
    $${PWD}/OAIGeolocalisationApi.h \
    $${PWD}/OAIReversegeocodingApi.h \
    $${PWD}/OAIStreetserviceApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAddressResultsDto.cpp \
    $${PWD}/OAIFulltextResultsDto.cpp \
    $${PWD}/OAIGeolocResultsDto.cpp \
    $${PWD}/OAIGisFeatureDistance.cpp \
    $${PWD}/OAIHouseNumberDto.cpp \
    $${PWD}/OAISolrResponseDto.cpp \
    $${PWD}/OAIStreetDistance.cpp \
    $${PWD}/OAIStreetSearchResultsDto.cpp \
# APIs
    $${PWD}/OAIAddressparserStandardizerApi.cpp \
    $${PWD}/OAIFulltextAutocompleteApi.cpp \
    $${PWD}/OAIGeocodingApi.cpp \
    $${PWD}/OAIGeolocalisationApi.cpp \
    $${PWD}/OAIReversegeocodingApi.cpp \
    $${PWD}/OAIStreetserviceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
