QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountEmbeddedObject.h \
    $${PWD}/OAIAccountHalResponse.h \
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAddressWithTimeZone.h \
    $${PWD}/OAIFirstHref.h \
    $${PWD}/OAILastHref.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAILocationEmbeddedObject.h \
    $${PWD}/OAILocationHalResponse.h \
    $${PWD}/OAILocationsEmbeddedObject.h \
    $${PWD}/OAILocationsHalResponse.h \
    $${PWD}/OAINextHref.h \
    $${PWD}/OAIPrevHref.h \
    $${PWD}/OAISelfHref.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccountEmbeddedObject.cpp \
    $${PWD}/OAIAccountHalResponse.cpp \
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAddressWithTimeZone.cpp \
    $${PWD}/OAIFirstHref.cpp \
    $${PWD}/OAILastHref.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILocationEmbeddedObject.cpp \
    $${PWD}/OAILocationHalResponse.cpp \
    $${PWD}/OAILocationsEmbeddedObject.cpp \
    $${PWD}/OAILocationsHalResponse.cpp \
    $${PWD}/OAINextHref.cpp \
    $${PWD}/OAIPrevHref.cpp \
    $${PWD}/OAISelfHref.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
