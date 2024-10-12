QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAINetworkProfile.h \
    $${PWD}/OAIOSType.h \
    $${PWD}/OAIOpenShiftAgentPoolProfileRole.h \
    $${PWD}/OAIOpenShiftContainerServiceVMSize.h \
    $${PWD}/OAIOpenShiftManagedCluster.h \
    $${PWD}/OAIOpenShiftManagedClusterAADIdentityProvider.h \
    $${PWD}/OAIOpenShiftManagedClusterAgentPoolProfile.h \
    $${PWD}/OAIOpenShiftManagedClusterAuthProfile.h \
    $${PWD}/OAIOpenShiftManagedClusterBaseIdentityProvider.h \
    $${PWD}/OAIOpenShiftManagedClusterIdentityProvider.h \
    $${PWD}/OAIOpenShiftManagedClusterListResult.h \
    $${PWD}/OAIOpenShiftManagedClusterMasterPoolProfile.h \
    $${PWD}/OAIOpenShiftManagedClusterProperties.h \
    $${PWD}/OAIOpenShiftRouterProfile.h \
    $${PWD}/OAIPurchasePlan.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITagsObject.h \
# APIs
    $${PWD}/OAIOpenShiftManagedClustersApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAINetworkProfile.cpp \
    $${PWD}/OAIOSType.cpp \
    $${PWD}/OAIOpenShiftAgentPoolProfileRole.cpp \
    $${PWD}/OAIOpenShiftContainerServiceVMSize.cpp \
    $${PWD}/OAIOpenShiftManagedCluster.cpp \
    $${PWD}/OAIOpenShiftManagedClusterAADIdentityProvider.cpp \
    $${PWD}/OAIOpenShiftManagedClusterAgentPoolProfile.cpp \
    $${PWD}/OAIOpenShiftManagedClusterAuthProfile.cpp \
    $${PWD}/OAIOpenShiftManagedClusterBaseIdentityProvider.cpp \
    $${PWD}/OAIOpenShiftManagedClusterIdentityProvider.cpp \
    $${PWD}/OAIOpenShiftManagedClusterListResult.cpp \
    $${PWD}/OAIOpenShiftManagedClusterMasterPoolProfile.cpp \
    $${PWD}/OAIOpenShiftManagedClusterProperties.cpp \
    $${PWD}/OAIOpenShiftRouterProfile.cpp \
    $${PWD}/OAIPurchasePlan.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITagsObject.cpp \
# APIs
    $${PWD}/OAIOpenShiftManagedClustersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
