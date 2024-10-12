QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddOrReplaceDocuments_request_inner.h \
    $${PWD}/OAIAddOrUpdateDocuments_request_inner.h \
    $${PWD}/OAICreateAKey_request.h \
    $${PWD}/OAICreateIndexWithPrimaryKey_request.h \
    $${PWD}/OAISearchInIndex1_request.h \
    $${PWD}/OAISearchOneOrMoreIndexes_request.h \
    $${PWD}/OAISearchOneOrMoreIndexes_request_queries_inner.h \
    $${PWD}/OAISwapIndexes_request_inner.h \
    $${PWD}/OAIUpdateAKey_request.h \
    $${PWD}/OAIUpdateFaceting_request.h \
    $${PWD}/OAIUpdateIndex_request.h \
    $${PWD}/OAIUpdatePagination_request.h \
    $${PWD}/OAIUpdateSettings_request.h \
    $${PWD}/OAIUpdateSynonyms_request.h \
    $${PWD}/OAIUpdateTypoTolerance_request.h \
    $${PWD}/OAIUpdateTypoTolerance_request_minWordSizeForTypos.h \
# APIs
    $${PWD}/OAIDocumentsApi.h \
    $${PWD}/OAIDumpsApi.h \
    $${PWD}/OAIIndexesApi.h \
    $${PWD}/OAIKeyManagementApi.h \
    $${PWD}/OAIMultiSearchApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAISettingsApi.h \
    $${PWD}/OAIStatsApi.h \
    $${PWD}/OAISubRoutesApi.h \
    $${PWD}/OAITasksApi.h \
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
    $${PWD}/OAIAddOrReplaceDocuments_request_inner.cpp \
    $${PWD}/OAIAddOrUpdateDocuments_request_inner.cpp \
    $${PWD}/OAICreateAKey_request.cpp \
    $${PWD}/OAICreateIndexWithPrimaryKey_request.cpp \
    $${PWD}/OAISearchInIndex1_request.cpp \
    $${PWD}/OAISearchOneOrMoreIndexes_request.cpp \
    $${PWD}/OAISearchOneOrMoreIndexes_request_queries_inner.cpp \
    $${PWD}/OAISwapIndexes_request_inner.cpp \
    $${PWD}/OAIUpdateAKey_request.cpp \
    $${PWD}/OAIUpdateFaceting_request.cpp \
    $${PWD}/OAIUpdateIndex_request.cpp \
    $${PWD}/OAIUpdatePagination_request.cpp \
    $${PWD}/OAIUpdateSettings_request.cpp \
    $${PWD}/OAIUpdateSynonyms_request.cpp \
    $${PWD}/OAIUpdateTypoTolerance_request.cpp \
    $${PWD}/OAIUpdateTypoTolerance_request_minWordSizeForTypos.cpp \
# APIs
    $${PWD}/OAIDocumentsApi.cpp \
    $${PWD}/OAIDumpsApi.cpp \
    $${PWD}/OAIIndexesApi.cpp \
    $${PWD}/OAIKeyManagementApi.cpp \
    $${PWD}/OAIMultiSearchApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAISettingsApi.cpp \
    $${PWD}/OAIStatsApi.cpp \
    $${PWD}/OAISubRoutesApi.cpp \
    $${PWD}/OAITasksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
