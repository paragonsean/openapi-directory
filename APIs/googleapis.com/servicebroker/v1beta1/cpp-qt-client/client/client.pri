QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Binding.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Broker.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__CreateBindingResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__CreateServiceInstanceResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DashboardClient.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DeleteBindingResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DeleteServiceInstanceResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__GetBindingResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListBindingsResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListBrokersResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListCatalogResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListServiceInstancesResponse.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Operation.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Plan.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Service.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ServiceInstance.h \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__UpdateServiceInstanceResponse.h \
    $${PWD}/OAIGoogleIamV1__Binding.h \
    $${PWD}/OAIGoogleIamV1__Policy.h \
    $${PWD}/OAIGoogleIamV1__SetIamPolicyRequest.h \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsRequest.h \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsResponse.h \
    $${PWD}/OAIGoogleType__Expr.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
    $${PWD}/OAIV1beta1Api.h \
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
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Binding.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Broker.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__CreateBindingResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__CreateServiceInstanceResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DashboardClient.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DeleteBindingResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__DeleteServiceInstanceResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__GetBindingResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListBindingsResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListBrokersResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListCatalogResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ListServiceInstancesResponse.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Operation.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Plan.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__Service.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__ServiceInstance.cpp \
    $${PWD}/OAIGoogleCloudServicebrokerV1beta1__UpdateServiceInstanceResponse.cpp \
    $${PWD}/OAIGoogleIamV1__Binding.cpp \
    $${PWD}/OAIGoogleIamV1__Policy.cpp \
    $${PWD}/OAIGoogleIamV1__SetIamPolicyRequest.cpp \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsRequest.cpp \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsResponse.cpp \
    $${PWD}/OAIGoogleType__Expr.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAIV1beta1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
