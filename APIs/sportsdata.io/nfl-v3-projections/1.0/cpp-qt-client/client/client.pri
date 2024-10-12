QT += network

HEADERS += \
# Models
    $${PWD}/OAIDfsSlate.h \
    $${PWD}/OAIDfsSlateGame.h \
    $${PWD}/OAIDfsSlatePlayer.h \
    $${PWD}/OAIDfsSlatePlayerOwnershipProjection.h \
    $${PWD}/OAIDfsSlateWithOwnershipProjection.h \
    $${PWD}/OAIFantasyDefenseGameProjection.h \
    $${PWD}/OAIFantasyDefenseSeasonProjection.h \
    $${PWD}/OAIPlayer.h \
    $${PWD}/OAIPlayerGameProjection.h \
    $${PWD}/OAIPlayerSeasonProjection.h \
    $${PWD}/OAISchedule.h \
    $${PWD}/OAIScoringDetail.h \
    $${PWD}/OAIStadium.h \
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
    $${PWD}/OAIDfsSlatePlayerOwnershipProjection.cpp \
    $${PWD}/OAIDfsSlateWithOwnershipProjection.cpp \
    $${PWD}/OAIFantasyDefenseGameProjection.cpp \
    $${PWD}/OAIFantasyDefenseSeasonProjection.cpp \
    $${PWD}/OAIPlayer.cpp \
    $${PWD}/OAIPlayerGameProjection.cpp \
    $${PWD}/OAIPlayerSeasonProjection.cpp \
    $${PWD}/OAISchedule.cpp \
    $${PWD}/OAIScoringDetail.cpp \
    $${PWD}/OAIStadium.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
