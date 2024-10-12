QT += network

HEADERS += \
# Models
    $${PWD}/OAIDetectedLanguage.h \
    $${PWD}/OAIDocumentStatistics.h \
    $${PWD}/OAIEntitiesBatchResult.h \
    $${PWD}/OAIEntitiesBatchResultItem.h \
    $${PWD}/OAIEntityRecord.h \
    $${PWD}/OAIErrorRecord.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIInternalError.h \
    $${PWD}/OAIKeyPhraseBatchResult.h \
    $${PWD}/OAIKeyPhraseBatchResultItem.h \
    $${PWD}/OAILanguageBatchInput.h \
    $${PWD}/OAILanguageBatchResult.h \
    $${PWD}/OAILanguageBatchResultItem.h \
    $${PWD}/OAILanguageInput.h \
    $${PWD}/OAIMatchRecord.h \
    $${PWD}/OAIMultiLanguageBatchInput.h \
    $${PWD}/OAIMultiLanguageInput.h \
    $${PWD}/OAIRequestStatistics.h \
    $${PWD}/OAISentimentBatchResult.h \
    $${PWD}/OAISentimentBatchResultItem.h \
# APIs
    $${PWD}/OAIDetectLanguageApi.h \
    $${PWD}/OAIEntitiesApi.h \
    $${PWD}/OAIKeyPhrasesApi.h \
    $${PWD}/OAISentimentApi.h \
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
    $${PWD}/OAIDetectedLanguage.cpp \
    $${PWD}/OAIDocumentStatistics.cpp \
    $${PWD}/OAIEntitiesBatchResult.cpp \
    $${PWD}/OAIEntitiesBatchResultItem.cpp \
    $${PWD}/OAIEntityRecord.cpp \
    $${PWD}/OAIErrorRecord.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIInternalError.cpp \
    $${PWD}/OAIKeyPhraseBatchResult.cpp \
    $${PWD}/OAIKeyPhraseBatchResultItem.cpp \
    $${PWD}/OAILanguageBatchInput.cpp \
    $${PWD}/OAILanguageBatchResult.cpp \
    $${PWD}/OAILanguageBatchResultItem.cpp \
    $${PWD}/OAILanguageInput.cpp \
    $${PWD}/OAIMatchRecord.cpp \
    $${PWD}/OAIMultiLanguageBatchInput.cpp \
    $${PWD}/OAIMultiLanguageInput.cpp \
    $${PWD}/OAIRequestStatistics.cpp \
    $${PWD}/OAISentimentBatchResult.cpp \
    $${PWD}/OAISentimentBatchResultItem.cpp \
# APIs
    $${PWD}/OAIDetectLanguageApi.cpp \
    $${PWD}/OAIEntitiesApi.cpp \
    $${PWD}/OAIKeyPhrasesApi.cpp \
    $${PWD}/OAISentimentApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
