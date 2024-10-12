QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectRequest.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIKeywordJobRank.h \
    $${PWD}/OAIKeywordJobSerp.h \
    $${PWD}/OAIKeywordTask.h \
    $${PWD}/OAIRankCollectResponse.h \
    $${PWD}/OAIRankCollectResponse_tasks_inner.h \
    $${PWD}/OAIRankCollectResponse_tasks_inner_task_id.h \
    $${PWD}/OAIRankSubmitRequest.h \
    $${PWD}/OAIRankSubmitResponse.h \
    $${PWD}/OAISerpCollectResponse.h \
    $${PWD}/OAISerpCollectResponse_tasks_inner.h \
    $${PWD}/OAISerpCollectResponse_tasks_inner_task_id.h \
    $${PWD}/OAISerpCollectResponse_tasks_inner_task_id_organic_results_inner.h \
    $${PWD}/OAISerpSubmitRequest.h \
    $${PWD}/OAISerpSubmitResponse.h \
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
    $${PWD}/OAICollectRequest.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIKeywordJobRank.cpp \
    $${PWD}/OAIKeywordJobSerp.cpp \
    $${PWD}/OAIKeywordTask.cpp \
    $${PWD}/OAIRankCollectResponse.cpp \
    $${PWD}/OAIRankCollectResponse_tasks_inner.cpp \
    $${PWD}/OAIRankCollectResponse_tasks_inner_task_id.cpp \
    $${PWD}/OAIRankSubmitRequest.cpp \
    $${PWD}/OAIRankSubmitResponse.cpp \
    $${PWD}/OAISerpCollectResponse.cpp \
    $${PWD}/OAISerpCollectResponse_tasks_inner.cpp \
    $${PWD}/OAISerpCollectResponse_tasks_inner_task_id.cpp \
    $${PWD}/OAISerpCollectResponse_tasks_inner_task_id_organic_results_inner.cpp \
    $${PWD}/OAISerpSubmitRequest.cpp \
    $${PWD}/OAISerpSubmitResponse.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
