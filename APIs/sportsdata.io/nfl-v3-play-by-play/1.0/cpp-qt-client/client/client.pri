QT += network

HEADERS += \
# Models
    $${PWD}/OAIPlay.h \
    $${PWD}/OAIPlayByPlay.h \
    $${PWD}/OAIPlayStat.h \
    $${PWD}/OAIQuarter.h \
    $${PWD}/OAIScore.h \
    $${PWD}/OAIScoringPlay.h \
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
    $${PWD}/OAIPlay.cpp \
    $${PWD}/OAIPlayByPlay.cpp \
    $${PWD}/OAIPlayStat.cpp \
    $${PWD}/OAIQuarter.cpp \
    $${PWD}/OAIScore.cpp \
    $${PWD}/OAIScoringPlay.cpp \
    $${PWD}/OAIStadium.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
