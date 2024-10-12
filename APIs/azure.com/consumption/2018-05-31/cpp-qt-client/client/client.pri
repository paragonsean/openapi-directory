QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIForecast.h \
    $${PWD}/OAIForecastProperties.h \
    $${PWD}/OAIForecastProperties_confidenceLevels_inner.h \
    $${PWD}/OAIForecastsListResult.h \
    $${PWD}/OAIMeterDetails.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIPriceSheetModel.h \
    $${PWD}/OAIPriceSheetProperties.h \
    $${PWD}/OAIPriceSheetResult.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIUsageDetail.h \
    $${PWD}/OAIUsageDetailProperties.h \
    $${PWD}/OAIUsageDetailsListResult.h \
# APIs
    $${PWD}/OAIForecastsApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIPriceSheetApi.h \
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
    $${PWD}/OAIForecast.cpp \
    $${PWD}/OAIForecastProperties.cpp \
    $${PWD}/OAIForecastProperties_confidenceLevels_inner.cpp \
    $${PWD}/OAIForecastsListResult.cpp \
    $${PWD}/OAIMeterDetails.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIPriceSheetModel.cpp \
    $${PWD}/OAIPriceSheetProperties.cpp \
    $${PWD}/OAIPriceSheetResult.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIUsageDetail.cpp \
    $${PWD}/OAIUsageDetailProperties.cpp \
    $${PWD}/OAIUsageDetailsListResult.cpp \
# APIs
    $${PWD}/OAIForecastsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIPriceSheetApi.cpp \
    $${PWD}/OAIUsageDetailsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
