QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIEndpoint.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIGetIamPolicyRequest.h \
    $${PWD}/OAIGetPolicyOptions.h \
    $${PWD}/OAIListEndpointsResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListNamespacesResponse.h \
    $${PWD}/OAIListServicesResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAINamespace.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIResolveServiceRequest.h \
    $${PWD}/OAIResolveServiceResponse.h \
    $${PWD}/OAIService.h \
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
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAIEndpoint.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIGetIamPolicyRequest.cpp \
    $${PWD}/OAIGetPolicyOptions.cpp \
    $${PWD}/OAIListEndpointsResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListNamespacesResponse.cpp \
    $${PWD}/OAIListServicesResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAINamespace.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIResolveServiceRequest.cpp \
    $${PWD}/OAIResolveServiceResponse.cpp \
    $${PWD}/OAIService.cpp \
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
