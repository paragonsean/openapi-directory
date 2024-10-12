QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureAsyncOperationResult.h \
    $${PWD}/OAIDataLakeStoreAccount.h \
    $${PWD}/OAIDataLakeStoreAccountListResult.h \
    $${PWD}/OAIDataLakeStoreAccountProperties.h \
    $${PWD}/OAIDataLakeStoreFirewallRuleListResult.h \
    $${PWD}/OAIEncryptionConfig.h \
    $${PWD}/OAIEncryptionIdentity.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIFirewallRule.h \
    $${PWD}/OAIFirewallRuleProperties.h \
    $${PWD}/OAIInnerError.h \
    $${PWD}/OAIKeyVaultMetaInfo.h \
# APIs
    $${PWD}/OAIAccountApi.h \
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
    $${PWD}/OAIAzureAsyncOperationResult.cpp \
    $${PWD}/OAIDataLakeStoreAccount.cpp \
    $${PWD}/OAIDataLakeStoreAccountListResult.cpp \
    $${PWD}/OAIDataLakeStoreAccountProperties.cpp \
    $${PWD}/OAIDataLakeStoreFirewallRuleListResult.cpp \
    $${PWD}/OAIEncryptionConfig.cpp \
    $${PWD}/OAIEncryptionIdentity.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIFirewallRule.cpp \
    $${PWD}/OAIFirewallRuleProperties.cpp \
    $${PWD}/OAIInnerError.cpp \
    $${PWD}/OAIKeyVaultMetaInfo.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
