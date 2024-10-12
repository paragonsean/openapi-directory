QT += network

HEADERS += \
# Models
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMeta.h \
    $${PWD}/OAIOnTimePrediction.h \
    $${PWD}/OAIPrediction.h \
# APIs
    $${PWD}/OAIAirportOntimePredictionApi.h \
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
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMeta.cpp \
    $${PWD}/OAIOnTimePrediction.cpp \
    $${PWD}/OAIPrediction.cpp \
# APIs
    $${PWD}/OAIAirportOntimePredictionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
