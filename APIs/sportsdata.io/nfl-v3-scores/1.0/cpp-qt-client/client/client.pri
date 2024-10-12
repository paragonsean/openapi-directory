QT += network

HEADERS += \
# Models
    $${PWD}/OAIBye.h \
    $${PWD}/OAIDepthChart.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerDetail.h \
    $${PWD}/OAIPlayerSeason.h \
    $${PWD}/OAIReferee.h \
    $${PWD}/OAISchedule.h \
    $${PWD}/OAIScheduleBasic.h \
    $${PWD}/OAIScore.h \
    $${PWD}/OAIScoreBasic.h \
    $${PWD}/OAIScoringDetail.h \
    $${PWD}/OAIStadium.h \
    $${PWD}/OAIStanding.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamBasic.h \
    $${PWD}/OAITeamDepthChart.h \
    $${PWD}/OAITeamGame.h \
    $${PWD}/OAITeamSeason.h \
    $${PWD}/OAITimeframe.h \
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
    $${PWD}/OAIBye.cpp \
    $${PWD}/OAIDepthChart.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerDetail.cpp \
    $${PWD}/OAIPlayerSeason.cpp \
    $${PWD}/OAIReferee.cpp \
    $${PWD}/OAISchedule.cpp \
    $${PWD}/OAIScheduleBasic.cpp \
    $${PWD}/OAIScore.cpp \
    $${PWD}/OAIScoreBasic.cpp \
    $${PWD}/OAIScoringDetail.cpp \
    $${PWD}/OAIStadium.cpp \
    $${PWD}/OAIStanding.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamBasic.cpp \
    $${PWD}/OAITeamDepthChart.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
    $${PWD}/OAITimeframe.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
