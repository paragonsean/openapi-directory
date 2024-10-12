QT += network

HEADERS += \
# Models
    $${PWD}/OAIApigatewayApi.h \
    $${PWD}/OAIApigatewayApiConfig.h \
    $${PWD}/OAIApigatewayApiConfigFile.h \
    $${PWD}/OAIApigatewayApiConfigGrpcServiceDefinition.h \
    $${PWD}/OAIApigatewayApiConfigOpenApiDocument.h \
    $${PWD}/OAIApigatewayAuditConfig.h \
    $${PWD}/OAIApigatewayAuditLogConfig.h \
    $${PWD}/OAIApigatewayBinding.h \
    $${PWD}/OAIApigatewayExpr.h \
    $${PWD}/OAIApigatewayGateway.h \
    $${PWD}/OAIApigatewayListApiConfigsResponse.h \
    $${PWD}/OAIApigatewayListApisResponse.h \
    $${PWD}/OAIApigatewayListGatewaysResponse.h \
    $${PWD}/OAIApigatewayListLocationsResponse.h \
    $${PWD}/OAIApigatewayListOperationsResponse.h \
    $${PWD}/OAIApigatewayLocation.h \
    $${PWD}/OAIApigatewayOperation.h \
    $${PWD}/OAIApigatewayOperationMetadata.h \
    $${PWD}/OAIApigatewayOperationMetadataDiagnostic.h \
    $${PWD}/OAIApigatewayPolicy.h \
    $${PWD}/OAIApigatewaySetIamPolicyRequest.h \
    $${PWD}/OAIApigatewayStatus.h \
    $${PWD}/OAIApigatewayTestIamPermissionsRequest.h \
    $${PWD}/OAIApigatewayTestIamPermissionsResponse.h \
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
    $${PWD}/OAIApigatewayApi.cpp \
    $${PWD}/OAIApigatewayApiConfig.cpp \
    $${PWD}/OAIApigatewayApiConfigFile.cpp \
    $${PWD}/OAIApigatewayApiConfigGrpcServiceDefinition.cpp \
    $${PWD}/OAIApigatewayApiConfigOpenApiDocument.cpp \
    $${PWD}/OAIApigatewayAuditConfig.cpp \
    $${PWD}/OAIApigatewayAuditLogConfig.cpp \
    $${PWD}/OAIApigatewayBinding.cpp \
    $${PWD}/OAIApigatewayExpr.cpp \
    $${PWD}/OAIApigatewayGateway.cpp \
    $${PWD}/OAIApigatewayListApiConfigsResponse.cpp \
    $${PWD}/OAIApigatewayListApisResponse.cpp \
    $${PWD}/OAIApigatewayListGatewaysResponse.cpp \
    $${PWD}/OAIApigatewayListLocationsResponse.cpp \
    $${PWD}/OAIApigatewayListOperationsResponse.cpp \
    $${PWD}/OAIApigatewayLocation.cpp \
    $${PWD}/OAIApigatewayOperation.cpp \
    $${PWD}/OAIApigatewayOperationMetadata.cpp \
    $${PWD}/OAIApigatewayOperationMetadataDiagnostic.cpp \
    $${PWD}/OAIApigatewayPolicy.cpp \
    $${PWD}/OAIApigatewaySetIamPolicyRequest.cpp \
    $${PWD}/OAIApigatewayStatus.cpp \
    $${PWD}/OAIApigatewayTestIamPermissionsRequest.cpp \
    $${PWD}/OAIApigatewayTestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
