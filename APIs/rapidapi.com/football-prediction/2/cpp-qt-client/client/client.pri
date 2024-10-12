QT += network

HEADERS += \
# Models
    $${PWD}/OAI_api_v2_list_federations_get_200_response.h \
    $${PWD}/OAI_api_v2_list_federations_get_404_response.h \
    $${PWD}/OAI_api_v2_list_federations_get_404_response_errors_inner.h \
    $${PWD}/OAI_api_v2_list_markets_get_200_response.h \
    $${PWD}/OAI_api_v2_list_markets_get_200_response_data.h \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response.h \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data.h \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_accuracy.h \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_details.h \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days.h \
    $${PWD}/OAI_api_v2_predictions__id__get_200_response.h \
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
    $${PWD}/OAI_api_v2_list_federations_get_200_response.cpp \
    $${PWD}/OAI_api_v2_list_federations_get_404_response.cpp \
    $${PWD}/OAI_api_v2_list_federations_get_404_response_errors_inner.cpp \
    $${PWD}/OAI_api_v2_list_markets_get_200_response.cpp \
    $${PWD}/OAI_api_v2_list_markets_get_200_response_data.cpp \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response.cpp \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data.cpp \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_accuracy.cpp \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_details.cpp \
    $${PWD}/OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days.cpp \
    $${PWD}/OAI_api_v2_predictions__id__get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
