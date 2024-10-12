QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIKey.h \
    $${PWD}/OAIAPIKeyVersion.h \
    $${PWD}/OAIAPIKeyVersionChangelog.h \
    $${PWD}/OAIBehavior.h \
    $${PWD}/OAIBehaviourOutput.h \
    $${PWD}/OAIChange.h \
    $${PWD}/OAICheck.h \
    $${PWD}/OAICheckDetails.h \
    $${PWD}/OAICheckDetailsOutput.h \
    $${PWD}/OAICheckOutput.h \
    $${PWD}/OAIChecksOutput.h \
    $${PWD}/OAIComment.h \
    $${PWD}/OAICommentOutput.h \
    $${PWD}/OAICommentsOutput.h \
    $${PWD}/OAICompanySummary.h \
    $${PWD}/OAIConfig.h \
    $${PWD}/OAIContinuousCheck.h \
    $${PWD}/OAIContinuousCheckEntry.h \
    $${PWD}/OAICreateAPIKeyInput.h \
    $${PWD}/OAICreateCommentInput.h \
    $${PWD}/OAICreateRuleInput.h \
    $${PWD}/OAICreateUserInput.h \
    $${PWD}/OAIDatabase.h \
    $${PWD}/OAIDeleteAPIKeyInput.h \
    $${PWD}/OAIDeleteUserInput.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIGetContiuousCheckHistoryOutput.h \
    $${PWD}/OAIGetHealthDashboardInput.h \
    $${PWD}/OAIHook.h \
    $${PWD}/OAIHookOutput.h \
    $${PWD}/OAIListContinuousChecksOutput.h \
    $${PWD}/OAINameFound.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReportOutput.h \
    $${PWD}/OAIReportsOutput.h \
    $${PWD}/OAIRule.h \
    $${PWD}/OAIRuleOutput.h \
    $${PWD}/OAIScore.h \
    $${PWD}/OAIScoreConfig.h \
    $${PWD}/OAIScoreConfigOutput.h \
    $${PWD}/OAIScoreConfigsOutput.h \
    $${PWD}/OAIScoreDetail.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISubscriber.h \
    $${PWD}/OAISummary.h \
    $${PWD}/OAITable.h \
    $${PWD}/OAITableCell.h \
    $${PWD}/OAITableRow.h \
    $${PWD}/OAIUpdateAPIKeyInput.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIVehicleSummary.h \
    $${PWD}/OAIWrongInput.h \
# APIs
    $${PWD}/OAIBehaviorApi.h \
    $${PWD}/OAIChecksApi.h \
    $${PWD}/OAIContinuousApi.h \
    $${PWD}/OAICustomTypeApi.h \
    $${PWD}/OAIHooksApi.h \
    $${PWD}/OAIPdfApi.h \
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIAPIKey.cpp \
    $${PWD}/OAIAPIKeyVersion.cpp \
    $${PWD}/OAIAPIKeyVersionChangelog.cpp \
    $${PWD}/OAIBehavior.cpp \
    $${PWD}/OAIBehaviourOutput.cpp \
    $${PWD}/OAIChange.cpp \
    $${PWD}/OAICheck.cpp \
    $${PWD}/OAICheckDetails.cpp \
    $${PWD}/OAICheckDetailsOutput.cpp \
    $${PWD}/OAICheckOutput.cpp \
    $${PWD}/OAIChecksOutput.cpp \
    $${PWD}/OAIComment.cpp \
    $${PWD}/OAICommentOutput.cpp \
    $${PWD}/OAICommentsOutput.cpp \
    $${PWD}/OAICompanySummary.cpp \
    $${PWD}/OAIConfig.cpp \
    $${PWD}/OAIContinuousCheck.cpp \
    $${PWD}/OAIContinuousCheckEntry.cpp \
    $${PWD}/OAICreateAPIKeyInput.cpp \
    $${PWD}/OAICreateCommentInput.cpp \
    $${PWD}/OAICreateRuleInput.cpp \
    $${PWD}/OAICreateUserInput.cpp \
    $${PWD}/OAIDatabase.cpp \
    $${PWD}/OAIDeleteAPIKeyInput.cpp \
    $${PWD}/OAIDeleteUserInput.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIGetContiuousCheckHistoryOutput.cpp \
    $${PWD}/OAIGetHealthDashboardInput.cpp \
    $${PWD}/OAIHook.cpp \
    $${PWD}/OAIHookOutput.cpp \
    $${PWD}/OAIListContinuousChecksOutput.cpp \
    $${PWD}/OAINameFound.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReportOutput.cpp \
    $${PWD}/OAIReportsOutput.cpp \
    $${PWD}/OAIRule.cpp \
    $${PWD}/OAIRuleOutput.cpp \
    $${PWD}/OAIScore.cpp \
    $${PWD}/OAIScoreConfig.cpp \
    $${PWD}/OAIScoreConfigOutput.cpp \
    $${PWD}/OAIScoreConfigsOutput.cpp \
    $${PWD}/OAIScoreDetail.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISubscriber.cpp \
    $${PWD}/OAISummary.cpp \
    $${PWD}/OAITable.cpp \
    $${PWD}/OAITableCell.cpp \
    $${PWD}/OAITableRow.cpp \
    $${PWD}/OAIUpdateAPIKeyInput.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIVehicleSummary.cpp \
    $${PWD}/OAIWrongInput.cpp \
# APIs
    $${PWD}/OAIBehaviorApi.cpp \
    $${PWD}/OAIChecksApi.cpp \
    $${PWD}/OAIContinuousApi.cpp \
    $${PWD}/OAICustomTypeApi.cpp \
    $${PWD}/OAIHooksApi.cpp \
    $${PWD}/OAIPdfApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
