QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssignment.h \
    $${PWD}/OAIAssignmentList.h \
    $${PWD}/OAIAssignmentLockSettings.h \
    $${PWD}/OAIAssignmentProperties.h \
    $${PWD}/OAIAssignmentStatus.h \
    $${PWD}/OAIAzureResourceBase.h \
    $${PWD}/OAIBlueprintResourcePropertiesBase.h \
    $${PWD}/OAIBlueprintResourceStatusBase.h \
    $${PWD}/OAIKeyVaultReference.h \
    $${PWD}/OAIManagedServiceIdentity.h \
    $${PWD}/OAIParameterValue.h \
    $${PWD}/OAIParameterValueBase.h \
    $${PWD}/OAIResourceGroupValue.h \
    $${PWD}/OAISecretReferenceParameterValue.h \
    $${PWD}/OAISecretValueReference.h \
    $${PWD}/OAITrackedResource.h \
# APIs
    $${PWD}/OAIAssignmentApi.h \
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
    $${PWD}/OAIAssignment.cpp \
    $${PWD}/OAIAssignmentList.cpp \
    $${PWD}/OAIAssignmentLockSettings.cpp \
    $${PWD}/OAIAssignmentProperties.cpp \
    $${PWD}/OAIAssignmentStatus.cpp \
    $${PWD}/OAIAzureResourceBase.cpp \
    $${PWD}/OAIBlueprintResourcePropertiesBase.cpp \
    $${PWD}/OAIBlueprintResourceStatusBase.cpp \
    $${PWD}/OAIKeyVaultReference.cpp \
    $${PWD}/OAIManagedServiceIdentity.cpp \
    $${PWD}/OAIParameterValue.cpp \
    $${PWD}/OAIParameterValueBase.cpp \
    $${PWD}/OAIResourceGroupValue.cpp \
    $${PWD}/OAISecretReferenceParameterValue.cpp \
    $${PWD}/OAISecretValueReference.cpp \
    $${PWD}/OAITrackedResource.cpp \
# APIs
    $${PWD}/OAIAssignmentApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
