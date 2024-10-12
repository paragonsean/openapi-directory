QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthentiqID.h \
    $${PWD}/OAIClaims.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIJWT.h \
    $${PWD}/OAIJWT_1.h \
    $${PWD}/OAIKey_bind_200_response.h \
    $${PWD}/OAIKey_register_201_response.h \
    $${PWD}/OAIKey_revoke_200_response.h \
    $${PWD}/OAIKey_revoke_nosecret_200_response.h \
    $${PWD}/OAIPushToken.h \
    $${PWD}/OAIPush_login_request_200_response.h \
    $${PWD}/OAISign_request_201_response.h \
    $${PWD}/OAISign_update_200_response.h \
# APIs
    $${PWD}/OAIDeleteApi.h \
    $${PWD}/OAIGetApi.h \
    $${PWD}/OAIHeadApi.h \
    $${PWD}/OAIKeyApi.h \
    $${PWD}/OAILoginApi.h \
    $${PWD}/OAIPostApi.h \
    $${PWD}/OAIPutApi.h \
    $${PWD}/OAIScopeApi.h \
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
    $${PWD}/OAIAuthentiqID.cpp \
    $${PWD}/OAIClaims.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIJWT.cpp \
    $${PWD}/OAIJWT_1.cpp \
    $${PWD}/OAIKey_bind_200_response.cpp \
    $${PWD}/OAIKey_register_201_response.cpp \
    $${PWD}/OAIKey_revoke_200_response.cpp \
    $${PWD}/OAIKey_revoke_nosecret_200_response.cpp \
    $${PWD}/OAIPushToken.cpp \
    $${PWD}/OAIPush_login_request_200_response.cpp \
    $${PWD}/OAISign_request_201_response.cpp \
    $${PWD}/OAISign_update_200_response.cpp \
# APIs
    $${PWD}/OAIDeleteApi.cpp \
    $${PWD}/OAIGetApi.cpp \
    $${PWD}/OAIHeadApi.cpp \
    $${PWD}/OAIKeyApi.cpp \
    $${PWD}/OAILoginApi.cpp \
    $${PWD}/OAIPostApi.cpp \
    $${PWD}/OAIPutApi.cpp \
    $${PWD}/OAIScopeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
