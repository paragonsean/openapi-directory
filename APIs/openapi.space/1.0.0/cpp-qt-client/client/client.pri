QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIMeta.h \
    $${PWD}/OAICredentials.h \
    $${PWD}/OAILoginToken.h \
    $${PWD}/OAILogin_apinf_request.h \
    $${PWD}/OAILogin_apinf_token_request.h \
    $${PWD}/OAIRegistration.h \
# APIs
    $${PWD}/OAIAPIsApi.h \
    $${PWD}/OAIAuthApi.h \
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
    $${PWD}/OAIAPIMeta.cpp \
    $${PWD}/OAICredentials.cpp \
    $${PWD}/OAILoginToken.cpp \
    $${PWD}/OAILogin_apinf_request.cpp \
    $${PWD}/OAILogin_apinf_token_request.cpp \
    $${PWD}/OAIRegistration.cpp \
# APIs
    $${PWD}/OAIAPIsApi.cpp \
    $${PWD}/OAIAuthApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
