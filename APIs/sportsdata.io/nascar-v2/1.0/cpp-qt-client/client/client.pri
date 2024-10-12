QT += network

HEADERS += \
# Models
    $${PWD}/OAIDriver.h \
    $${PWD}/OAIDriverRace.h \
    $${PWD}/OAIDriverRaceProjection.h \
    $${PWD}/OAIRace.h \
    $${PWD}/OAIRaceResult.h \
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
    $${PWD}/OAIDriver.cpp \
    $${PWD}/OAIDriverRace.cpp \
    $${PWD}/OAIDriverRaceProjection.cpp \
    $${PWD}/OAIRace.cpp \
    $${PWD}/OAIRaceResult.cpp \
    $${PWD}/OAISeries.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
