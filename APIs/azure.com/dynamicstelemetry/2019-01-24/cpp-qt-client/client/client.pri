QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAILogSpecification.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIProperties.h \
    $${PWD}/OAIServiceSpecification.h \
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
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAILogSpecification.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIProperties.cpp \
    $${PWD}/OAIServiceSpecification.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
