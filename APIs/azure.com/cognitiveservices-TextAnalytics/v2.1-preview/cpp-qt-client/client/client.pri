QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchInput.h \
    $${PWD}/OAIDetectedLanguage.h \
    $${PWD}/OAIEntitiesBatchResultItemV2dot1.h \
    $${PWD}/OAIEntitiesBatchResultV2dot1.h \
    $${PWD}/OAIEntityRecordV2dot1.h \
    $${PWD}/OAIErrorRecord.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIInput.h \
    $${PWD}/OAIInternalError.h \
    $${PWD}/OAIKeyPhraseBatchResult.h \
    $${PWD}/OAIKeyPhraseBatchResultItem.h \
    $${PWD}/OAILanguageBatchResult.h \
    $${PWD}/OAILanguageBatchResultItem.h \
    $${PWD}/OAIMatchRecordV2dot1.h \
    $${PWD}/OAIMultiLanguageBatchInput.h \
    $${PWD}/OAIMultiLanguageInput.h \
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
    $${PWD}/OAIBatchInput.cpp \
    $${PWD}/OAIDetectedLanguage.cpp \
    $${PWD}/OAIEntitiesBatchResultItemV2dot1.cpp \
    $${PWD}/OAIEntitiesBatchResultV2dot1.cpp \
    $${PWD}/OAIEntityRecordV2dot1.cpp \
    $${PWD}/OAIErrorRecord.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIInput.cpp \
    $${PWD}/OAIInternalError.cpp \
    $${PWD}/OAIKeyPhraseBatchResult.cpp \
    $${PWD}/OAIKeyPhraseBatchResultItem.cpp \
    $${PWD}/OAILanguageBatchResult.cpp \
    $${PWD}/OAILanguageBatchResultItem.cpp \
    $${PWD}/OAIMatchRecordV2dot1.cpp \
    $${PWD}/OAIMultiLanguageBatchInput.cpp \
    $${PWD}/OAIMultiLanguageInput.cpp \
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
