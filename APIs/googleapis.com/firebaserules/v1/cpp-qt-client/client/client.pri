QT += network

HEADERS += \
# Models
    $${PWD}/OAIArg.h \
    $${PWD}/OAIExpressionReport.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIFunctionCall.h \
    $${PWD}/OAIFunctionMock.h \
    $${PWD}/OAIGetReleaseExecutableResponse.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIListReleasesResponse.h \
    $${PWD}/OAIListRulesetsResponse.h \
    $${PWD}/OAIMetadata.h \
    $${PWD}/OAIRelease.h \
    $${PWD}/OAIResult.h \
    $${PWD}/OAIRuleset.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAISourcePosition.h \
    $${PWD}/OAITestCase.h \
    $${PWD}/OAITestResult.h \
    $${PWD}/OAITestRulesetRequest.h \
    $${PWD}/OAITestRulesetResponse.h \
    $${PWD}/OAITestSuite.h \
    $${PWD}/OAIUpdateReleaseRequest.h \
    $${PWD}/OAIValueCount.h \
    $${PWD}/OAIVisitedExpression.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIArg.cpp \
    $${PWD}/OAIExpressionReport.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIFunctionCall.cpp \
    $${PWD}/OAIFunctionMock.cpp \
    $${PWD}/OAIGetReleaseExecutableResponse.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIListReleasesResponse.cpp \
    $${PWD}/OAIListRulesetsResponse.cpp \
    $${PWD}/OAIMetadata.cpp \
    $${PWD}/OAIRelease.cpp \
    $${PWD}/OAIResult.cpp \
    $${PWD}/OAIRuleset.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAISourcePosition.cpp \
    $${PWD}/OAITestCase.cpp \
    $${PWD}/OAITestResult.cpp \
    $${PWD}/OAITestRulesetRequest.cpp \
    $${PWD}/OAITestRulesetResponse.cpp \
    $${PWD}/OAITestSuite.cpp \
    $${PWD}/OAIUpdateReleaseRequest.cpp \
    $${PWD}/OAIValueCount.cpp \
    $${PWD}/OAIVisitedExpression.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
