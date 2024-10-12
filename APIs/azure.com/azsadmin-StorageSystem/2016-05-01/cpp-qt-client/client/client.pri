QT += network

HEADERS += \
# Models
    $${PWD}/OAIStorageSystem.h \
    $${PWD}/OAIStorageSystemList.h \
    $${PWD}/OAIStorageSystemModel.h \
# APIs
    $${PWD}/OAIStorageSystemsApi.h \
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
    $${PWD}/OAIStorageSystem.cpp \
    $${PWD}/OAIStorageSystemList.cpp \
    $${PWD}/OAIStorageSystemModel.cpp \
# APIs
    $${PWD}/OAIStorageSystemsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
