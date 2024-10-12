QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudDatapipelinesV1DataflowJobDetails.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Job.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchFlexTemplateParameter.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchFlexTemplateRequest.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchTemplateParameters.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchTemplateRequest.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ListJobsResponse.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ListPipelinesResponse.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Pipeline.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1RunPipelineResponse.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1RuntimeEnvironment.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ScheduleSpec.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1SdkVersion.h \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Workload.h \
    $${PWD}/OAIGoogleRpcStatus.h \
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
    $${PWD}/OAIGoogleCloudDatapipelinesV1DataflowJobDetails.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Job.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchFlexTemplateParameter.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchFlexTemplateRequest.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchTemplateParameters.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1LaunchTemplateRequest.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ListJobsResponse.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ListPipelinesResponse.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Pipeline.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1RunPipelineResponse.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1RuntimeEnvironment.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1ScheduleSpec.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1SdkVersion.cpp \
    $${PWD}/OAIGoogleCloudDatapipelinesV1Workload.cpp \
    $${PWD}/OAIGoogleRpcStatus.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
