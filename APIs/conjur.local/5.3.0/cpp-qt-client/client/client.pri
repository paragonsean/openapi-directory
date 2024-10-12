QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateHost_201_response.h \
    $${PWD}/OAICreateToken_200_response_inner.h \
    $${PWD}/OAIGetAuthenticators_200_response.h \
    $${PWD}/OAIGetServiceAuthenticatorStatus_200_response.h \
    $${PWD}/OAIInfo_200_response.h \
    $${PWD}/OAIInfo_200_response_authenticators.h \
    $${PWD}/OAIReplacePolicy_201_response.h \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner.h \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_permissions_inner.h \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_policy_versions_inner.h \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_secrets_inner.h \
    $${PWD}/OAISign_201_response.h \
    $${PWD}/OAIWhoAmI_200_response.h \
# APIs
    $${PWD}/OAIAuthenticationApi.h \
    $${PWD}/OAICertificateAuthorityApi.h \
    $${PWD}/OAIHostFactoryApi.h \
    $${PWD}/OAIPoliciesApi.h \
    $${PWD}/OAIPublicKeysApi.h \
    $${PWD}/OAIResourcesApi.h \
    $${PWD}/OAIRolesApi.h \
    $${PWD}/OAISecretsApi.h \
    $${PWD}/OAIStatusApi.h \
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
    $${PWD}/OAICreateHost_201_response.cpp \
    $${PWD}/OAICreateToken_200_response_inner.cpp \
    $${PWD}/OAIGetAuthenticators_200_response.cpp \
    $${PWD}/OAIGetServiceAuthenticatorStatus_200_response.cpp \
    $${PWD}/OAIInfo_200_response.cpp \
    $${PWD}/OAIInfo_200_response_authenticators.cpp \
    $${PWD}/OAIReplacePolicy_201_response.cpp \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner.cpp \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_permissions_inner.cpp \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_policy_versions_inner.cpp \
    $${PWD}/OAIShowResourcesForAllAccounts_200_response_inner_secrets_inner.cpp \
    $${PWD}/OAISign_201_response.cpp \
    $${PWD}/OAIWhoAmI_200_response.cpp \
# APIs
    $${PWD}/OAIAuthenticationApi.cpp \
    $${PWD}/OAICertificateAuthorityApi.cpp \
    $${PWD}/OAIHostFactoryApi.cpp \
    $${PWD}/OAIPoliciesApi.cpp \
    $${PWD}/OAIPublicKeysApi.cpp \
    $${PWD}/OAIResourcesApi.cpp \
    $${PWD}/OAIRolesApi.cpp \
    $${PWD}/OAISecretsApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
