QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessProfile.h \
    $${PWD}/OAIContainerServiceAgentPoolProfile.h \
    $${PWD}/OAIContainerServiceDiagnosticsProfile.h \
    $${PWD}/OAIContainerServiceLinuxProfile.h \
    $${PWD}/OAIContainerServiceMasterProfile.h \
    $${PWD}/OAIContainerServiceServicePrincipalProfile.h \
    $${PWD}/OAIContainerServiceSshConfiguration.h \
    $${PWD}/OAIContainerServiceSshPublicKey.h \
    $${PWD}/OAIContainerServiceStorageProfile.h \
    $${PWD}/OAIContainerServiceVMDiagnostics.h \
    $${PWD}/OAIContainerServiceVMSize.h \
    $${PWD}/OAIContainerServiceWindowsProfile.h \
    $${PWD}/OAIKeyVaultSecretRef.h \
    $${PWD}/OAIManagedCluster.h \
    $${PWD}/OAIManagedClusterAccessProfile.h \
    $${PWD}/OAIManagedClusterListResult.h \
    $${PWD}/OAIManagedClusterPoolUpgradeProfile.h \
    $${PWD}/OAIManagedClusterProperties.h \
    $${PWD}/OAIManagedClusterUpgradeProfile.h \
    $${PWD}/OAIManagedClusterUpgradeProfileProperties.h \
    $${PWD}/OAIOSType.h \
    $${PWD}/OAIOrchestratorProfile.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIManagedClustersApi.h \
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
    $${PWD}/OAIAccessProfile.cpp \
    $${PWD}/OAIContainerServiceAgentPoolProfile.cpp \
    $${PWD}/OAIContainerServiceDiagnosticsProfile.cpp \
    $${PWD}/OAIContainerServiceLinuxProfile.cpp \
    $${PWD}/OAIContainerServiceMasterProfile.cpp \
    $${PWD}/OAIContainerServiceServicePrincipalProfile.cpp \
    $${PWD}/OAIContainerServiceSshConfiguration.cpp \
    $${PWD}/OAIContainerServiceSshPublicKey.cpp \
    $${PWD}/OAIContainerServiceStorageProfile.cpp \
    $${PWD}/OAIContainerServiceVMDiagnostics.cpp \
    $${PWD}/OAIContainerServiceVMSize.cpp \
    $${PWD}/OAIContainerServiceWindowsProfile.cpp \
    $${PWD}/OAIKeyVaultSecretRef.cpp \
    $${PWD}/OAIManagedCluster.cpp \
    $${PWD}/OAIManagedClusterAccessProfile.cpp \
    $${PWD}/OAIManagedClusterListResult.cpp \
    $${PWD}/OAIManagedClusterPoolUpgradeProfile.cpp \
    $${PWD}/OAIManagedClusterProperties.cpp \
    $${PWD}/OAIManagedClusterUpgradeProfile.cpp \
    $${PWD}/OAIManagedClusterUpgradeProfileProperties.cpp \
    $${PWD}/OAIOSType.cpp \
    $${PWD}/OAIOrchestratorProfile.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIManagedClustersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
