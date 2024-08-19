QT += network

HEADERS += \
# Models
    $${PWD}/OAIBootStrapActionParameters.h \
    $${PWD}/OAIDeployActionParameters.h \
    $${PWD}/OAIDeploymentInfo.h \
    $${PWD}/OAIDeploymentStatus.h \
    $${PWD}/OAIExternalAccessInfo.h \
    $${PWD}/OAIProductDeploymentResourceEntity.h \
    $${PWD}/OAIProductDeploymentsInternalState.h \
    $${PWD}/OAIProductDeploymentsList.h \
    $${PWD}/OAIProductDeploymentsProperties.h \
    $${PWD}/OAIProductDeploymentsProperties_error.h \
    $${PWD}/OAIProductDeployments_BootStrap_request.h \
    $${PWD}/OAIProductDeployments_Deploy_request.h \
    $${PWD}/OAIProductDeployments_Unlock_request.h \
    $${PWD}/OAISecretRotationInfo.h \
    $${PWD}/OAIUnlockActionParameters.h \
# APIs
    $${PWD}/OAIProductDeploymentsApi.h \
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
    $${PWD}/OAIBootStrapActionParameters.cpp \
    $${PWD}/OAIDeployActionParameters.cpp \
    $${PWD}/OAIDeploymentInfo.cpp \
    $${PWD}/OAIDeploymentStatus.cpp \
    $${PWD}/OAIExternalAccessInfo.cpp \
    $${PWD}/OAIProductDeploymentResourceEntity.cpp \
    $${PWD}/OAIProductDeploymentsInternalState.cpp \
    $${PWD}/OAIProductDeploymentsList.cpp \
    $${PWD}/OAIProductDeploymentsProperties.cpp \
    $${PWD}/OAIProductDeploymentsProperties_error.cpp \
    $${PWD}/OAIProductDeployments_BootStrap_request.cpp \
    $${PWD}/OAIProductDeployments_Deploy_request.cpp \
    $${PWD}/OAIProductDeployments_Unlock_request.cpp \
    $${PWD}/OAISecretRotationInfo.cpp \
    $${PWD}/OAIUnlockActionParameters.cpp \
# APIs
    $${PWD}/OAIProductDeploymentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
