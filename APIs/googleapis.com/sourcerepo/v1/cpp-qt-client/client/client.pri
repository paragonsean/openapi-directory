QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListReposResponse.h \
    $${PWD}/OAIMirrorConfig.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIProjectConfig.h \
    $${PWD}/OAIPubsubConfig.h \
    $${PWD}/OAIRepo.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISyncRepoMetadata.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAIUpdateProjectConfigRequest.h \
    $${PWD}/OAIUpdateRepoRequest.h \
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
    $${PWD}/OAIListReposResponse.cpp \
    $${PWD}/OAIMirrorConfig.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIProjectConfig.cpp \
    $${PWD}/OAIPubsubConfig.cpp \
    $${PWD}/OAIRepo.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISyncRepoMetadata.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAIUpdateProjectConfigRequest.cpp \
    $${PWD}/OAIUpdateRepoRequest.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
