QT += network

HEADERS += \
# Models
    $${PWD}/OAIBaseIndexResponse.h \
    $${PWD}/OAIBaseIndexResponse__links.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAIPagination.h \
    $${PWD}/OAIPersona.h \
    $${PWD}/OAIPersona__links.h \
    $${PWD}/OAIPlaylist.h \
    $${PWD}/OAIPlaylist__links.h \
    $${PWD}/OAIShow.h \
    $${PWD}/OAIShow__links.h \
    $${PWD}/OAISpin.h \
    $${PWD}/OAISpin__links.h \
    $${PWD}/OAIValidationError.h \
    $${PWD}/OAI_personas_get_200_response.h \
    $${PWD}/OAI_playlists_get_200_response.h \
    $${PWD}/OAI_shows_get_200_response.h \
    $${PWD}/OAI_spins_get_200_response.h \
# APIs
    $${PWD}/OAIPersonaApi.h \
    $${PWD}/OAIPlaylistApi.h \
    $${PWD}/OAIShowApi.h \
    $${PWD}/OAISpinApi.h \
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
    $${PWD}/OAIBaseIndexResponse.cpp \
    $${PWD}/OAIBaseIndexResponse__links.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAIPagination.cpp \
    $${PWD}/OAIPersona.cpp \
    $${PWD}/OAIPersona__links.cpp \
    $${PWD}/OAIPlaylist.cpp \
    $${PWD}/OAIPlaylist__links.cpp \
    $${PWD}/OAIShow.cpp \
    $${PWD}/OAIShow__links.cpp \
    $${PWD}/OAISpin.cpp \
    $${PWD}/OAISpin__links.cpp \
    $${PWD}/OAIValidationError.cpp \
    $${PWD}/OAI_personas_get_200_response.cpp \
    $${PWD}/OAI_playlists_get_200_response.cpp \
    $${PWD}/OAI_shows_get_200_response.cpp \
    $${PWD}/OAI_spins_get_200_response.cpp \
# APIs
    $${PWD}/OAIPersonaApi.cpp \
    $${PWD}/OAIPlaylistApi.cpp \
    $${PWD}/OAIShowApi.cpp \
    $${PWD}/OAISpinApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
