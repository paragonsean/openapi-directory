QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswered.h \
    $${PWD}/OAIAttachmentViewModel.h \
    $${PWD}/OAIDailyReportViewModel.h \
    $${PWD}/OAIDailyReportViewModelItem.h \
    $${PWD}/OAIDailyReportViewModelSearchResult.h \
    $${PWD}/OAIGroupedQuestionViewModel.h \
    $${PWD}/OAIHouseEnum.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAILinkedStatements.h \
    $${PWD}/OAIMemberViewModel.h \
    $${PWD}/OAIProblemDetails.h \
    $${PWD}/OAIQuestionStatusEnum.h \
    $${PWD}/OAIQuestionsViewModel.h \
    $${PWD}/OAIQuestionsViewModelItem.h \
    $${PWD}/OAIQuestionsViewModelSearchResult.h \
    $${PWD}/OAIStatementLinkTypeEnum.h \
    $${PWD}/OAIStatementsViewModel.h \
    $${PWD}/OAIStatementsViewModelItem.h \
    $${PWD}/OAIStatementsViewModelSearchResult.h \
# APIs
    $${PWD}/OAIDailyReportsApi.h \
    $${PWD}/OAIWrittenQuestionsApi.h \
    $${PWD}/OAIWrittenStatementsApi.h \
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
    $${PWD}/OAIAnswered.cpp \
    $${PWD}/OAIAttachmentViewModel.cpp \
    $${PWD}/OAIDailyReportViewModel.cpp \
    $${PWD}/OAIDailyReportViewModelItem.cpp \
    $${PWD}/OAIDailyReportViewModelSearchResult.cpp \
    $${PWD}/OAIGroupedQuestionViewModel.cpp \
    $${PWD}/OAIHouseEnum.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAILinkedStatements.cpp \
    $${PWD}/OAIMemberViewModel.cpp \
    $${PWD}/OAIProblemDetails.cpp \
    $${PWD}/OAIQuestionStatusEnum.cpp \
    $${PWD}/OAIQuestionsViewModel.cpp \
    $${PWD}/OAIQuestionsViewModelItem.cpp \
    $${PWD}/OAIQuestionsViewModelSearchResult.cpp \
    $${PWD}/OAIStatementLinkTypeEnum.cpp \
    $${PWD}/OAIStatementsViewModel.cpp \
    $${PWD}/OAIStatementsViewModelItem.cpp \
    $${PWD}/OAIStatementsViewModelSearchResult.cpp \
# APIs
    $${PWD}/OAIDailyReportsApi.cpp \
    $${PWD}/OAIWrittenQuestionsApi.cpp \
    $${PWD}/OAIWrittenStatementsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
