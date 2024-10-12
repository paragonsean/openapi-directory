QT += network

HEADERS += \
# Models
    $${PWD}/OAIStep.h \
    $${PWD}/OAIStep_coordinates.h \
    $${PWD}/OAIStep_route.h \
    $${PWD}/OAITrip.h \
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
    $${PWD}/OAIStep.cpp \
    $${PWD}/OAIStep_coordinates.cpp \
    $${PWD}/OAIStep_route.cpp \
    $${PWD}/OAITrip.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
