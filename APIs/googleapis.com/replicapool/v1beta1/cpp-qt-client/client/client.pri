QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessConfig.h \
    $${PWD}/OAIAction.h \
    $${PWD}/OAIDiskAttachment.h \
    $${PWD}/OAIEnvVariable.h \
    $${PWD}/OAIExistingDisk.h \
    $${PWD}/OAIHealthCheck.h \
    $${PWD}/OAILabel.h \
    $${PWD}/OAIMetadata.h \
    $${PWD}/OAIMetadataItem.h \
    $${PWD}/OAINetworkInterface.h \
    $${PWD}/OAINewDisk.h \
    $${PWD}/OAINewDiskInitializeParams.h \
    $${PWD}/OAIPool.h \
    $${PWD}/OAIPoolsDeleteRequest.h \
    $${PWD}/OAIPoolsListResponse.h \
    $${PWD}/OAIReplica.h \
    $${PWD}/OAIReplicaStatus.h \
    $${PWD}/OAIReplicasDeleteRequest.h \
    $${PWD}/OAIReplicasListResponse.h \
    $${PWD}/OAIServiceAccount.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAITemplate.h \
    $${PWD}/OAIVmParams.h \
# APIs
    $${PWD}/OAIPoolsApi.h \
    $${PWD}/OAIReplicasApi.h \
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
    $${PWD}/OAIAccessConfig.cpp \
    $${PWD}/OAIAction.cpp \
    $${PWD}/OAIDiskAttachment.cpp \
    $${PWD}/OAIEnvVariable.cpp \
    $${PWD}/OAIExistingDisk.cpp \
    $${PWD}/OAIHealthCheck.cpp \
    $${PWD}/OAILabel.cpp \
    $${PWD}/OAIMetadata.cpp \
    $${PWD}/OAIMetadataItem.cpp \
    $${PWD}/OAINetworkInterface.cpp \
    $${PWD}/OAINewDisk.cpp \
    $${PWD}/OAINewDiskInitializeParams.cpp \
    $${PWD}/OAIPool.cpp \
    $${PWD}/OAIPoolsDeleteRequest.cpp \
    $${PWD}/OAIPoolsListResponse.cpp \
    $${PWD}/OAIReplica.cpp \
    $${PWD}/OAIReplicaStatus.cpp \
    $${PWD}/OAIReplicasDeleteRequest.cpp \
    $${PWD}/OAIReplicasListResponse.cpp \
    $${PWD}/OAIServiceAccount.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAITemplate.cpp \
    $${PWD}/OAIVmParams.cpp \
# APIs
    $${PWD}/OAIPoolsApi.cpp \
    $${PWD}/OAIReplicasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
