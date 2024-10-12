QT += network

HEADERS += \
# Models
    $${PWD}/OAIBoxScore.h \
    $${PWD}/OAIConference.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIPeriod.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGame.h \
    $${PWD}/OAIPlayerGameProjection.h \
    $${PWD}/OAIPlayerSeason.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAIStadium.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamGame.h \
    $${PWD}/OAITeamSeason.h \
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
    $${PWD}/OAIBoxScore.cpp \
    $${PWD}/OAIConference.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIPeriod.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGame.cpp \
    $${PWD}/OAIPlayerGameProjection.cpp \
    $${PWD}/OAIPlayerSeason.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAIStadium.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
    $${PWD}/OAITournament.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
