QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnalyzeCommentRequest.h \
    $${PWD}/OAIAnalyzeCommentResponse.h \
    $${PWD}/OAIArticleAndParentComment.h \
    $${PWD}/OAIAttributeParameters.h \
    $${PWD}/OAIAttributeScores.h \
    $${PWD}/OAIContext.h \
    $${PWD}/OAIScore.h \
    $${PWD}/OAISpanScore.h \
    $${PWD}/OAISuggestCommentScoreRequest.h \
    $${PWD}/OAISuggestCommentScoreResponse.h \
    $${PWD}/OAITextEntry.h \
# APIs
    $${PWD}/OAICommentsApi.h \
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
    $${PWD}/OAIAnalyzeCommentRequest.cpp \
    $${PWD}/OAIAnalyzeCommentResponse.cpp \
    $${PWD}/OAIArticleAndParentComment.cpp \
    $${PWD}/OAIAttributeParameters.cpp \
    $${PWD}/OAIAttributeScores.cpp \
    $${PWD}/OAIContext.cpp \
    $${PWD}/OAIScore.cpp \
    $${PWD}/OAISpanScore.cpp \
    $${PWD}/OAISuggestCommentScoreRequest.cpp \
    $${PWD}/OAISuggestCommentScoreResponse.cpp \
    $${PWD}/OAITextEntry.cpp \
# APIs
    $${PWD}/OAICommentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
