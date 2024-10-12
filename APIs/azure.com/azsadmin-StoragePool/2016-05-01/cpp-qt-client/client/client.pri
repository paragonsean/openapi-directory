QT += network

HEADERS += \
# Models
    $${PWD}/OAIStoragePool.h \
    $${PWD}/OAIStoragePoolList.h \
    $${PWD}/OAIStoragePoolModel.h \
# APIs
    $${PWD}/OAIStoragePoolsApi.h \
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
    $${PWD}/OAIStoragePool.cpp \
    $${PWD}/OAIStoragePoolList.cpp \
    $${PWD}/OAIStoragePoolModel.cpp \
# APIs
    $${PWD}/OAIStoragePoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
