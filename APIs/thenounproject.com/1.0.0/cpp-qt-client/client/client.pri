QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAICollectionApi.h \
    $${PWD}/OAICollectionsApi.h \
    $${PWD}/OAIIconApi.h \
    $${PWD}/OAIIconsApi.h \
    $${PWD}/OAIOauthApi.h \
    $${PWD}/OAIUserApi.h \
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
    $${PWD}/OAICollectionApi.cpp \
    $${PWD}/OAICollectionsApi.cpp \
    $${PWD}/OAIIconApi.cpp \
    $${PWD}/OAIIconsApi.cpp \
    $${PWD}/OAIOauthApi.cpp \
    $${PWD}/OAIUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
