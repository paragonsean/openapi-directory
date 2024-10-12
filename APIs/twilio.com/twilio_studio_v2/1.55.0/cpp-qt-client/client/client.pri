QT += network

HEADERS += \
# Models
    $${PWD}/OAIExecution_enum_status.h \
    $${PWD}/OAIFlow_enum_status.h \
    $${PWD}/OAIFlow_revision_enum_status.h \
    $${PWD}/OAIFlow_validate_enum_status.h \
    $${PWD}/OAIListExecutionResponse.h \
    $${PWD}/OAIListExecutionStepResponse.h \
    $${PWD}/OAIListFlowResponse.h \
    $${PWD}/OAIListFlowResponse_meta.h \
    $${PWD}/OAIListFlowRevisionResponse.h \
    $${PWD}/OAIStudio_v2_flow.h \
    $${PWD}/OAIStudio_v2_flow_execution.h \
    $${PWD}/OAIStudio_v2_flow_execution_execution_context.h \
    $${PWD}/OAIStudio_v2_flow_execution_execution_step.h \
    $${PWD}/OAIStudio_v2_flow_execution_execution_step_execution_step_context.h \
    $${PWD}/OAIStudio_v2_flow_flow_revision.h \
    $${PWD}/OAIStudio_v2_flow_test_user.h \
    $${PWD}/OAIStudio_v2_flow_validate.h \
# APIs
    $${PWD}/OAIStudioV2ExecutionApi.h \
    $${PWD}/OAIStudioV2ExecutionContextApi.h \
    $${PWD}/OAIStudioV2ExecutionStepApi.h \
    $${PWD}/OAIStudioV2ExecutionStepContextApi.h \
    $${PWD}/OAIStudioV2FlowApi.h \
    $${PWD}/OAIStudioV2FlowRevisionApi.h \
    $${PWD}/OAIStudioV2FlowTestUserApi.h \
    $${PWD}/OAIStudioV2FlowValidateApi.h \
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
    $${PWD}/OAIExecution_enum_status.cpp \
    $${PWD}/OAIFlow_enum_status.cpp \
    $${PWD}/OAIFlow_revision_enum_status.cpp \
    $${PWD}/OAIFlow_validate_enum_status.cpp \
    $${PWD}/OAIListExecutionResponse.cpp \
    $${PWD}/OAIListExecutionStepResponse.cpp \
    $${PWD}/OAIListFlowResponse.cpp \
    $${PWD}/OAIListFlowResponse_meta.cpp \
    $${PWD}/OAIListFlowRevisionResponse.cpp \
    $${PWD}/OAIStudio_v2_flow.cpp \
    $${PWD}/OAIStudio_v2_flow_execution.cpp \
    $${PWD}/OAIStudio_v2_flow_execution_execution_context.cpp \
    $${PWD}/OAIStudio_v2_flow_execution_execution_step.cpp \
    $${PWD}/OAIStudio_v2_flow_execution_execution_step_execution_step_context.cpp \
    $${PWD}/OAIStudio_v2_flow_flow_revision.cpp \
    $${PWD}/OAIStudio_v2_flow_test_user.cpp \
    $${PWD}/OAIStudio_v2_flow_validate.cpp \
# APIs
    $${PWD}/OAIStudioV2ExecutionApi.cpp \
    $${PWD}/OAIStudioV2ExecutionContextApi.cpp \
    $${PWD}/OAIStudioV2ExecutionStepApi.cpp \
    $${PWD}/OAIStudioV2ExecutionStepContextApi.cpp \
    $${PWD}/OAIStudioV2FlowApi.cpp \
    $${PWD}/OAIStudioV2FlowRevisionApi.cpp \
    $${PWD}/OAIStudioV2FlowTestUserApi.cpp \
    $${PWD}/OAIStudioV2FlowValidateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
