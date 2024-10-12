QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIIntersectionsApi.h \
    $${PWD}/OAIOccupantsApi.h \
    $${PWD}/OAIParcelsApi.h \
    $${PWD}/OAISitesApi.h \
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
    $${PWD}/OAIIntersectionsApi.cpp \
    $${PWD}/OAIOccupantsApi.cpp \
    $${PWD}/OAIParcelsApi.cpp \
    $${PWD}/OAISitesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
