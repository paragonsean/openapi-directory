QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPolicyDefinitionReference.h \
    $${PWD}/OAIPolicySetDefinition.h \
    $${PWD}/OAIPolicySetDefinitionListResult.h \
    $${PWD}/OAIPolicySetDefinitionProperties.h \
# APIs
    $${PWD}/OAIPolicySetDefinitionsApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPolicyDefinitionReference.cpp \
    $${PWD}/OAIPolicySetDefinition.cpp \
    $${PWD}/OAIPolicySetDefinitionListResult.cpp \
    $${PWD}/OAIPolicySetDefinitionProperties.cpp \
# APIs
    $${PWD}/OAIPolicySetDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
