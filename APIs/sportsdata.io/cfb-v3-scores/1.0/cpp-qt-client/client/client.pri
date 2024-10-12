QT += network

HEADERS += \
# Models
    $${PWD}/OAIConference.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIPeriod.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerBasic.h \
    $${PWD}/OAIScheduleBasic.h \
    $${PWD}/OAISeason.h \
    $${PWD}/OAIStadium.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITeamBasic.h \
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
    $${PWD}/OAIConference.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIPeriod.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerBasic.cpp \
    $${PWD}/OAIScheduleBasic.cpp \
    $${PWD}/OAISeason.cpp \
    $${PWD}/OAIStadium.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITeamBasic.cpp \
    $${PWD}/OAITeamGame.cpp \
    $${PWD}/OAITeamSeason.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
