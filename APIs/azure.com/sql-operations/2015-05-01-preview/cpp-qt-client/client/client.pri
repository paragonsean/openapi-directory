QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationListResult.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationListResult.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
