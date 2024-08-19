QT += network

HEADERS += \
# Models
    $${PWD}/OAIABU.h \
    $${PWD}/OAIAbuDTO.h \
    $${PWD}/OAIAbuResponse.h \
    $${PWD}/OAIAbuResultDTO.h \
# APIs
    $${PWD}/OAIABUApi.h \
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
    $${PWD}/OAIABU.cpp \
    $${PWD}/OAIAbuDTO.cpp \
    $${PWD}/OAIAbuResponse.cpp \
    $${PWD}/OAIAbuResultDTO.cpp \
# APIs
    $${PWD}/OAIABUApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
