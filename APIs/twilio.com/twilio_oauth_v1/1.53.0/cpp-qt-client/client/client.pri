QT += network

HEADERS += \
# Models
    $${PWD}/OAIOauth_v1_certs.h \
    $${PWD}/OAIOauth_v1_device_code.h \
    $${PWD}/OAIOauth_v1_openid_discovery.h \
    $${PWD}/OAIOauth_v1_token.h \
    $${PWD}/OAIOauth_v1_user_info.h \
# APIs
    $${PWD}/OAIOauthV1DeviceCodeApi.h \
    $${PWD}/OAIOauthV1OauthApi.h \
    $${PWD}/OAIOauthV1OpenidDiscoveryApi.h \
    $${PWD}/OAIOauthV1TokenApi.h \
    $${PWD}/OAIOauthV1UserInfoApi.h \
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
    $${PWD}/OAIOauth_v1_certs.cpp \
    $${PWD}/OAIOauth_v1_device_code.cpp \
    $${PWD}/OAIOauth_v1_openid_discovery.cpp \
    $${PWD}/OAIOauth_v1_token.cpp \
    $${PWD}/OAIOauth_v1_user_info.cpp \
# APIs
    $${PWD}/OAIOauthV1DeviceCodeApi.cpp \
    $${PWD}/OAIOauthV1OauthApi.cpp \
    $${PWD}/OAIOauthV1OpenidDiscoveryApi.cpp \
    $${PWD}/OAIOauthV1TokenApi.cpp \
    $${PWD}/OAIOauthV1UserInfoApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
