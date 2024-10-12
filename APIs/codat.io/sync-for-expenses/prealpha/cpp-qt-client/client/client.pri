QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountMappingInfo.h \
    $${PWD}/OAIAttachment.h \
    $${PWD}/OAICodatErrorMessage.h \
    $${PWD}/OAICodatErrorMessage_validation.h \
    $${PWD}/OAICodatErrorMessage_validation_errors_inner.h \
    $${PWD}/OAICompanyConfiguration.h \
    $${PWD}/OAICompanySyncStatus.h \
    $${PWD}/OAIDataConnection.h \
    $${PWD}/OAIDataConnectionError.h \
    $${PWD}/OAIDataConnectionStatus.h \
    $${PWD}/OAIExpenseTransaction.h \
    $${PWD}/OAIMappingOptions.h \
    $${PWD}/OAIPostSync.h \
    $${PWD}/OAISyncInitiated.h \
    $${PWD}/OAITaxRateMappingInfo.h \
    $${PWD}/OAITrackingCategoryMappingInfo.h \
    $${PWD}/OAITransactionMetadata.h \
# APIs
    $${PWD}/OAIConfigurationApi.h \
    $${PWD}/OAIConnectionsApi.h \
    $${PWD}/OAIExpensesApi.h \
    $${PWD}/OAIMappingOptionsApi.h \
    $${PWD}/OAISyncApi.h \
    $${PWD}/OAISyncStatusApi.h \
    $${PWD}/OAITransactionStatusApi.h \
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
    $${PWD}/OAIAccountMappingInfo.cpp \
    $${PWD}/OAIAttachment.cpp \
    $${PWD}/OAICodatErrorMessage.cpp \
    $${PWD}/OAICodatErrorMessage_validation.cpp \
    $${PWD}/OAICodatErrorMessage_validation_errors_inner.cpp \
    $${PWD}/OAICompanyConfiguration.cpp \
    $${PWD}/OAICompanySyncStatus.cpp \
    $${PWD}/OAIDataConnection.cpp \
    $${PWD}/OAIDataConnectionError.cpp \
    $${PWD}/OAIDataConnectionStatus.cpp \
    $${PWD}/OAIExpenseTransaction.cpp \
    $${PWD}/OAIMappingOptions.cpp \
    $${PWD}/OAIPostSync.cpp \
    $${PWD}/OAISyncInitiated.cpp \
    $${PWD}/OAITaxRateMappingInfo.cpp \
    $${PWD}/OAITrackingCategoryMappingInfo.cpp \
    $${PWD}/OAITransactionMetadata.cpp \
# APIs
    $${PWD}/OAIConfigurationApi.cpp \
    $${PWD}/OAIConnectionsApi.cpp \
    $${PWD}/OAIExpensesApi.cpp \
    $${PWD}/OAIMappingOptionsApi.cpp \
    $${PWD}/OAISyncApi.cpp \
    $${PWD}/OAISyncStatusApi.cpp \
    $${PWD}/OAITransactionStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
