QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIReconciliationOperationMetadata.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
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
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIReconciliationOperationMetadata.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
