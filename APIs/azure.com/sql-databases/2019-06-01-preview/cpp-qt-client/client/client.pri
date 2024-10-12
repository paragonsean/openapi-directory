QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabase.h \
    $${PWD}/OAIDatabaseListResult.h \
    $${PWD}/OAIDatabaseProperties.h \
    $${PWD}/OAIDatabaseUpdate.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceMoveDefinition.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAITrackedResource.h \
# APIs
    $${PWD}/OAIDatabasesApi.h \
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
    $${PWD}/OAIDatabase.cpp \
    $${PWD}/OAIDatabaseListResult.cpp \
    $${PWD}/OAIDatabaseProperties.cpp \
    $${PWD}/OAIDatabaseUpdate.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceMoveDefinition.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAITrackedResource.cpp \
# APIs
    $${PWD}/OAIDatabasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
