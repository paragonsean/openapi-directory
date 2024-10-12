QT += network

HEADERS += \
# Models
    $${PWD}/OAIListPlaceActionLinksResponse.h \
    $${PWD}/OAIListPlaceActionTypeMetadataResponse.h \
    $${PWD}/OAIPlaceActionLink.h \
    $${PWD}/OAIPlaceActionTypeMetadata.h \
# APIs
    $${PWD}/OAILocationsApi.h \
    $${PWD}/OAIPlaceActionTypeMetadataApi.h \
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
    $${PWD}/OAIListPlaceActionLinksResponse.cpp \
    $${PWD}/OAIListPlaceActionTypeMetadataResponse.cpp \
    $${PWD}/OAIPlaceActionLink.cpp \
    $${PWD}/OAIPlaceActionTypeMetadata.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
    $${PWD}/OAIPlaceActionTypeMetadataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
