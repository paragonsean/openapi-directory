QT += network

HEADERS += \
# Models
    $${PWD}/OAIArea.h \
    $${PWD}/OAICanceledMembership.h \
    $${PWD}/OAICompetition.h \
    $${PWD}/OAICompetitionDetail.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIMembership.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerSeason.h \
    $${PWD}/OAIPlayoffAggregateScore.h \
    $${PWD}/OAIRound.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAISeasonTeam.h \
    $${PWD}/OAIStanding.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamDetail.h \
    $${PWD}/OAITeamGame.h \
    $${PWD}/OAITeamSeason.h \
    $${PWD}/OAIVenue.h \
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
    $${PWD}/OAIArea.cpp \
    $${PWD}/OAICanceledMembership.cpp \
    $${PWD}/OAICompetition.cpp \
    $${PWD}/OAICompetitionDetail.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIMembership.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerSeason.cpp \
    $${PWD}/OAIPlayoffAggregateScore.cpp \
    $${PWD}/OAIRound.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAISeasonTeam.cpp \
    $${PWD}/OAIStanding.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamDetail.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
    $${PWD}/OAIVenue.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
