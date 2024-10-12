QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountBalance.h \
    $${PWD}/OAIAccountSettings.h \
    $${PWD}/OAICreateAPISecret_400_response.h \
    $${PWD}/OAICreateAPISecret_400_response_invalid_parameters_inner.h \
    $${PWD}/OAICreateSecretRequest.h \
    $${PWD}/OAIErrorAPIKeyNotFound.h \
    $${PWD}/OAIErrorAuthenticationFailed.h \
    $${PWD}/OAIErrorAuthenticationFailedAccountBalance.h \
    $${PWD}/OAIErrorAutoReloadNotEnabled.h \
    $${PWD}/OAIErrorSecretIDNotFound.h \
    $${PWD}/OAIRegisterEmailRequest.h \
    $${PWD}/OAIRegisterEmailResponse.h \
    $${PWD}/OAIRetrieveAPISecret_404_response.h \
    $${PWD}/OAIRetrieveAPISecrets_200_response.h \
    $${PWD}/OAIRetrieveAPISecrets_200_response__embedded.h \
    $${PWD}/OAIRetrieveAPISecrets_401_response.h \
    $${PWD}/OAIRevokeAPISecret_403_response.h \
    $${PWD}/OAISecretInfo.h \
    $${PWD}/OAISecretMgmtLinks.h \
    $${PWD}/OAISecretMgmtLinks_self.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAITopUpAccountBalance_401_response.h \
# APIs
    $${PWD}/OAIBalanceApi.h \
    $${PWD}/OAIConfigurationApi.h \
    $${PWD}/OAISecretManagementApi.h \
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
    $${PWD}/OAIAccountBalance.cpp \
    $${PWD}/OAIAccountSettings.cpp \
    $${PWD}/OAICreateAPISecret_400_response.cpp \
    $${PWD}/OAICreateAPISecret_400_response_invalid_parameters_inner.cpp \
    $${PWD}/OAICreateSecretRequest.cpp \
    $${PWD}/OAIErrorAPIKeyNotFound.cpp \
    $${PWD}/OAIErrorAuthenticationFailed.cpp \
    $${PWD}/OAIErrorAuthenticationFailedAccountBalance.cpp \
    $${PWD}/OAIErrorAutoReloadNotEnabled.cpp \
    $${PWD}/OAIErrorSecretIDNotFound.cpp \
    $${PWD}/OAIRegisterEmailRequest.cpp \
    $${PWD}/OAIRegisterEmailResponse.cpp \
    $${PWD}/OAIRetrieveAPISecret_404_response.cpp \
    $${PWD}/OAIRetrieveAPISecrets_200_response.cpp \
    $${PWD}/OAIRetrieveAPISecrets_200_response__embedded.cpp \
    $${PWD}/OAIRetrieveAPISecrets_401_response.cpp \
    $${PWD}/OAIRevokeAPISecret_403_response.cpp \
    $${PWD}/OAISecretInfo.cpp \
    $${PWD}/OAISecretMgmtLinks.cpp \
    $${PWD}/OAISecretMgmtLinks_self.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAITopUpAccountBalance_401_response.cpp \
# APIs
    $${PWD}/OAIBalanceApi.cpp \
    $${PWD}/OAIConfigurationApi.cpp \
    $${PWD}/OAISecretManagementApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
