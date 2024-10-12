QT += network

HEADERS += \
# Models
    $${PWD}/OAIContainerService.h \
    $${PWD}/OAIContainerServiceAgentPoolProfile.h \
    $${PWD}/OAIContainerServiceCustomProfile.h \
    $${PWD}/OAIContainerServiceDiagnosticsProfile.h \
    $${PWD}/OAIContainerServiceLinuxProfile.h \
    $${PWD}/OAIContainerServiceListResult.h \
    $${PWD}/OAIContainerServiceMasterProfile.h \
    $${PWD}/OAIContainerServiceOrchestratorProfile.h \
    $${PWD}/OAIContainerServiceProperties.h \
    $${PWD}/OAIContainerServiceServicePrincipalProfile.h \
    $${PWD}/OAIContainerServiceSshConfiguration.h \
    $${PWD}/OAIContainerServiceSshPublicKey.h \
    $${PWD}/OAIContainerServiceStorageProfile.h \
    $${PWD}/OAIContainerServiceVMDiagnostics.h \
    $${PWD}/OAIContainerServiceVMSize.h \
    $${PWD}/OAIContainerServiceWindowsProfile.h \
    $${PWD}/OAIKeyVaultSecretRef.h \
    $${PWD}/OAIOSType.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIContainerServiceApi.h \
    $${PWD}/OAIContainerServicesApi.h \
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
    $${PWD}/OAIContainerService.cpp \
    $${PWD}/OAIContainerServiceAgentPoolProfile.cpp \
    $${PWD}/OAIContainerServiceCustomProfile.cpp \
    $${PWD}/OAIContainerServiceDiagnosticsProfile.cpp \
    $${PWD}/OAIContainerServiceLinuxProfile.cpp \
    $${PWD}/OAIContainerServiceListResult.cpp \
    $${PWD}/OAIContainerServiceMasterProfile.cpp \
    $${PWD}/OAIContainerServiceOrchestratorProfile.cpp \
    $${PWD}/OAIContainerServiceProperties.cpp \
    $${PWD}/OAIContainerServiceServicePrincipalProfile.cpp \
    $${PWD}/OAIContainerServiceSshConfiguration.cpp \
    $${PWD}/OAIContainerServiceSshPublicKey.cpp \
    $${PWD}/OAIContainerServiceStorageProfile.cpp \
    $${PWD}/OAIContainerServiceVMDiagnostics.cpp \
    $${PWD}/OAIContainerServiceVMSize.cpp \
    $${PWD}/OAIContainerServiceWindowsProfile.cpp \
    $${PWD}/OAIKeyVaultSecretRef.cpp \
    $${PWD}/OAIOSType.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIContainerServiceApi.cpp \
    $${PWD}/OAIContainerServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
