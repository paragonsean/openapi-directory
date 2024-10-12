QT += network

HEADERS += \
# Models
    $${PWD}/OAIDepthChart.h \
    $${PWD}/OAIDfsSlate.h \
    $${PWD}/OAIDfsSlateGame.h \
    $${PWD}/OAIDfsSlatePlayer.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIInning.h \
    $${PWD}/OAILineup.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGameProjection.h \
    $${PWD}/OAIPlayerSeasonProjection.h \
    $${PWD}/OAISeries.h \
    $${PWD}/OAIStartingLineups.h \
    $${PWD}/OAITeamDepthChart.h \
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
    $${PWD}/OAIDfsSlate.cpp \
    $${PWD}/OAIDfsSlateGame.cpp \
    $${PWD}/OAIDfsSlatePlayer.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIInning.cpp \
    $${PWD}/OAILineup.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGameProjection.cpp \
    $${PWD}/OAIPlayerSeasonProjection.cpp \
    $${PWD}/OAISeries.cpp \
    $${PWD}/OAIStartingLineups.cpp \
    $${PWD}/OAITeamDepthChart.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
