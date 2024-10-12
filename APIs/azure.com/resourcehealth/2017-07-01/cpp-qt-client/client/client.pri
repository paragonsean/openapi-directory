QT += network

HEADERS += \
# Models
    $${PWD}/OAIAvailabilityStatus.h \
    $${PWD}/OAIAvailabilityStatusListResult.h \
    $${PWD}/OAIAvailabilityStatus_properties.h \
    $${PWD}/OAIAvailabilityStatus_properties_recentlyResolvedState.h \
    $${PWD}/OAIEmergingIssue.h \
    $${PWD}/OAIEmergingIssueImpact.h \
    $${PWD}/OAIEmergingIssueListResult.h \
    $${PWD}/OAIEmergingIssuesGetResult.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIImpactedRegion.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIRecommendedAction.h \
    $${PWD}/OAIServiceImpactingEvent.h \
    $${PWD}/OAIServiceImpactingEvent_incidentProperties.h \
    $${PWD}/OAIServiceImpactingEvent_status.h \
    $${PWD}/OAIStatusActiveEvent.h \
    $${PWD}/OAIStatusBanner.h \
# APIs
    $${PWD}/OAIAvailabilityStatusesApi.h \
    $${PWD}/OAIChildAvailabilityStatusesApi.h \
    $${PWD}/OAIChildResourcesApi.h \
    $${PWD}/OAIEmergingIssuesApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIAvailabilityStatus.cpp \
    $${PWD}/OAIAvailabilityStatusListResult.cpp \
    $${PWD}/OAIAvailabilityStatus_properties.cpp \
    $${PWD}/OAIAvailabilityStatus_properties_recentlyResolvedState.cpp \
    $${PWD}/OAIEmergingIssue.cpp \
    $${PWD}/OAIEmergingIssueImpact.cpp \
    $${PWD}/OAIEmergingIssueListResult.cpp \
    $${PWD}/OAIEmergingIssuesGetResult.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIImpactedRegion.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIRecommendedAction.cpp \
    $${PWD}/OAIServiceImpactingEvent.cpp \
    $${PWD}/OAIServiceImpactingEvent_incidentProperties.cpp \
    $${PWD}/OAIServiceImpactingEvent_status.cpp \
    $${PWD}/OAIStatusActiveEvent.cpp \
    $${PWD}/OAIStatusBanner.cpp \
# APIs
    $${PWD}/OAIAvailabilityStatusesApi.cpp \
    $${PWD}/OAIChildAvailabilityStatusesApi.cpp \
    $${PWD}/OAIChildResourcesApi.cpp \
    $${PWD}/OAIEmergingIssuesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
