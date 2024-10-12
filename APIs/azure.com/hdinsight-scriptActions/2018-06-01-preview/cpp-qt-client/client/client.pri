QT += network

HEADERS += \
# Models
    $${PWD}/OAIClusterListRuntimeScriptActionDetailResult.h \
    $${PWD}/OAIClusterListRuntimeScriptActionDetailResult_value_inner.h \
    $${PWD}/OAIClusters_ExecuteScriptActions_default_response.h \
    $${PWD}/OAIClusters_ExecuteScriptActions_request.h \
    $${PWD}/OAIClusters_ExecuteScriptActions_request_scriptActions_inner.h \
    $${PWD}/OAIScriptAction.h \
    $${PWD}/OAIScriptActionExecutionHistoryList.h \
    $${PWD}/OAIScriptActionPersistedGetResponseSpec.h \
    $${PWD}/OAIScriptActionsList.h \
    $${PWD}/OAIScriptActions_GetExecutionDetail_200_response.h \
    $${PWD}/OAIScriptActions_GetExecutionDetail_200_response_allOf_executionSummary_inner.h \
# APIs
    $${PWD}/OAIClustersApi.h \
    $${PWD}/OAIPromoteApi.h \
    $${PWD}/OAIScriptActionsApi.h \
    $${PWD}/OAIScriptExecutionHistoryApi.h \
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
    $${PWD}/OAIClusterListRuntimeScriptActionDetailResult.cpp \
    $${PWD}/OAIClusterListRuntimeScriptActionDetailResult_value_inner.cpp \
    $${PWD}/OAIClusters_ExecuteScriptActions_default_response.cpp \
    $${PWD}/OAIClusters_ExecuteScriptActions_request.cpp \
    $${PWD}/OAIClusters_ExecuteScriptActions_request_scriptActions_inner.cpp \
    $${PWD}/OAIScriptAction.cpp \
    $${PWD}/OAIScriptActionExecutionHistoryList.cpp \
    $${PWD}/OAIScriptActionPersistedGetResponseSpec.cpp \
    $${PWD}/OAIScriptActionsList.cpp \
    $${PWD}/OAIScriptActions_GetExecutionDetail_200_response.cpp \
    $${PWD}/OAIScriptActions_GetExecutionDetail_200_response_allOf_executionSummary_inner.cpp \
# APIs
    $${PWD}/OAIClustersApi.cpp \
    $${PWD}/OAIPromoteApi.cpp \
    $${PWD}/OAIScriptActionsApi.cpp \
    $${PWD}/OAIScriptExecutionHistoryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
