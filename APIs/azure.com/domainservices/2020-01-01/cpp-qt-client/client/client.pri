QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIDomainSecuritySettings.h \
    $${PWD}/OAIDomainService.h \
    $${PWD}/OAIDomainServiceListResult.h \
    $${PWD}/OAIDomainServiceProperties.h \
    $${PWD}/OAIHealthAlert.h \
    $${PWD}/OAIHealthMonitor.h \
    $${PWD}/OAILdapsSettings.h \
    $${PWD}/OAINotificationSettings.h \
    $${PWD}/OAIOperationDisplayInfo.h \
    $${PWD}/OAIOperationEntity.h \
    $${PWD}/OAIOperationEntityListResult.h \
    $${PWD}/OAIReplicaSet.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIDomainServicesApi.h \
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
    $${PWD}/OAIDomainSecuritySettings.cpp \
    $${PWD}/OAIDomainService.cpp \
    $${PWD}/OAIDomainServiceListResult.cpp \
    $${PWD}/OAIDomainServiceProperties.cpp \
    $${PWD}/OAIHealthAlert.cpp \
    $${PWD}/OAIHealthMonitor.cpp \
    $${PWD}/OAILdapsSettings.cpp \
    $${PWD}/OAINotificationSettings.cpp \
    $${PWD}/OAIOperationDisplayInfo.cpp \
    $${PWD}/OAIOperationEntity.cpp \
    $${PWD}/OAIOperationEntityListResult.cpp \
    $${PWD}/OAIReplicaSet.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIDomainServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
