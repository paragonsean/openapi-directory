QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIDirectionsApi.h \
    $${PWD}/OAIDistanceApi.h \
    $${PWD}/OAIRouteApi.h \
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
    $${PWD}/OAIDirectionsApi.cpp \
    $${PWD}/OAIDistanceApi.cpp \
    $${PWD}/OAIRouteApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
