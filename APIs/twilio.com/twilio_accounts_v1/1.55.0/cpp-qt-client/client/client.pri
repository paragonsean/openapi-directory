QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccounts_v1_auth_token_promotion.h \
    $${PWD}/OAIAccounts_v1_credential_credential_aws.h \
    $${PWD}/OAIAccounts_v1_credential_credential_public_key.h \
    $${PWD}/OAIAccounts_v1_safelist.h \
    $${PWD}/OAIAccounts_v1_secondary_auth_token.h \
    $${PWD}/OAIListCredentialAwsResponse.h \
    $${PWD}/OAIListCredentialAwsResponse_meta.h \
    $${PWD}/OAIListCredentialPublicKeyResponse.h \
# APIs
    $${PWD}/OAIAccountsV1AuthTokenPromotionApi.h \
    $${PWD}/OAIAccountsV1AwsApi.h \
    $${PWD}/OAIAccountsV1PublicKeyApi.h \
    $${PWD}/OAIAccountsV1SafelistApi.h \
    $${PWD}/OAIAccountsV1SecondaryAuthTokenApi.h \
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
    $${PWD}/OAIAccounts_v1_auth_token_promotion.cpp \
    $${PWD}/OAIAccounts_v1_credential_credential_aws.cpp \
    $${PWD}/OAIAccounts_v1_credential_credential_public_key.cpp \
    $${PWD}/OAIAccounts_v1_safelist.cpp \
    $${PWD}/OAIAccounts_v1_secondary_auth_token.cpp \
    $${PWD}/OAIListCredentialAwsResponse.cpp \
    $${PWD}/OAIListCredentialAwsResponse_meta.cpp \
    $${PWD}/OAIListCredentialPublicKeyResponse.cpp \
# APIs
    $${PWD}/OAIAccountsV1AuthTokenPromotionApi.cpp \
    $${PWD}/OAIAccountsV1AwsApi.cpp \
    $${PWD}/OAIAccountsV1PublicKeyApi.cpp \
    $${PWD}/OAIAccountsV1SafelistApi.cpp \
    $${PWD}/OAIAccountsV1SecondaryAuthTokenApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
