QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutomaticTuningOptions.h \
    $${PWD}/OAIDatabaseAutomaticTuning.h \
    $${PWD}/OAIDatabaseAutomaticTuningProperties.h \
# APIs
    $${PWD}/OAIDatabaseAutomaticTuningApi.h \
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
    $${PWD}/OAIAutomaticTuningOptions.cpp \
    $${PWD}/OAIDatabaseAutomaticTuning.cpp \
    $${PWD}/OAIDatabaseAutomaticTuningProperties.cpp \
# APIs
    $${PWD}/OAIDatabaseAutomaticTuningApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
