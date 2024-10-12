QT += network

HEADERS += \
# Models
    $${PWD}/OAIGET_user_content_by_date_json_200_response.h \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_debug.h \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_results.h \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_results_comments_inner.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_all_properties_inner.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_properties.h \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_properties_automoderation_on.h \
    $${PWD}/OAIGET_user_content_url_json_200_response.h \
    $${PWD}/OAIGET_user_content_url_json_200_response_results.h \
    $${PWD}/OAIGET_user_content_url_json_200_response_results_comments_inner.h \
    $${PWD}/OAIGET_user_content_user_json_200_response.h \
    $${PWD}/OAIGET_user_content_user_json_200_response_results.h \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner.h \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset.h \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset_labels_inner.h \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset_properties.h \
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
    $${PWD}/OAIGET_user_content_by_date_json_200_response.cpp \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_debug.cpp \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_results.cpp \
    $${PWD}/OAIGET_user_content_by_date_json_200_response_results_comments_inner.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_all_properties_inner.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_properties.cpp \
    $${PWD}/OAIGET_user_content_recent_json_200_response_results_comments_inner_asset_properties_automoderation_on.cpp \
    $${PWD}/OAIGET_user_content_url_json_200_response.cpp \
    $${PWD}/OAIGET_user_content_url_json_200_response_results.cpp \
    $${PWD}/OAIGET_user_content_url_json_200_response_results_comments_inner.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response_results.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset_labels_inner.cpp \
    $${PWD}/OAIGET_user_content_user_json_200_response_results_comments_inner_asset_properties.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
