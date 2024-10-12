QT += network

HEADERS += \
# Models
    $${PWD}/OAI_check_get_200_response.h \
    $${PWD}/OAI_check_get_default_response.h \
    $${PWD}/OAI_news_get_200_response.h \
    $${PWD}/OAI_news_get_200_response_br.h \
    $${PWD}/OAI_news_get_200_response_common.h \
    $${PWD}/OAI_oauth_token_post_200_response.h \
    $${PWD}/OAI_oauth_token_post_401_response.h \
    $${PWD}/OAI_oauth_token_post_request.h \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response.h \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_group.h \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_group_duo.h \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_info.h \
    $${PWD}/OAI_user__plateform___username__get_200_response.h \
# APIs
    $${PWD}/OAICheckApi.h \
    $${PWD}/OAINewsApi.h \
    $${PWD}/OAIPVEApi.h \
    $${PWD}/OAISecurityApi.h \
    $${PWD}/OAIStatsApi.h \
    $${PWD}/OAIStoreApi.h \
    $${PWD}/OAIUserApi.h \
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
    $${PWD}/OAI_check_get_200_response.cpp \
    $${PWD}/OAI_check_get_default_response.cpp \
    $${PWD}/OAI_news_get_200_response.cpp \
    $${PWD}/OAI_news_get_200_response_br.cpp \
    $${PWD}/OAI_news_get_200_response_common.cpp \
    $${PWD}/OAI_oauth_token_post_200_response.cpp \
    $${PWD}/OAI_oauth_token_post_401_response.cpp \
    $${PWD}/OAI_oauth_token_post_request.cpp \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response.cpp \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_group.cpp \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_group_duo.cpp \
    $${PWD}/OAI_stats_id__plateform___id__get_200_response_info.cpp \
    $${PWD}/OAI_user__plateform___username__get_200_response.cpp \
# APIs
    $${PWD}/OAICheckApi.cpp \
    $${PWD}/OAINewsApi.cpp \
    $${PWD}/OAIPVEApi.cpp \
    $${PWD}/OAISecurityApi.cpp \
    $${PWD}/OAIStatsApi.cpp \
    $${PWD}/OAIStoreApi.cpp \
    $${PWD}/OAIUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
