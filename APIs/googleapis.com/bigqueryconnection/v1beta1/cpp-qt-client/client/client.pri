QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAICloudSqlCredential.h \
    $${PWD}/OAICloudSqlProperties.h \
    $${PWD}/OAIConnection.h \
    $${PWD}/OAIConnectionCredential.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIGetIamPolicyRequest.h \
    $${PWD}/OAIGetPolicyOptions.h \
    $${PWD}/OAIListConnectionsResponse.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAISetIamPolicyRequest.h \
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
    $${PWD}/OAICloudSqlCredential.cpp \
    $${PWD}/OAICloudSqlProperties.cpp \
    $${PWD}/OAIConnection.cpp \
    $${PWD}/OAIConnectionCredential.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIGetIamPolicyRequest.cpp \
    $${PWD}/OAIGetPolicyOptions.cpp \
    $${PWD}/OAIListConnectionsResponse.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
