QT += network

HEADERS += \
# Models
    $${PWD}/OAIGame.h \
    $${PWD}/OAIInning.h \
    $${PWD}/OAINews.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerBasic.h \
    $${PWD}/OAIScheduleBasic.h \
    $${PWD}/OAIScoreBasic.h \
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
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIInning.cpp \
    $${PWD}/OAINews.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerBasic.cpp \
    $${PWD}/OAIScheduleBasic.cpp \
    $${PWD}/OAIScoreBasic.cpp \
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
