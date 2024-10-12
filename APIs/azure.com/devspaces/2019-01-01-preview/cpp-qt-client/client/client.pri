QT += network

HEADERS += \
# Models
    $${PWD}/OAIContainerHostMapping.h \
    $${PWD}/OAIController.h \
    $${PWD}/OAIControllerConnectionDetails.h \
    $${PWD}/OAIControllerConnectionDetailsList.h \
    $${PWD}/OAIControllerList.h \
    $${PWD}/OAIControllerProperties.h \
    $${PWD}/OAIControllerUpdateParameters.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIKubernetesConnectionDetails.h \
    $${PWD}/OAIOrchestratorSpecificConnectionDetails.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceProviderOperationDefinition.h \
    $${PWD}/OAIResourceProviderOperationDisplay.h \
    $${PWD}/OAIResourceProviderOperationList.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAITrackedResource.h \
# APIs
    $${PWD}/OAIContainerHostMappingsApi.h \
    $${PWD}/OAIControllersApi.h \
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
    $${PWD}/OAIContainerHostMapping.cpp \
    $${PWD}/OAIController.cpp \
    $${PWD}/OAIControllerConnectionDetails.cpp \
    $${PWD}/OAIControllerConnectionDetailsList.cpp \
    $${PWD}/OAIControllerList.cpp \
    $${PWD}/OAIControllerProperties.cpp \
    $${PWD}/OAIControllerUpdateParameters.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIKubernetesConnectionDetails.cpp \
    $${PWD}/OAIOrchestratorSpecificConnectionDetails.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceProviderOperationDefinition.cpp \
    $${PWD}/OAIResourceProviderOperationDisplay.cpp \
    $${PWD}/OAIResourceProviderOperationList.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAITrackedResource.cpp \
# APIs
    $${PWD}/OAIContainerHostMappingsApi.cpp \
    $${PWD}/OAIControllersApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
