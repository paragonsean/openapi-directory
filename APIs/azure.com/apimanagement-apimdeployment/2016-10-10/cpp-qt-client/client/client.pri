QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalRegion.h \
    $${PWD}/OAIApiManagementServiceBackupRestoreParameters.h \
    $${PWD}/OAIApiManagementServiceCheckNameAvailabilityParameters.h \
    $${PWD}/OAIApiManagementServiceGetSsoTokenResult.h \
    $${PWD}/OAIApiManagementServiceListResult.h \
    $${PWD}/OAIApiManagementServiceManageDeploymentsParameters.h \
    $${PWD}/OAIApiManagementServiceNameAvailabilityResult.h \
    $${PWD}/OAIApiManagementServiceProperties.h \
    $${PWD}/OAIApiManagementServiceResource.h \
    $${PWD}/OAIApiManagementServiceSkuProperties.h \
    $${PWD}/OAIApiManagementServiceUpdateHostnameParameters.h \
    $${PWD}/OAIApiManagementServiceUpdateParameters.h \
    $${PWD}/OAIApiManagementServiceUploadCertificateParameters.h \
    $${PWD}/OAICertificateInformation.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIHostnameConfiguration.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIVirtualNetworkConfiguration.h \
# APIs
    $${PWD}/OAIApiManagementOperationsApi.h \
    $${PWD}/OAIApiManagementServiceApi.h \
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
    $${PWD}/OAIAdditionalRegion.cpp \
    $${PWD}/OAIApiManagementServiceBackupRestoreParameters.cpp \
    $${PWD}/OAIApiManagementServiceCheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIApiManagementServiceGetSsoTokenResult.cpp \
    $${PWD}/OAIApiManagementServiceListResult.cpp \
    $${PWD}/OAIApiManagementServiceManageDeploymentsParameters.cpp \
    $${PWD}/OAIApiManagementServiceNameAvailabilityResult.cpp \
    $${PWD}/OAIApiManagementServiceProperties.cpp \
    $${PWD}/OAIApiManagementServiceResource.cpp \
    $${PWD}/OAIApiManagementServiceSkuProperties.cpp \
    $${PWD}/OAIApiManagementServiceUpdateHostnameParameters.cpp \
    $${PWD}/OAIApiManagementServiceUpdateParameters.cpp \
    $${PWD}/OAIApiManagementServiceUploadCertificateParameters.cpp \
    $${PWD}/OAICertificateInformation.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIHostnameConfiguration.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIVirtualNetworkConfiguration.cpp \
# APIs
    $${PWD}/OAIApiManagementOperationsApi.cpp \
    $${PWD}/OAIApiManagementServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
