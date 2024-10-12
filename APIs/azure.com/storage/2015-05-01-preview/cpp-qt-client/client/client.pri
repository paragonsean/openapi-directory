QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityResult.h \
    $${PWD}/OAICustomDomain.h \
    $${PWD}/OAIEndpoints.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIStorageAccount.h \
    $${PWD}/OAIStorageAccountCheckNameAvailabilityParameters.h \
    $${PWD}/OAIStorageAccountCreateParameters.h \
    $${PWD}/OAIStorageAccountKeys.h \
    $${PWD}/OAIStorageAccountListResult.h \
    $${PWD}/OAIStorageAccountProperties.h \
    $${PWD}/OAIStorageAccountPropertiesCreateParameters.h \
    $${PWD}/OAIStorageAccountPropertiesUpdateParameters.h \
    $${PWD}/OAIStorageAccountRegenerateKeyParameters.h \
    $${PWD}/OAIStorageAccountUpdateParameters.h \
    $${PWD}/OAISubResource.h \
    $${PWD}/OAIUsage.h \
    $${PWD}/OAIUsageListResult.h \
    $${PWD}/OAIUsageName.h \
# APIs
    $${PWD}/OAIStorageAccountsApi.h \
    $${PWD}/OAIUsageApi.h \
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
    $${PWD}/OAICheckNameAvailabilityResult.cpp \
    $${PWD}/OAICustomDomain.cpp \
    $${PWD}/OAIEndpoints.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIStorageAccount.cpp \
    $${PWD}/OAIStorageAccountCheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIStorageAccountCreateParameters.cpp \
    $${PWD}/OAIStorageAccountKeys.cpp \
    $${PWD}/OAIStorageAccountListResult.cpp \
    $${PWD}/OAIStorageAccountProperties.cpp \
    $${PWD}/OAIStorageAccountPropertiesCreateParameters.cpp \
    $${PWD}/OAIStorageAccountPropertiesUpdateParameters.cpp \
    $${PWD}/OAIStorageAccountRegenerateKeyParameters.cpp \
    $${PWD}/OAIStorageAccountUpdateParameters.cpp \
    $${PWD}/OAISubResource.cpp \
    $${PWD}/OAIUsage.cpp \
    $${PWD}/OAIUsageListResult.cpp \
    $${PWD}/OAIUsageName.cpp \
# APIs
    $${PWD}/OAIStorageAccountsApi.cpp \
    $${PWD}/OAIUsageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
