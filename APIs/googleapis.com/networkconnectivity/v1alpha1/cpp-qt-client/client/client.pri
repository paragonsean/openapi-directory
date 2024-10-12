QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditConfig.h \
    $${PWD}/OAIAuditLogConfig.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIGoogleLongrunningListOperationsResponse.h \
    $${PWD}/OAIGoogleLongrunningOperation.h \
    $${PWD}/OAIGoogleRpcStatus.h \
    $${PWD}/OAIHub.h \
    $${PWD}/OAIInternalRange.h \
    $${PWD}/OAIListHubsResponse.h \
    $${PWD}/OAIListInternalRangesResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListSpokesResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIRouterApplianceInstance.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAISpoke.h \
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
    $${PWD}/OAIGoogleLongrunningListOperationsResponse.cpp \
    $${PWD}/OAIGoogleLongrunningOperation.cpp \
    $${PWD}/OAIGoogleRpcStatus.cpp \
    $${PWD}/OAIHub.cpp \
    $${PWD}/OAIInternalRange.cpp \
    $${PWD}/OAIListHubsResponse.cpp \
    $${PWD}/OAIListInternalRangesResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListSpokesResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIRouterApplianceInstance.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAISpoke.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
