QT += network

HEADERS += \
# Models
    $${PWD}/OAIArtistData.h \
    $${PWD}/OAIEventData.h \
    $${PWD}/OAIOfferData.h \
    $${PWD}/OAIVenueData.h \
# APIs
    $${PWD}/OAIArtistEventsApi.h \
    $${PWD}/OAIArtistInformationApi.h \
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
    $${PWD}/OAIArtistData.cpp \
    $${PWD}/OAIEventData.cpp \
    $${PWD}/OAIOfferData.cpp \
    $${PWD}/OAIVenueData.cpp \
# APIs
    $${PWD}/OAIArtistEventsApi.cpp \
    $${PWD}/OAIArtistInformationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
