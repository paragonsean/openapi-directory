QT += network

HEADERS += \
# Models
    $${PWD}/OAIComplianceDetails.h \
    $${PWD}/OAIDescribeReportCreationOutput.h \
    $${PWD}/OAIErrorCode.h \
    $${PWD}/OAIFailureInfo.h \
    $${PWD}/OAIGetComplianceSummaryInput.h \
    $${PWD}/OAIGetComplianceSummaryOutput.h \
    $${PWD}/OAIGetResourcesInput.h \
    $${PWD}/OAIGetResourcesOutput.h \
    $${PWD}/OAIGetTagKeysInput.h \
    $${PWD}/OAIGetTagKeysOutput.h \
    $${PWD}/OAIGetTagValuesInput.h \
    $${PWD}/OAIGetTagValuesOutput.h \
    $${PWD}/OAIGroupByAttribute.h \
    $${PWD}/OAIResourceTagMapping.h \
    $${PWD}/OAIResourceTagMapping_ComplianceDetails.h \
    $${PWD}/OAIStartReportCreationInput.h \
    $${PWD}/OAISummary.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAITagFilter.h \
    $${PWD}/OAITagResourcesInput.h \
    $${PWD}/OAITagResourcesOutput.h \
    $${PWD}/OAITargetIdType.h \
    $${PWD}/OAIUntagResourcesInput.h \
    $${PWD}/OAIUntagResourcesOutput.h \
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
    $${PWD}/OAIComplianceDetails.cpp \
    $${PWD}/OAIDescribeReportCreationOutput.cpp \
    $${PWD}/OAIErrorCode.cpp \
    $${PWD}/OAIFailureInfo.cpp \
    $${PWD}/OAIGetComplianceSummaryInput.cpp \
    $${PWD}/OAIGetComplianceSummaryOutput.cpp \
    $${PWD}/OAIGetResourcesInput.cpp \
    $${PWD}/OAIGetResourcesOutput.cpp \
    $${PWD}/OAIGetTagKeysInput.cpp \
    $${PWD}/OAIGetTagKeysOutput.cpp \
    $${PWD}/OAIGetTagValuesInput.cpp \
    $${PWD}/OAIGetTagValuesOutput.cpp \
    $${PWD}/OAIGroupByAttribute.cpp \
    $${PWD}/OAIResourceTagMapping.cpp \
    $${PWD}/OAIResourceTagMapping_ComplianceDetails.cpp \
    $${PWD}/OAIStartReportCreationInput.cpp \
    $${PWD}/OAISummary.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAITagFilter.cpp \
    $${PWD}/OAITagResourcesInput.cpp \
    $${PWD}/OAITagResourcesOutput.cpp \
    $${PWD}/OAITargetIdType.cpp \
    $${PWD}/OAIUntagResourcesInput.cpp \
    $${PWD}/OAIUntagResourcesOutput.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
