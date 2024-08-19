QT += network

HEADERS += \
# Models
    $${PWD}/OAIPermission.h \
    $${PWD}/OAIPermissionGetResult.h \
    $${PWD}/OAIProviderOperation.h \
    $${PWD}/OAIProviderOperationsMetadata.h \
    $${PWD}/OAIProviderOperationsMetadataListResult.h \
    $${PWD}/OAIResourceType.h \
    $${PWD}/OAIRoleAssignment.h \
    $${PWD}/OAIRoleAssignmentCreateParameters.h \
    $${PWD}/OAIRoleAssignmentFilter.h \
    $${PWD}/OAIRoleAssignmentListResult.h \
    $${PWD}/OAIRoleAssignmentProperties.h \
    $${PWD}/OAIRoleAssignmentPropertiesWithScope.h \
    $${PWD}/OAIRoleDefinition.h \
    $${PWD}/OAIRoleDefinitionFilter.h \
    $${PWD}/OAIRoleDefinitionListResult.h \
    $${PWD}/OAIRoleDefinitionProperties.h \
# APIs
    $${PWD}/OAIElevateAccessApi.h \
    $${PWD}/OAIPermissionsApi.h \
    $${PWD}/OAIProviderOperationsMetadataApi.h \
    $${PWD}/OAIRoleAssignmentsApi.h \
    $${PWD}/OAIRoleDefinitionsApi.h \
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
    $${PWD}/OAIPermission.cpp \
    $${PWD}/OAIPermissionGetResult.cpp \
    $${PWD}/OAIProviderOperation.cpp \
    $${PWD}/OAIProviderOperationsMetadata.cpp \
    $${PWD}/OAIProviderOperationsMetadataListResult.cpp \
    $${PWD}/OAIResourceType.cpp \
    $${PWD}/OAIRoleAssignment.cpp \
    $${PWD}/OAIRoleAssignmentCreateParameters.cpp \
    $${PWD}/OAIRoleAssignmentFilter.cpp \
    $${PWD}/OAIRoleAssignmentListResult.cpp \
    $${PWD}/OAIRoleAssignmentProperties.cpp \
    $${PWD}/OAIRoleAssignmentPropertiesWithScope.cpp \
    $${PWD}/OAIRoleDefinition.cpp \
    $${PWD}/OAIRoleDefinitionFilter.cpp \
    $${PWD}/OAIRoleDefinitionListResult.cpp \
    $${PWD}/OAIRoleDefinitionProperties.cpp \
# APIs
    $${PWD}/OAIElevateAccessApi.cpp \
    $${PWD}/OAIPermissionsApi.cpp \
    $${PWD}/OAIProviderOperationsMetadataApi.cpp \
    $${PWD}/OAIRoleAssignmentsApi.cpp \
    $${PWD}/OAIRoleDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
