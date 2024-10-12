QT += network

HEADERS += \
# Models
    $${PWD}/OAIDepthChart.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAIOpponentSeason.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerBasic.h \
    $${PWD}/OAIQuarter.h \
    $${PWD}/OAIReferee.h \
    $${PWD}/OAIScheduleBasic.h \
    $${PWD}/OAIScoreBasic.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAISeries.h \
    $${PWD}/OAIStadium.h \
    $${PWD}/OAIStanding.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamDepthChart.h \
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
    $${PWD}/OAIDepthChart.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAIOpponentSeason.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerBasic.cpp \
    $${PWD}/OAIQuarter.cpp \
    $${PWD}/OAIReferee.cpp \
    $${PWD}/OAIScheduleBasic.cpp \
    $${PWD}/OAIScoreBasic.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAISeries.cpp \
    $${PWD}/OAIStadium.cpp \
    $${PWD}/OAIStanding.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamDepthChart.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
