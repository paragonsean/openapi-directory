QT += network

HEADERS += \
# Models
    $${PWD}/OAICountResult.h \
    $${PWD}/OAIErrorResult.h \
    $${PWD}/OAIInfoResult.h \
# APIs
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAITransitApi.h \
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
    $${PWD}/OAICountResult.cpp \
    $${PWD}/OAIErrorResult.cpp \
    $${PWD}/OAIInfoResult.cpp \
# APIs
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAITransitApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
