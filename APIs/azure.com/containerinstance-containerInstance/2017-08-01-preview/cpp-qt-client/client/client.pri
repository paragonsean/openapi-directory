QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureFileVolume.h \
    $${PWD}/OAIContainer.h \
    $${PWD}/OAIContainerEvent.h \
    $${PWD}/OAIContainerGroup.h \
    $${PWD}/OAIContainerGroupListResult.h \
    $${PWD}/OAIContainerGroup_allOf_properties.h \
    $${PWD}/OAIContainerPort.h \
    $${PWD}/OAIContainerProperties.h \
    $${PWD}/OAIContainerProperties_instanceView.h \
    $${PWD}/OAIContainerState.h \
    $${PWD}/OAIEnvironmentVariable.h \
    $${PWD}/OAIImageRegistryCredential.h \
    $${PWD}/OAIIpAddress.h \
    $${PWD}/OAILogs.h \
    $${PWD}/OAIPort.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceLimits.h \
    $${PWD}/OAIResourceRequests.h \
    $${PWD}/OAIResourceRequirements.h \
    $${PWD}/OAIVolume.h \
    $${PWD}/OAIVolumeMount.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAzureFileVolume.cpp \
    $${PWD}/OAIContainer.cpp \
    $${PWD}/OAIContainerEvent.cpp \
    $${PWD}/OAIContainerGroup.cpp \
    $${PWD}/OAIContainerGroupListResult.cpp \
    $${PWD}/OAIContainerGroup_allOf_properties.cpp \
    $${PWD}/OAIContainerPort.cpp \
    $${PWD}/OAIContainerProperties.cpp \
    $${PWD}/OAIContainerProperties_instanceView.cpp \
    $${PWD}/OAIContainerState.cpp \
    $${PWD}/OAIEnvironmentVariable.cpp \
    $${PWD}/OAIImageRegistryCredential.cpp \
    $${PWD}/OAIIpAddress.cpp \
    $${PWD}/OAILogs.cpp \
    $${PWD}/OAIPort.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceLimits.cpp \
    $${PWD}/OAIResourceRequests.cpp \
    $${PWD}/OAIResourceRequirements.cpp \
    $${PWD}/OAIVolume.cpp \
    $${PWD}/OAIVolumeMount.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
