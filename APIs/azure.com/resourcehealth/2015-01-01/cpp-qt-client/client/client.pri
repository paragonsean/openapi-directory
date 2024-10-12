QT += network

HEADERS += \
# Models
    $${PWD}/OAIAvailabilityStatus.h \
    $${PWD}/OAIAvailabilityStatusListResult.h \
    $${PWD}/OAIAvailabilityStatus_properties.h \
    $${PWD}/OAIAvailabilityStatus_properties_recentlyResolvedState.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIRecommendedAction.h \
    $${PWD}/OAIServiceImpactingEvent.h \
    $${PWD}/OAIServiceImpactingEvent_incidentProperties.h \
    $${PWD}/OAIServiceImpactingEvent_status.h \
# APIs
    $${PWD}/OAIAvailabilityStatusesApi.h \
    $${PWD}/OAIChildAvailabilityStatusesApi.h \
    $${PWD}/OAIChildResourcesApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIRecommendedAction.cpp \
    $${PWD}/OAIServiceImpactingEvent.cpp \
    $${PWD}/OAIServiceImpactingEvent_incidentProperties.cpp \
    $${PWD}/OAIServiceImpactingEvent_status.cpp \
# APIs
    $${PWD}/OAIAvailabilityStatusesApi.cpp \
    $${PWD}/OAIChildAvailabilityStatusesApi.cpp \
    $${PWD}/OAIChildResourcesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
