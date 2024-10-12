QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListManagementServersResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIManagementServer.h \
    $${PWD}/OAIManagementURI.h \
    $${PWD}/OAINetworkConfig.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAIWorkforceIdentityBasedManagementURI.h \
    $${PWD}/OAIWorkforceIdentityBasedOAuth2ClientID.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListManagementServersResponse.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIManagementServer.cpp \
    $${PWD}/OAIManagementURI.cpp \
    $${PWD}/OAINetworkConfig.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAIWorkforceIdentityBasedManagementURI.cpp \
    $${PWD}/OAIWorkforceIdentityBasedOAuth2ClientID.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
