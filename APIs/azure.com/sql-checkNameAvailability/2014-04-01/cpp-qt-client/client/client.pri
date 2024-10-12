QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityRequest.h \
    $${PWD}/OAICheckNameAvailabilityResponse.h \
# APIs
    $${PWD}/OAIServersApi.h \
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
    $${PWD}/OAICheckNameAvailabilityRequest.cpp \
    $${PWD}/OAICheckNameAvailabilityResponse.cpp \
# APIs
    $${PWD}/OAIServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
