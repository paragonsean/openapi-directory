QT += network

HEADERS += \
# Models
    $${PWD}/OAICustomer.h \
    $${PWD}/OAIJwtResponse.h \
    $${PWD}/OAILoginUser.h \
    $${PWD}/OAIProblem.h \
    $${PWD}/OAIResponseEntity.h \
    $${PWD}/OAIResponseStatus.h \
# APIs
    $${PWD}/OAIAuthenticationApiControllerApi.h \
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
    $${PWD}/OAICustomer.cpp \
    $${PWD}/OAIJwtResponse.cpp \
    $${PWD}/OAILoginUser.cpp \
    $${PWD}/OAIProblem.cpp \
    $${PWD}/OAIResponseEntity.cpp \
    $${PWD}/OAIResponseStatus.cpp \
# APIs
    $${PWD}/OAIAuthenticationApiControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
