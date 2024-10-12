QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorizationValue.h \
    $${PWD}/OAICliOption.h \
    $${PWD}/OAIGeneratorInput.h \
    $${PWD}/OAIResponseCode.h \
    $${PWD}/OAISecuritySchemeDefinition.h \
# APIs
    $${PWD}/OAIClientsApi.h \
    $${PWD}/OAIServersApi.h \
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
    $${PWD}/OAIAuthorizationValue.cpp \
    $${PWD}/OAICliOption.cpp \
    $${PWD}/OAIGeneratorInput.cpp \
    $${PWD}/OAIResponseCode.cpp \
    $${PWD}/OAISecuritySchemeDefinition.cpp \
# APIs
    $${PWD}/OAIClientsApi.cpp \
    $${PWD}/OAIServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
