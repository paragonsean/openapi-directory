QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIMediaApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAISparqlApi.h \
    $${PWD}/OAISubjectApi.h \
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
    $${PWD}/OAIMediaApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAISparqlApi.cpp \
    $${PWD}/OAISubjectApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
