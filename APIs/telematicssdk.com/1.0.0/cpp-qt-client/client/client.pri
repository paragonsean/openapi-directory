QT += network

HEADERS += \
# Models
    $${PWD}/OAITripsTripDetails_200_response.h \
    $${PWD}/OAITripsTripDetails_200_response_Result.h \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track.h \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track_AddressFinishParts.h \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track_Points_inner.h \
    $${PWD}/OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response.h \
    $${PWD}/OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result.h \
    $${PWD}/OAIUserSafeScoringDailyValue_v1_scorings_individual_daily_200_response.h \
    $${PWD}/OAIUserSafeScoringDailyValue_v1_scorings_individual_daily_200_response_Result_inner.h \
    $${PWD}/OAIUserStatisticeDailyValueV1_statistics_individual_daily_200_response.h \
    $${PWD}/OAIUserStatisticeDailyValueV1_statistics_individual_daily_200_response_Result_inner.h \
    $${PWD}/OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response.h \
    $${PWD}/OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response_Result.h \
    $${PWD}/OAI_v1_scorings_consolidated_daily_200_response.h \
    $${PWD}/OAI_v1_scorings_consolidated_daily_200_response_Result_inner.h \
# APIs
    $${PWD}/OAIClass21UserStatisticsOptionalApi.h \
    $${PWD}/OAIClass22UserTripsOptionalApi.h \
    $${PWD}/OAIClass24UserSafeScoringOptionalApi.h \
    $${PWD}/OAIClass2ForMobileAppOptionalApi.h \
    $${PWD}/OAIClass3ForBackEndOptionalApi.h \
    $${PWD}/OAIConsolidatedSafeScoringApi.h \
    $${PWD}/OAIConsolidatedStatisticsApi.h \
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
    $${PWD}/OAITripsTripDetails_200_response.cpp \
    $${PWD}/OAITripsTripDetails_200_response_Result.cpp \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track.cpp \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track_AddressFinishParts.cpp \
    $${PWD}/OAITripsTripDetails_200_response_Result_Track_Points_inner.cpp \
    $${PWD}/OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response.cpp \
    $${PWD}/OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result.cpp \
    $${PWD}/OAIUserSafeScoringDailyValue_v1_scorings_individual_daily_200_response.cpp \
    $${PWD}/OAIUserSafeScoringDailyValue_v1_scorings_individual_daily_200_response_Result_inner.cpp \
    $${PWD}/OAIUserStatisticeDailyValueV1_statistics_individual_daily_200_response.cpp \
    $${PWD}/OAIUserStatisticeDailyValueV1_statistics_individual_daily_200_response_Result_inner.cpp \
    $${PWD}/OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response.cpp \
    $${PWD}/OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response_Result.cpp \
    $${PWD}/OAI_v1_scorings_consolidated_daily_200_response.cpp \
    $${PWD}/OAI_v1_scorings_consolidated_daily_200_response_Result_inner.cpp \
# APIs
    $${PWD}/OAIClass21UserStatisticsOptionalApi.cpp \
    $${PWD}/OAIClass22UserTripsOptionalApi.cpp \
    $${PWD}/OAIClass24UserSafeScoringOptionalApi.cpp \
    $${PWD}/OAIClass2ForMobileAppOptionalApi.cpp \
    $${PWD}/OAIClass3ForBackEndOptionalApi.cpp \
    $${PWD}/OAIConsolidatedSafeScoringApi.cpp \
    $${PWD}/OAIConsolidatedStatisticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
