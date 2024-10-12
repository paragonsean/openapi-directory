QT += network

HEADERS += \
# Models
    $${PWD}/OAIInputPart.h \
    $${PWD}/OAIMediaType.h \
# APIs
    $${PWD}/OAIGeorgApi.h \
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
    $${PWD}/OAIInputPart.cpp \
    $${PWD}/OAIMediaType.cpp \
# APIs
    $${PWD}/OAIGeorgApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
