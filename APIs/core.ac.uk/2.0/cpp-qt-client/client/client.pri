QT += network

HEADERS += \
# Models
    $${PWD}/OAIArticle.h \
    $${PWD}/OAIArticleHistoryResponse.h \
    $${PWD}/OAIArticleJournal.h \
    $${PWD}/OAIArticleResponse.h \
    $${PWD}/OAIArticleSearchResponse.h \
    $${PWD}/OAIArticleSimilarResponse.h \
    $${PWD}/OAICitation.h \
    $${PWD}/OAIJournal.h \
    $${PWD}/OAIJournalResponse.h \
    $${PWD}/OAIJournalSearchResponse.h \
    $${PWD}/OAILanguage.h \
    $${PWD}/OAIRawRecordXml.h \
    $${PWD}/OAIRepository.h \
    $${PWD}/OAIRepositoryLocation.h \
    $${PWD}/OAIRepositoryResponse.h \
    $${PWD}/OAIRepositorySearchResponse.h \
    $${PWD}/OAIRepositoryStats.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISearchAllResponse.h \
    $${PWD}/OAISearchRequest.h \
    $${PWD}/OAISimilar.h \
    $${PWD}/OAISimilarRequest.h \
# APIs
    $${PWD}/OAIAllApi.h \
    $${PWD}/OAIArticlesApi.h \
    $${PWD}/OAIJournalsApi.h \
    $${PWD}/OAIRepositoriesApi.h \
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
    $${PWD}/OAIArticle.cpp \
    $${PWD}/OAIArticleHistoryResponse.cpp \
    $${PWD}/OAIArticleJournal.cpp \
    $${PWD}/OAIArticleResponse.cpp \
    $${PWD}/OAIArticleSearchResponse.cpp \
    $${PWD}/OAIArticleSimilarResponse.cpp \
    $${PWD}/OAICitation.cpp \
    $${PWD}/OAIJournal.cpp \
    $${PWD}/OAIJournalResponse.cpp \
    $${PWD}/OAIJournalSearchResponse.cpp \
    $${PWD}/OAILanguage.cpp \
    $${PWD}/OAIRawRecordXml.cpp \
    $${PWD}/OAIRepository.cpp \
    $${PWD}/OAIRepositoryLocation.cpp \
    $${PWD}/OAIRepositoryResponse.cpp \
    $${PWD}/OAIRepositorySearchResponse.cpp \
    $${PWD}/OAIRepositoryStats.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISearchAllResponse.cpp \
    $${PWD}/OAISearchRequest.cpp \
    $${PWD}/OAISimilar.cpp \
    $${PWD}/OAISimilarRequest.cpp \
# APIs
    $${PWD}/OAIAllApi.cpp \
    $${PWD}/OAIArticlesApi.cpp \
    $${PWD}/OAIJournalsApi.cpp \
    $${PWD}/OAIRepositoriesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
