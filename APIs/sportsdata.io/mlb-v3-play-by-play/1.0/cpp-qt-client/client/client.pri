QT += network

HEADERS += \
# Models
    $${PWD}/OAIGame.h \
    $${PWD}/OAIInning.h \
    $${PWD}/OAIPitch.h \
    $${PWD}/OAIPlay.h \
    $${PWD}/OAIPlayByPlay.h \
    $${PWD}/OAISeries.h \
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
    $${PWD}/OAIPitch.cpp \
    $${PWD}/OAIPlay.cpp \
    $${PWD}/OAIPlayByPlay.cpp \
    $${PWD}/OAISeries.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
