QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessTokenInfoResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIRefreshTokenInfoResponse.h \
    $${PWD}/OAITokenResponseIF.h \
# APIs
    $${PWD}/OAIAccessTokensApi.h \
    $${PWD}/OAIRefreshTokensApi.h \
    $${PWD}/OAITokensApi.h \
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
    $${PWD}/OAIAccessTokenInfoResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIRefreshTokenInfoResponse.cpp \
    $${PWD}/OAITokenResponseIF.cpp \
# APIs
    $${PWD}/OAIAccessTokensApi.cpp \
    $${PWD}/OAIRefreshTokensApi.cpp \
    $${PWD}/OAITokensApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
