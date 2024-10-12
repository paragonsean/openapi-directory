QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAINumbersErrors.h \
    $${PWD}/OAISuccess.h \
# APIs
    $${PWD}/OAINumbersApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAINumbersErrors.cpp \
    $${PWD}/OAISuccess.cpp \
# APIs
    $${PWD}/OAINumbersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
