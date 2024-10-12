QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseOperation.h \
    $${PWD}/OAIDatabaseOperationListResult.h \
    $${PWD}/OAIDatabaseOperationProperties.h \
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
    $${PWD}/OAIDatabaseOperation.cpp \
    $${PWD}/OAIDatabaseOperationListResult.cpp \
    $${PWD}/OAIDatabaseOperationProperties.cpp \
# APIs
    $${PWD}/OAIDatabasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
