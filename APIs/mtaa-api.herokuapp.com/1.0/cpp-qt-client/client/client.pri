QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIDistrictsInRegionApi.h \
    $${PWD}/OAINeighborhoodInAStreetApi.h \
    $${PWD}/OAIStreetsInAWardApi.h \
    $${PWD}/OAITanzaniaRegionsApi.h \
    $${PWD}/OAIWardsInADistrictApi.h \
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
# APIs
    $${PWD}/OAIDistrictsInRegionApi.cpp \
    $${PWD}/OAINeighborhoodInAStreetApi.cpp \
    $${PWD}/OAIStreetsInAWardApi.cpp \
    $${PWD}/OAITanzaniaRegionsApi.cpp \
    $${PWD}/OAIWardsInADistrictApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
