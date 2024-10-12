QT += network

HEADERS += \
# Models
    $${PWD}/OAIServiceObjective.h \
    $${PWD}/OAIServiceObjectiveListResult.h \
    $${PWD}/OAIServiceObjectiveProperties.h \
# APIs
    $${PWD}/OAIServiceObjectivesApi.h \
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
    $${PWD}/OAIServiceObjective.cpp \
    $${PWD}/OAIServiceObjectiveListResult.cpp \
    $${PWD}/OAIServiceObjectiveProperties.cpp \
# APIs
    $${PWD}/OAIServiceObjectivesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
