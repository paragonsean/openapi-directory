QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssetItem.h \
    $${PWD}/OAIAssetLocation.h \
    $${PWD}/OAIColumnSpecification.h \
    $${PWD}/OAICommitmentPlan.h \
    $${PWD}/OAIDiagnosticsConfiguration.h \
    $${PWD}/OAIExampleRequest.h \
    $${PWD}/OAIGraphEdge.h \
    $${PWD}/OAIGraphNode.h \
    $${PWD}/OAIGraphPackage.h \
    $${PWD}/OAIGraphParameter.h \
    $${PWD}/OAIGraphParameterLink.h \
    $${PWD}/OAIInputPort.h \
    $${PWD}/OAIMachineLearningWorkspace.h \
    $${PWD}/OAIModeValueInfo.h \
    $${PWD}/OAIModuleAssetParameter.h \
    $${PWD}/OAIOutputPort.h \
    $${PWD}/OAIPaginatedWebServicesList.h \
    $${PWD}/OAIRealtimeConfiguration.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIServiceInputOutputSpecification.h \
    $${PWD}/OAIStorageAccount.h \
    $${PWD}/OAITableSpecification.h \
    $${PWD}/OAIWebService.h \
    $${PWD}/OAIWebServiceKeys.h \
    $${PWD}/OAIWebServiceProperties.h \
    $${PWD}/OAIWebServicePropertiesForGraph.h \
# APIs
    $${PWD}/OAIWebServicesApi.h \
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
    $${PWD}/OAIAssetItem.cpp \
    $${PWD}/OAIAssetLocation.cpp \
    $${PWD}/OAIColumnSpecification.cpp \
    $${PWD}/OAICommitmentPlan.cpp \
    $${PWD}/OAIDiagnosticsConfiguration.cpp \
    $${PWD}/OAIExampleRequest.cpp \
    $${PWD}/OAIGraphEdge.cpp \
    $${PWD}/OAIGraphNode.cpp \
    $${PWD}/OAIGraphPackage.cpp \
    $${PWD}/OAIGraphParameter.cpp \
    $${PWD}/OAIGraphParameterLink.cpp \
    $${PWD}/OAIInputPort.cpp \
    $${PWD}/OAIMachineLearningWorkspace.cpp \
    $${PWD}/OAIModeValueInfo.cpp \
    $${PWD}/OAIModuleAssetParameter.cpp \
    $${PWD}/OAIOutputPort.cpp \
    $${PWD}/OAIPaginatedWebServicesList.cpp \
    $${PWD}/OAIRealtimeConfiguration.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIServiceInputOutputSpecification.cpp \
    $${PWD}/OAIStorageAccount.cpp \
    $${PWD}/OAITableSpecification.cpp \
    $${PWD}/OAIWebService.cpp \
    $${PWD}/OAIWebServiceKeys.cpp \
    $${PWD}/OAIWebServiceProperties.cpp \
    $${PWD}/OAIWebServicePropertiesForGraph.cpp \
# APIs
    $${PWD}/OAIWebServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
