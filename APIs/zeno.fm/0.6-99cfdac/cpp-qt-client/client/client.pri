QT += network

HEADERS += \
# Models
    $${PWD}/OAICountry.h \
    $${PWD}/OAILanguage.h \
    $${PWD}/OAIPodcast.h \
    $${PWD}/OAIPodcastCategory.h \
    $${PWD}/OAIPodcastEpisode.h \
    $${PWD}/OAIPodcastEpisodeList.h \
    $${PWD}/OAIPodcastFilters.h \
    $${PWD}/OAIPodcastSearchParams.h \
    $${PWD}/OAIPodcastSearchResults.h \
    $${PWD}/OAIStation.h \
    $${PWD}/OAIStationFilters.h \
    $${PWD}/OAIStationGenre.h \
    $${PWD}/OAIStationList.h \
    $${PWD}/OAIStationSearchParams.h \
    $${PWD}/OAIStationSearchResults.h \
# APIs
    $${PWD}/OAIAPIV2Api.h \
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
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAILanguage.cpp \
    $${PWD}/OAIPodcast.cpp \
    $${PWD}/OAIPodcastCategory.cpp \
    $${PWD}/OAIPodcastEpisode.cpp \
    $${PWD}/OAIPodcastEpisodeList.cpp \
    $${PWD}/OAIPodcastFilters.cpp \
    $${PWD}/OAIPodcastSearchParams.cpp \
    $${PWD}/OAIPodcastSearchResults.cpp \
    $${PWD}/OAIStation.cpp \
    $${PWD}/OAIStationFilters.cpp \
    $${PWD}/OAIStationGenre.cpp \
    $${PWD}/OAIStationList.cpp \
    $${PWD}/OAIStationSearchParams.cpp \
    $${PWD}/OAIStationSearchResults.cpp \
# APIs
    $${PWD}/OAIAPIV2Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
