QT += network

HEADERS += \
# Models
    $${PWD}/OAIDetectedLanguage.h \
    $${PWD}/OAIDocumentEntities.h \
    $${PWD}/OAIDocumentError.h \
    $${PWD}/OAIDocumentKeyPhrases.h \
    $${PWD}/OAIDocumentLanguage.h \
    $${PWD}/OAIDocumentLinkedEntities.h \
    $${PWD}/OAIDocumentSentiment.h \
    $${PWD}/OAIDocumentStatistics.h \
    $${PWD}/OAIEntitiesResult.h \
    $${PWD}/OAIEntity.h \
    $${PWD}/OAIEntityLinkingResult.h \
    $${PWD}/OAIInnerError.h \
    $${PWD}/OAIKeyPhraseResult.h \
    $${PWD}/OAILanguageBatchInput.h \
    $${PWD}/OAILanguageInput.h \
    $${PWD}/OAILanguageResult.h \
    $${PWD}/OAILinkedEntity.h \
    $${PWD}/OAIMatch.h \
    $${PWD}/OAIMultiLanguageBatchInput.h \
    $${PWD}/OAIMultiLanguageInput.h \
    $${PWD}/OAIRequestStatistics.h \
    $${PWD}/OAISentenceSentiment.h \
    $${PWD}/OAISentimentConfidenceScorePerLabel.h \
    $${PWD}/OAISentimentResponse.h \
    $${PWD}/OAITextAnalyticsError.h \
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
    $${PWD}/OAIDetectedLanguage.cpp \
    $${PWD}/OAIDocumentEntities.cpp \
    $${PWD}/OAIDocumentError.cpp \
    $${PWD}/OAIDocumentKeyPhrases.cpp \
    $${PWD}/OAIDocumentLanguage.cpp \
    $${PWD}/OAIDocumentLinkedEntities.cpp \
    $${PWD}/OAIDocumentSentiment.cpp \
    $${PWD}/OAIDocumentStatistics.cpp \
    $${PWD}/OAIEntitiesResult.cpp \
    $${PWD}/OAIEntity.cpp \
    $${PWD}/OAIEntityLinkingResult.cpp \
    $${PWD}/OAIInnerError.cpp \
    $${PWD}/OAIKeyPhraseResult.cpp \
    $${PWD}/OAILanguageBatchInput.cpp \
    $${PWD}/OAILanguageInput.cpp \
    $${PWD}/OAILanguageResult.cpp \
    $${PWD}/OAILinkedEntity.cpp \
    $${PWD}/OAIMatch.cpp \
    $${PWD}/OAIMultiLanguageBatchInput.cpp \
    $${PWD}/OAIMultiLanguageInput.cpp \
    $${PWD}/OAIRequestStatistics.cpp \
    $${PWD}/OAISentenceSentiment.cpp \
    $${PWD}/OAISentimentConfidenceScorePerLabel.cpp \
    $${PWD}/OAISentimentResponse.cpp \
    $${PWD}/OAITextAnalyticsError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
