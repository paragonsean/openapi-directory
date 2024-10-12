QT += network

HEADERS += \
# Models
    $${PWD}/OAIBoxScore.h \
    $${PWD}/OAIDfsSlate.h \
    $${PWD}/OAIDfsSlateGame.h \
    $${PWD}/OAIDfsSlatePlayer.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAIOpponentSeason.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGame.h \
    $${PWD}/OAIPlayerInfo.h \
    $${PWD}/OAIPlayerSeason.h \
    $${PWD}/OAIQuarter.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAISeries.h \
    $${PWD}/OAIStadium.h \
    $${PWD}/OAIStanding.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamGame.h \
    $${PWD}/OAITeamSeason.h \
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
    $${PWD}/OAIDfsSlate.cpp \
    $${PWD}/OAIDfsSlateGame.cpp \
    $${PWD}/OAIDfsSlatePlayer.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAIOpponentSeason.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGame.cpp \
    $${PWD}/OAIPlayerInfo.cpp \
    $${PWD}/OAIPlayerSeason.cpp \
    $${PWD}/OAIQuarter.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAISeries.cpp \
    $${PWD}/OAIStadium.cpp \
    $${PWD}/OAIStanding.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
