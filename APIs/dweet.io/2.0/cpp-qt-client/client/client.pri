QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIAlertsApi.h \
    $${PWD}/OAIDweetsApi.h \
    $${PWD}/OAILocksApi.h \
    $${PWD}/OAIStorageApi.h \
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
    $${PWD}/OAIAlertsApi.cpp \
    $${PWD}/OAIDweetsApi.cpp \
    $${PWD}/OAILocksApi.cpp \
    $${PWD}/OAIStorageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
