QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalLocation.h \
    $${PWD}/OAIApiManagementServiceApplyNetworkConfigurationParameters.h \
    $${PWD}/OAIApiManagementServiceBackupRestoreParameters.h \
    $${PWD}/OAIApiManagementServiceBaseProperties.h \
    $${PWD}/OAIApiManagementServiceCheckNameAvailabilityParameters.h \
    $${PWD}/OAIApiManagementServiceGetSsoTokenResult.h \
    $${PWD}/OAIApiManagementServiceIdentity.h \
    $${PWD}/OAIApiManagementServiceListResult.h \
    $${PWD}/OAIApiManagementServiceNameAvailabilityResult.h \
    $${PWD}/OAIApiManagementServiceProperties.h \
    $${PWD}/OAIApiManagementServiceResource.h \
    $${PWD}/OAIApiManagementServiceSkuProperties.h \
    $${PWD}/OAIApiManagementServiceUpdateHostnameParameters.h \
    $${PWD}/OAIApiManagementServiceUpdateParameters.h \
    $${PWD}/OAIApiManagementServiceUpdateProperties.h \
    $${PWD}/OAIApiManagementServiceUploadCertificateParameters.h \
    $${PWD}/OAIApimResource.h \
    $${PWD}/OAICertificateConfiguration.h \
    $${PWD}/OAICertificateInformation.h \
    $${PWD}/OAIHostnameConfiguration.h \
    $${PWD}/OAIHostnameConfigurationOld.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
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
    $${PWD}/OAIAdditionalLocation.cpp \
    $${PWD}/OAIApiManagementServiceApplyNetworkConfigurationParameters.cpp \
    $${PWD}/OAIApiManagementServiceBackupRestoreParameters.cpp \
    $${PWD}/OAIApiManagementServiceBaseProperties.cpp \
    $${PWD}/OAIApiManagementServiceCheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIApiManagementServiceGetSsoTokenResult.cpp \
    $${PWD}/OAIApiManagementServiceIdentity.cpp \
    $${PWD}/OAIApiManagementServiceListResult.cpp \
    $${PWD}/OAIApiManagementServiceNameAvailabilityResult.cpp \
    $${PWD}/OAIApiManagementServiceProperties.cpp \
    $${PWD}/OAIApiManagementServiceResource.cpp \
    $${PWD}/OAIApiManagementServiceSkuProperties.cpp \
    $${PWD}/OAIApiManagementServiceUpdateHostnameParameters.cpp \
    $${PWD}/OAIApiManagementServiceUpdateParameters.cpp \
    $${PWD}/OAIApiManagementServiceUpdateProperties.cpp \
    $${PWD}/OAIApiManagementServiceUploadCertificateParameters.cpp \
    $${PWD}/OAIApimResource.cpp \
    $${PWD}/OAICertificateConfiguration.cpp \
    $${PWD}/OAICertificateInformation.cpp \
    $${PWD}/OAIHostnameConfiguration.cpp \
    $${PWD}/OAIHostnameConfigurationOld.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIVirtualNetworkConfiguration.cpp \
# APIs
    $${PWD}/OAIApiManagementOperationsApi.cpp \
    $${PWD}/OAIApiManagementServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
