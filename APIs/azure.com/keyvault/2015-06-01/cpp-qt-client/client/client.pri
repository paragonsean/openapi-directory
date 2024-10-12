QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessPolicyEntry.h \
    $${PWD}/OAIPermissions.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceListResult.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAIVault.h \
    $${PWD}/OAIVaultCreateOrUpdateParameters.h \
    $${PWD}/OAIVaultListResult.h \
    $${PWD}/OAIVaultProperties.h \
# APIs
    $${PWD}/OAIVaultsApi.h \
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
    $${PWD}/OAIAccessPolicyEntry.cpp \
    $${PWD}/OAIPermissions.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceListResult.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAIVault.cpp \
    $${PWD}/OAIVaultCreateOrUpdateParameters.cpp \
    $${PWD}/OAIVaultListResult.cpp \
    $${PWD}/OAIVaultProperties.cpp \
# APIs
    $${PWD}/OAIVaultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
