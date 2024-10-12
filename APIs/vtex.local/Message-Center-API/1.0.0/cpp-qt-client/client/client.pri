QT += network

HEADERS += \
# Models
    $${PWD}/OAI200_OK.h \
    $${PWD}/OAI401_Unauthorized.h \
# APIs
    $${PWD}/OAIDKIMConfigurationApi.h \
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
    $${PWD}/OAI200_OK.cpp \
    $${PWD}/OAI401_Unauthorized.cpp \
# APIs
    $${PWD}/OAIDKIMConfigurationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
