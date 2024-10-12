QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIAuthorizationLoggingOptions.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAICloudAuditOptions.h \
    $${PWD}/OAICondition.h \
    $${PWD}/OAICounterOptions.h \
    $${PWD}/OAICustomField.h \
    $${PWD}/OAIDataAccessOptions.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAILogConfig.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIRule.h \
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
    $${PWD}/OAIAuthorizationLoggingOptions.cpp \
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAICloudAuditOptions.cpp \
    $${PWD}/OAICondition.cpp \
    $${PWD}/OAICounterOptions.cpp \
    $${PWD}/OAICustomField.cpp \
    $${PWD}/OAIDataAccessOptions.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILogConfig.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIRule.cpp \
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
