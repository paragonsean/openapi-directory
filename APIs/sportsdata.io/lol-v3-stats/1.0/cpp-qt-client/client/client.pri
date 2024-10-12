QT += network

HEADERS += \
# Models
    $${PWD}/OAIArea.h \
    $${PWD}/OAIBoxScore.h \
    $${PWD}/OAIChampion.h \
    $${PWD}/OAIChampionInfo.h \
    $${PWD}/OAICompetition.h \
    $${PWD}/OAICompetitionDetail.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIMatch.h \
    $${PWD}/OAIMatchBan.h \
    $${PWD}/OAIMembership.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGame.h \
    $${PWD}/OAIPlayerMatch.h \
    $${PWD}/OAIRound.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAISeasonTeam.h \
    $${PWD}/OAISpell.h \
    $${PWD}/OAIStanding.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamDetail.h \
    $${PWD}/OAITeamGame.h \
    $${PWD}/OAITeamMatch.h \
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
    $${PWD}/OAIBoxScore.cpp \
    $${PWD}/OAIChampion.cpp \
    $${PWD}/OAIChampionInfo.cpp \
    $${PWD}/OAICompetition.cpp \
    $${PWD}/OAICompetitionDetail.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIMatch.cpp \
    $${PWD}/OAIMatchBan.cpp \
    $${PWD}/OAIMembership.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGame.cpp \
    $${PWD}/OAIPlayerMatch.cpp \
    $${PWD}/OAIRound.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAISeasonTeam.cpp \
    $${PWD}/OAISpell.cpp \
    $${PWD}/OAIStanding.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamDetail.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamMatch.cpp \
    $${PWD}/OAIVenue.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
