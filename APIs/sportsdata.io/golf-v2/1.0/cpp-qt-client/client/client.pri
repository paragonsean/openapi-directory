QT += network

HEADERS += \
# Models
    $${PWD}/OAIDfsSlate.h \
    $${PWD}/OAIDfsSlatePlayer.h \
    $${PWD}/OAIDfsSlateTournament.h \
    $${PWD}/OAIInjury.h \
    $${PWD}/OAILeaderboard.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerHole.h \
    $${PWD}/OAIPlayerRound.h \
    $${PWD}/OAIPlayerSeason.h \
    $${PWD}/OAIPlayerTournament.h \
    $${PWD}/OAIPlayerTournamentProjection.h \
    $${PWD}/OAIRound.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAITournament.h \
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
    $${PWD}/OAIDfsSlate.cpp \
    $${PWD}/OAIDfsSlatePlayer.cpp \
    $${PWD}/OAIDfsSlateTournament.cpp \
    $${PWD}/OAIInjury.cpp \
    $${PWD}/OAILeaderboard.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerHole.cpp \
    $${PWD}/OAIPlayerRound.cpp \
    $${PWD}/OAIPlayerSeason.cpp \
    $${PWD}/OAIPlayerTournament.cpp \
    $${PWD}/OAIPlayerTournamentProjection.cpp \
    $${PWD}/OAIRound.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAITournament.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
