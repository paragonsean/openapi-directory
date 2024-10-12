QT += network

HEADERS += \
# Models
    $${PWD}/OAIEngagement_enum_status.h \
    $${PWD}/OAIExecution_enum_status.h \
    $${PWD}/OAIFlow_enum_status.h \
    $${PWD}/OAIListEngagementResponse.h \
    $${PWD}/OAIListExecutionResponse.h \
    $${PWD}/OAIListExecutionStepResponse.h \
    $${PWD}/OAIListFlowResponse.h \
    $${PWD}/OAIListFlowResponse_meta.h \
    $${PWD}/OAIListStepResponse.h \
    $${PWD}/OAIStudio_v1_flow.h \
    $${PWD}/OAIStudio_v1_flow_engagement.h \
    $${PWD}/OAIStudio_v1_flow_engagement_engagement_context.h \
    $${PWD}/OAIStudio_v1_flow_engagement_step.h \
    $${PWD}/OAIStudio_v1_flow_engagement_step_step_context.h \
    $${PWD}/OAIStudio_v1_flow_execution.h \
    $${PWD}/OAIStudio_v1_flow_execution_execution_context.h \
    $${PWD}/OAIStudio_v1_flow_execution_execution_step.h \
    $${PWD}/OAIStudio_v1_flow_execution_execution_step_execution_step_context.h \
# APIs
    $${PWD}/OAIStudioV1EngagementApi.h \
    $${PWD}/OAIStudioV1EngagementContextApi.h \
    $${PWD}/OAIStudioV1ExecutionApi.h \
    $${PWD}/OAIStudioV1ExecutionContextApi.h \
    $${PWD}/OAIStudioV1ExecutionStepApi.h \
    $${PWD}/OAIStudioV1ExecutionStepContextApi.h \
    $${PWD}/OAIStudioV1FlowApi.h \
    $${PWD}/OAIStudioV1StepApi.h \
    $${PWD}/OAIStudioV1StepContextApi.h \
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
    $${PWD}/OAIEngagement_enum_status.cpp \
    $${PWD}/OAIExecution_enum_status.cpp \
    $${PWD}/OAIFlow_enum_status.cpp \
    $${PWD}/OAIListEngagementResponse.cpp \
    $${PWD}/OAIListExecutionResponse.cpp \
    $${PWD}/OAIListExecutionStepResponse.cpp \
    $${PWD}/OAIListFlowResponse.cpp \
    $${PWD}/OAIListFlowResponse_meta.cpp \
    $${PWD}/OAIListStepResponse.cpp \
    $${PWD}/OAIStudio_v1_flow.cpp \
    $${PWD}/OAIStudio_v1_flow_engagement.cpp \
    $${PWD}/OAIStudio_v1_flow_engagement_engagement_context.cpp \
    $${PWD}/OAIStudio_v1_flow_engagement_step.cpp \
    $${PWD}/OAIStudio_v1_flow_engagement_step_step_context.cpp \
    $${PWD}/OAIStudio_v1_flow_execution.cpp \
    $${PWD}/OAIStudio_v1_flow_execution_execution_context.cpp \
    $${PWD}/OAIStudio_v1_flow_execution_execution_step.cpp \
    $${PWD}/OAIStudio_v1_flow_execution_execution_step_execution_step_context.cpp \
# APIs
    $${PWD}/OAIStudioV1EngagementApi.cpp \
    $${PWD}/OAIStudioV1EngagementContextApi.cpp \
    $${PWD}/OAIStudioV1ExecutionApi.cpp \
    $${PWD}/OAIStudioV1ExecutionContextApi.cpp \
    $${PWD}/OAIStudioV1ExecutionStepApi.cpp \
    $${PWD}/OAIStudioV1ExecutionStepContextApi.cpp \
    $${PWD}/OAIStudioV1FlowApi.cpp \
    $${PWD}/OAIStudioV1StepApi.cpp \
    $${PWD}/OAIStudioV1StepContextApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
