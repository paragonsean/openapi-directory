QT += network

HEADERS += \
# Models
    $${PWD}/OAIGenerateAccessTokenRequest.h \
    $${PWD}/OAIGenerateAccessTokenResponse.h \
    $${PWD}/OAIGenerateIdTokenRequest.h \
    $${PWD}/OAIGenerateIdTokenResponse.h \
    $${PWD}/OAISignBlobRequest.h \
    $${PWD}/OAISignBlobResponse.h \
    $${PWD}/OAISignJwtRequest.h \
    $${PWD}/OAISignJwtResponse.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGenerateAccessTokenRequest.cpp \
    $${PWD}/OAIGenerateAccessTokenResponse.cpp \
    $${PWD}/OAIGenerateIdTokenRequest.cpp \
    $${PWD}/OAIGenerateIdTokenResponse.cpp \
    $${PWD}/OAISignBlobRequest.cpp \
    $${PWD}/OAISignBlobResponse.cpp \
    $${PWD}/OAISignJwtRequest.cpp \
    $${PWD}/OAISignJwtResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
