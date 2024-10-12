QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIActivity.h \
    $${PWD}/OAIAdminAccount.h \
    $${PWD}/OAIAdminReport.h \
    $${PWD}/OAIAnnouncement.h \
    $${PWD}/OAIAnnouncementReaction.h \
    $${PWD}/OAIApplication.h \
    $${PWD}/OAIAttachment.h \
    $${PWD}/OAICard.h \
    $${PWD}/OAIContext.h \
    $${PWD}/OAIConversation.h \
    $${PWD}/OAIEmoji.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFeaturedTag.h \
    $${PWD}/OAIField.h \
    $${PWD}/OAIFilter.h \
    $${PWD}/OAIHistory.h \
    $${PWD}/OAIIdentityProof.h \
    $${PWD}/OAIInstance.h \
    $${PWD}/OAIList.h \
    $${PWD}/OAIMarker.h \
    $${PWD}/OAIMention.h \
    $${PWD}/OAINotification.h \
    $${PWD}/OAIPoll.h \
    $${PWD}/OAIPreferences.h \
    $${PWD}/OAIPushSubscription.h \
    $${PWD}/OAIRelationship.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIResults.h \
    $${PWD}/OAIScheduledStatus.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIStatusParams.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAIToken.h \
    $${PWD}/OAI_api_v1_accounts__id__follow_post_request.h \
    $${PWD}/OAI_api_v1_accounts__id__mute_post_request.h \
    $${PWD}/OAI_api_v1_accounts__id__note_post_request.h \
    $${PWD}/OAI_api_v1_accounts_post_request.h \
    $${PWD}/OAI_api_v1_accounts_update_credentials_patch_request.h \
    $${PWD}/OAI_api_v1_accounts_update_credentials_patch_request_source.h \
    $${PWD}/OAI_api_v1_admin_accounts__id__action_post_request.h \
    $${PWD}/OAI_api_v1_apps_post_200_response.h \
    $${PWD}/OAI_api_v1_apps_post_request.h \
    $${PWD}/OAI_api_v1_domain_blocks_post_request.h \
    $${PWD}/OAI_api_v1_featured_tags_post_request.h \
    $${PWD}/OAI_api_v1_filters_post_request.h \
    $${PWD}/OAI_api_v1_lists__id__accounts_post_request.h \
    $${PWD}/OAI_api_v1_lists_post_request.h \
    $${PWD}/OAI_api_v1_lists_put_request.h \
    $${PWD}/OAI_api_v1_media_post_request.h \
    $${PWD}/OAI_api_v1_polls__id__post_request.h \
    $${PWD}/OAI_api_v1_push_subscription_post_request.h \
    $${PWD}/OAI_api_v1_push_subscription_put_request.h \
    $${PWD}/OAI_api_v1_reports_post_request.h \
    $${PWD}/OAI_api_v1_scheduled_statuses__id__put_request.h \
    $${PWD}/OAI_api_v1_statuses__id__reblog_post_request.h \
    $${PWD}/OAI_api_v1_statuses_post_200_response.h \
    $${PWD}/OAI_api_v1_statuses_post_request_inner.h \
    $${PWD}/OAI_api_v2_search_get_200_response.h \
    $${PWD}/OAI_oauth_revoke_post_request.h \
    $${PWD}/OAI_oauth_token_post_200_response.h \
    $${PWD}/OAI_oauth_token_post_request.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAIAppsApi.h \
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIOauthApi.h \
    $${PWD}/OAITODOSecurityApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIActivity.cpp \
    $${PWD}/OAIAdminAccount.cpp \
    $${PWD}/OAIAdminReport.cpp \
    $${PWD}/OAIAnnouncement.cpp \
    $${PWD}/OAIAnnouncementReaction.cpp \
    $${PWD}/OAIApplication.cpp \
    $${PWD}/OAIAttachment.cpp \
    $${PWD}/OAICard.cpp \
    $${PWD}/OAIContext.cpp \
    $${PWD}/OAIConversation.cpp \
    $${PWD}/OAIEmoji.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFeaturedTag.cpp \
    $${PWD}/OAIField.cpp \
    $${PWD}/OAIFilter.cpp \
    $${PWD}/OAIHistory.cpp \
    $${PWD}/OAIIdentityProof.cpp \
    $${PWD}/OAIInstance.cpp \
    $${PWD}/OAIList.cpp \
    $${PWD}/OAIMarker.cpp \
    $${PWD}/OAIMention.cpp \
    $${PWD}/OAINotification.cpp \
    $${PWD}/OAIPoll.cpp \
    $${PWD}/OAIPreferences.cpp \
    $${PWD}/OAIPushSubscription.cpp \
    $${PWD}/OAIRelationship.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIResults.cpp \
    $${PWD}/OAIScheduledStatus.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIStatusParams.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAIToken.cpp \
    $${PWD}/OAI_api_v1_accounts__id__follow_post_request.cpp \
    $${PWD}/OAI_api_v1_accounts__id__mute_post_request.cpp \
    $${PWD}/OAI_api_v1_accounts__id__note_post_request.cpp \
    $${PWD}/OAI_api_v1_accounts_post_request.cpp \
    $${PWD}/OAI_api_v1_accounts_update_credentials_patch_request.cpp \
    $${PWD}/OAI_api_v1_accounts_update_credentials_patch_request_source.cpp \
    $${PWD}/OAI_api_v1_admin_accounts__id__action_post_request.cpp \
    $${PWD}/OAI_api_v1_apps_post_200_response.cpp \
    $${PWD}/OAI_api_v1_apps_post_request.cpp \
    $${PWD}/OAI_api_v1_domain_blocks_post_request.cpp \
    $${PWD}/OAI_api_v1_featured_tags_post_request.cpp \
    $${PWD}/OAI_api_v1_filters_post_request.cpp \
    $${PWD}/OAI_api_v1_lists__id__accounts_post_request.cpp \
    $${PWD}/OAI_api_v1_lists_post_request.cpp \
    $${PWD}/OAI_api_v1_lists_put_request.cpp \
    $${PWD}/OAI_api_v1_media_post_request.cpp \
    $${PWD}/OAI_api_v1_polls__id__post_request.cpp \
    $${PWD}/OAI_api_v1_push_subscription_post_request.cpp \
    $${PWD}/OAI_api_v1_push_subscription_put_request.cpp \
    $${PWD}/OAI_api_v1_reports_post_request.cpp \
    $${PWD}/OAI_api_v1_scheduled_statuses__id__put_request.cpp \
    $${PWD}/OAI_api_v1_statuses__id__reblog_post_request.cpp \
    $${PWD}/OAI_api_v1_statuses_post_200_response.cpp \
    $${PWD}/OAI_api_v1_statuses_post_request_inner.cpp \
    $${PWD}/OAI_api_v2_search_get_200_response.cpp \
    $${PWD}/OAI_oauth_revoke_post_request.cpp \
    $${PWD}/OAI_oauth_token_post_200_response.cpp \
    $${PWD}/OAI_oauth_token_post_request.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAIAppsApi.cpp \
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIOauthApi.cpp \
    $${PWD}/OAITODOSecurityApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
