QT += network

HEADERS += \
# Models
    $${PWD}/OAIEmailModel.h \
    $${PWD}/OAIForgotMailToken.h \
    $${PWD}/OAIJwtResponse.h \
    $${PWD}/OAILoginUser.h \
    $${PWD}/OAIMailToken.h \
    $${PWD}/OAIProblem.h \
    $${PWD}/OAIRegistrationModel.h \
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
    $${PWD}/OAIEmailModel.cpp \
    $${PWD}/OAIForgotMailToken.cpp \
    $${PWD}/OAIJwtResponse.cpp \
    $${PWD}/OAILoginUser.cpp \
    $${PWD}/OAIMailToken.cpp \
    $${PWD}/OAIProblem.cpp \
    $${PWD}/OAIRegistrationModel.cpp \
    $${PWD}/OAIResponseEntity.cpp \
    $${PWD}/OAIResponseStatus.cpp \
# APIs
    $${PWD}/OAIAuthenticationApiControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
