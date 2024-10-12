QT += network

HEADERS += \
# Models
    $${PWD}/OAIContinent.h \
    $${PWD}/OAICountry.h \
    $${PWD}/OAIIsp.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIProxy.h \
    $${PWD}/OAISubdivision.h \
    $${PWD}/OAITimings.h \
# APIs
    $${PWD}/OAIProxyApi.h \
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
    $${PWD}/OAIContinent.cpp \
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAIIsp.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIProxy.cpp \
    $${PWD}/OAISubdivision.cpp \
    $${PWD}/OAITimings.cpp \
# APIs
    $${PWD}/OAIProxyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
