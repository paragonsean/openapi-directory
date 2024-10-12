QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIMeterDetails.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIReservationDetails.h \
    $${PWD}/OAIReservationDetailsListResult.h \
    $${PWD}/OAIReservationDetailsProperties.h \
    $${PWD}/OAIReservationSummaries.h \
    $${PWD}/OAIReservationSummariesListResult.h \
    $${PWD}/OAIReservationSummariesProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIUsageDetail.h \
    $${PWD}/OAIUsageDetailProperties.h \
    $${PWD}/OAIUsageDetailsListResult.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIReservedInstancesApi.h \
    $${PWD}/OAIUsageDetailsApi.h \
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
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIMeterDetails.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIReservationDetails.cpp \
    $${PWD}/OAIReservationDetailsListResult.cpp \
    $${PWD}/OAIReservationDetailsProperties.cpp \
    $${PWD}/OAIReservationSummaries.cpp \
    $${PWD}/OAIReservationSummariesListResult.cpp \
    $${PWD}/OAIReservationSummariesProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIUsageDetail.cpp \
    $${PWD}/OAIUsageDetailProperties.cpp \
    $${PWD}/OAIUsageDetailsListResult.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIReservedInstancesApi.cpp \
    $${PWD}/OAIUsageDetailsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
