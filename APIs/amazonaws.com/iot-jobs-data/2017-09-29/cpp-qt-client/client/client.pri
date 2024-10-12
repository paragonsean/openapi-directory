QT += network

HEADERS += \
# Models
    $${PWD}/OAIDescribeJobExecutionResponse.h \
    $${PWD}/OAIDescribeJobExecutionResponse_execution.h \
    $${PWD}/OAIGetPendingJobExecutionsResponse.h \
    $${PWD}/OAIJobExecution.h \
    $${PWD}/OAIJobExecutionState.h \
    $${PWD}/OAIJobExecutionStatus.h \
    $${PWD}/OAIJobExecutionSummary.h \
    $${PWD}/OAIStartNextPendingJobExecutionRequest.h \
    $${PWD}/OAIStartNextPendingJobExecutionResponse.h \
    $${PWD}/OAIStartNextPendingJobExecutionResponse_execution.h \
    $${PWD}/OAIStartNextPendingJobExecution_request.h \
    $${PWD}/OAIUpdateJobExecutionRequest.h \
    $${PWD}/OAIUpdateJobExecutionResponse.h \
    $${PWD}/OAIUpdateJobExecutionResponse_executionState.h \
    $${PWD}/OAIUpdateJobExecution_request.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIDescribeJobExecutionResponse.cpp \
    $${PWD}/OAIDescribeJobExecutionResponse_execution.cpp \
    $${PWD}/OAIGetPendingJobExecutionsResponse.cpp \
    $${PWD}/OAIJobExecution.cpp \
    $${PWD}/OAIJobExecutionState.cpp \
    $${PWD}/OAIJobExecutionStatus.cpp \
    $${PWD}/OAIJobExecutionSummary.cpp \
    $${PWD}/OAIStartNextPendingJobExecutionRequest.cpp \
    $${PWD}/OAIStartNextPendingJobExecutionResponse.cpp \
    $${PWD}/OAIStartNextPendingJobExecutionResponse_execution.cpp \
    $${PWD}/OAIStartNextPendingJobExecution_request.cpp \
    $${PWD}/OAIUpdateJobExecutionRequest.cpp \
    $${PWD}/OAIUpdateJobExecutionResponse.cpp \
    $${PWD}/OAIUpdateJobExecutionResponse_executionState.cpp \
    $${PWD}/OAIUpdateJobExecution_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
