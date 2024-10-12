QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateStatus.h \
    $${PWD}/OAIDeleteStatus.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIUpdateStatus.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAICreateStatus.cpp \
    $${PWD}/OAIDeleteStatus.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIUpdateStatus.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
