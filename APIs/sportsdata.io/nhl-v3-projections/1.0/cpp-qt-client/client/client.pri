QT += network

HEADERS += \
# Models
    $${PWD}/OAIDfsSlate.h \
    $${PWD}/OAIDfsSlateGame.h \
    $${PWD}/OAIDfsSlatePlayer.h \
    $${PWD}/OAIGame.h \
    $${PWD}/OAIGoaltender.h \
    $${PWD}/OAIPenalty.h \
    $${PWD}/OAIPeriod.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGameProjection.h \
    $${PWD}/OAIScoringPlay.h \
    $${PWD}/OAISeries.h \
    $${PWD}/OAIStartingGoaltenders.h \
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
    $${PWD}/OAIDfsSlateGame.cpp \
    $${PWD}/OAIDfsSlatePlayer.cpp \
    $${PWD}/OAIGame.cpp \
    $${PWD}/OAIGoaltender.cpp \
    $${PWD}/OAIPenalty.cpp \
    $${PWD}/OAIPeriod.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGameProjection.cpp \
    $${PWD}/OAIScoringPlay.cpp \
    $${PWD}/OAISeries.cpp \
    $${PWD}/OAIStartingGoaltenders.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
