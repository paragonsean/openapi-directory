QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeviceService.h \
    $${PWD}/OAIDeviceServiceCheckNameAvailabilityParameters.h \
    $${PWD}/OAIDeviceServiceDescriptionListResult.h \
    $${PWD}/OAIDeviceServiceNameAvailabilityInfo.h \
    $${PWD}/OAIDeviceServiceProperties.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIOperationDisplayInfo.h \
    $${PWD}/OAIOperationEntity.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITrackedResource.h \
# APIs
    $${PWD}/OAICheckDeviceServiceNameAvailabilityApi.h \
    $${PWD}/OAIDeviceServicesApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIDeviceService.cpp \
    $${PWD}/OAIDeviceServiceCheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIDeviceServiceDescriptionListResult.cpp \
    $${PWD}/OAIDeviceServiceNameAvailabilityInfo.cpp \
    $${PWD}/OAIDeviceServiceProperties.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIOperationDisplayInfo.cpp \
    $${PWD}/OAIOperationEntity.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
# APIs
    $${PWD}/OAICheckDeviceServiceNameAvailabilityApi.cpp \
    $${PWD}/OAIDeviceServicesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
