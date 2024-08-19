QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIFilterApi.h \
    $${PWD}/OAIPrivateApi.h \
    $${PWD}/OAIPublicApi.h \
    $${PWD}/OAIRetrieveApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAIUtilsApi.h \
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
    $${PWD}/OAIFilterApi.cpp \
    $${PWD}/OAIPrivateApi.cpp \
    $${PWD}/OAIPublicApi.cpp \
    $${PWD}/OAIRetrieveApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAIUtilsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
