QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIGamesApi.h \
    $${PWD}/OAIPlayersApi.h \
    $${PWD}/OAIStatsApi.h \
    $${PWD}/OAITeamsApi.h \
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
# APIs
    $${PWD}/OAIGamesApi.cpp \
    $${PWD}/OAIPlayersApi.cpp \
    $${PWD}/OAIStatsApi.cpp \
    $${PWD}/OAITeamsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
