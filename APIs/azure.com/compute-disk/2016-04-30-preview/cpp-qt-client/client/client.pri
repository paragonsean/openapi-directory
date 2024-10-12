QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessUri.h \
    $${PWD}/OAIAccessUriOutput.h \
    $${PWD}/OAIAccessUriRaw.h \
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIApiErrorBase.h \
    $${PWD}/OAICreationData.h \
    $${PWD}/OAIDisk.h \
    $${PWD}/OAIDiskList.h \
    $${PWD}/OAIDiskProperties.h \
    $${PWD}/OAIDiskUpdate.h \
    $${PWD}/OAIDiskUpdateProperties.h \
    $${PWD}/OAIEncryptionSettings.h \
    $${PWD}/OAIGrantAccessData.h \
    $${PWD}/OAIImageDiskReference.h \
    $${PWD}/OAIInnerError.h \
    $${PWD}/OAIKeyVaultAndKeyReference.h \
    $${PWD}/OAIKeyVaultAndSecretReference.h \
    $${PWD}/OAIOperationStatusResponse.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceUpdate.h \
    $${PWD}/OAISnapshot.h \
    $${PWD}/OAISnapshotList.h \
    $${PWD}/OAISnapshotUpdate.h \
    $${PWD}/OAISourceVault.h \
# APIs
    $${PWD}/OAIDisksApi.h \
    $${PWD}/OAISnapshotsApi.h \
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
    $${PWD}/OAIAccessUri.cpp \
    $${PWD}/OAIAccessUriOutput.cpp \
    $${PWD}/OAIAccessUriRaw.cpp \
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIApiErrorBase.cpp \
    $${PWD}/OAICreationData.cpp \
    $${PWD}/OAIDisk.cpp \
    $${PWD}/OAIDiskList.cpp \
    $${PWD}/OAIDiskProperties.cpp \
    $${PWD}/OAIDiskUpdate.cpp \
    $${PWD}/OAIDiskUpdateProperties.cpp \
    $${PWD}/OAIEncryptionSettings.cpp \
    $${PWD}/OAIGrantAccessData.cpp \
    $${PWD}/OAIImageDiskReference.cpp \
    $${PWD}/OAIInnerError.cpp \
    $${PWD}/OAIKeyVaultAndKeyReference.cpp \
    $${PWD}/OAIKeyVaultAndSecretReference.cpp \
    $${PWD}/OAIOperationStatusResponse.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceUpdate.cpp \
    $${PWD}/OAISnapshot.cpp \
    $${PWD}/OAISnapshotList.cpp \
    $${PWD}/OAISnapshotUpdate.cpp \
    $${PWD}/OAISourceVault.cpp \
# APIs
    $${PWD}/OAIDisksApi.cpp \
    $${PWD}/OAISnapshotsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
