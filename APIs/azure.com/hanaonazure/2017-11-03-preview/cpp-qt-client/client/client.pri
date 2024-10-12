QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisk.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIHanaInstance.h \
    $${PWD}/OAIHanaInstanceProperties.h \
    $${PWD}/OAIHanaInstancesListResult.h \
    $${PWD}/OAIHardwareProfile.h \
    $${PWD}/OAIIpAddress.h \
    $${PWD}/OAIMonitoringDetails.h \
    $${PWD}/OAINetworkProfile.h \
    $${PWD}/OAIOSProfile.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISapMonitor.h \
    $${PWD}/OAISapMonitorListResult.h \
    $${PWD}/OAISapMonitorProperties.h \
    $${PWD}/OAIStorageProfile.h \
    $${PWD}/OAITags.h \
# APIs
    $${PWD}/OAIHanaOnAzureApi.h \
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
    $${PWD}/OAIDisk.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIHanaInstance.cpp \
    $${PWD}/OAIHanaInstanceProperties.cpp \
    $${PWD}/OAIHanaInstancesListResult.cpp \
    $${PWD}/OAIHardwareProfile.cpp \
    $${PWD}/OAIIpAddress.cpp \
    $${PWD}/OAIMonitoringDetails.cpp \
    $${PWD}/OAINetworkProfile.cpp \
    $${PWD}/OAIOSProfile.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISapMonitor.cpp \
    $${PWD}/OAISapMonitorListResult.cpp \
    $${PWD}/OAISapMonitorProperties.cpp \
    $${PWD}/OAIStorageProfile.cpp \
    $${PWD}/OAITags.cpp \
# APIs
    $${PWD}/OAIHanaOnAzureApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
