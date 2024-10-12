QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeletedSite.h \
    $${PWD}/OAIDeletedWebAppCollection.h \
# APIs
    $${PWD}/OAIDeletedWebAppsApi.h \
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
    $${PWD}/OAIDeletedSite.cpp \
    $${PWD}/OAIDeletedWebAppCollection.cpp \
# APIs
    $${PWD}/OAIDeletedWebAppsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
