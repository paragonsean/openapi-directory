QT += network

HEADERS += \
# Models
    $${PWD}/OAIJoke.h \
    $${PWD}/OAIJokeOfTheDay.h \
    $${PWD}/OAIJokeOfTheDayResponse.h \
    $${PWD}/OAIJokeOfTheDayResponse_contents.h \
    $${PWD}/OAIJokeResponse.h \
    $${PWD}/OAIJokeResponse_contents.h \
    $${PWD}/OAINewJoke.h \
# APIs
    $${PWD}/OAIJodApi.h \
    $${PWD}/OAIJokeApi.h \
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
    $${PWD}/OAIJoke.cpp \
    $${PWD}/OAIJokeOfTheDay.cpp \
    $${PWD}/OAIJokeOfTheDayResponse.cpp \
    $${PWD}/OAIJokeOfTheDayResponse_contents.cpp \
    $${PWD}/OAIJokeResponse.cpp \
    $${PWD}/OAIJokeResponse_contents.cpp \
    $${PWD}/OAINewJoke.cpp \
# APIs
    $${PWD}/OAIJodApi.cpp \
    $${PWD}/OAIJokeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
