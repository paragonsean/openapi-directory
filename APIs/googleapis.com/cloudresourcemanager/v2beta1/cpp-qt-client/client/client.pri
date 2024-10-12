QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAICloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperation.h \
    $${PWD}/OAICloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation.h \
    $${PWD}/OAICreateFolderMetadata.h \
    $${PWD}/OAICreateProjectMetadata.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIFolder.h \
    $${PWD}/OAIFolderOperation.h \
    $${PWD}/OAIFolderOperationError.h \
    $${PWD}/OAIGetIamPolicyRequest.h \
    $${PWD}/OAIGetPolicyOptions.h \
    $${PWD}/OAIListFoldersResponse.h \
    $${PWD}/OAIMoveFolderMetadata.h \
    $${PWD}/OAIMoveFolderRequest.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIProjectCreationStatus.h \
    $${PWD}/OAISearchFoldersRequest.h \
    $${PWD}/OAISearchFoldersResponse.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
# APIs
    $${PWD}/OAIFoldersApi.h \
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
    $${PWD}/OAIAuditConfig.cpp \
    $${PWD}/OAIAuditLogConfig.cpp \
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAICloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperation.cpp \
    $${PWD}/OAICloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation.cpp \
    $${PWD}/OAICreateFolderMetadata.cpp \
    $${PWD}/OAICreateProjectMetadata.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIFolder.cpp \
    $${PWD}/OAIFolderOperation.cpp \
    $${PWD}/OAIFolderOperationError.cpp \
    $${PWD}/OAIGetIamPolicyRequest.cpp \
    $${PWD}/OAIGetPolicyOptions.cpp \
    $${PWD}/OAIListFoldersResponse.cpp \
    $${PWD}/OAIMoveFolderMetadata.cpp \
    $${PWD}/OAIMoveFolderRequest.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIProjectCreationStatus.cpp \
    $${PWD}/OAISearchFoldersRequest.cpp \
    $${PWD}/OAISearchFoldersResponse.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIFoldersApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
