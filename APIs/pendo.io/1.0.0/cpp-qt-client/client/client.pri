QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountWithTags.h \
    $${PWD}/OAIComment.h \
    $${PWD}/OAIEndUserPing.h \
    $${PWD}/OAIEndUserPing_user.h \
    $${PWD}/OAIFeature.h \
    $${PWD}/OAIFeatureVote.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUserAccount.h \
    $${PWD}/OAIVote.h \
    $${PWD}/OAI_accounts__id__put_request.h \
    $${PWD}/OAI_hooks_post_request.h \
    $${PWD}/OAI_hooks_unsubscribe_post_request.h \
    $${PWD}/OAI_users__id__put_request.h \
    $${PWD}/OAI_users_invite_end_user_post_request.h \
    $${PWD}/OAI_users_invite_vendor_user_post_request.h \
    $${PWD}/OAI_vendor_users_post_request.h \
    $${PWD}/OAI_votes_post_request.h \
# APIs
    $${PWD}/OAIAccountApi.h \
    $${PWD}/OAICommentApi.h \
    $${PWD}/OAIFeatureApi.h \
    $${PWD}/OAIHooksApi.h \
    $${PWD}/OAISystemApi.h \
    $${PWD}/OAITeamApi.h \
    $${PWD}/OAIUserApi.h \
    $${PWD}/OAIVotesApi.h \
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
    $${PWD}/OAIAccountWithTags.cpp \
    $${PWD}/OAIComment.cpp \
    $${PWD}/OAIEndUserPing.cpp \
    $${PWD}/OAIEndUserPing_user.cpp \
    $${PWD}/OAIFeature.cpp \
    $${PWD}/OAIFeatureVote.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUserAccount.cpp \
    $${PWD}/OAIVote.cpp \
    $${PWD}/OAI_accounts__id__put_request.cpp \
    $${PWD}/OAI_hooks_post_request.cpp \
    $${PWD}/OAI_hooks_unsubscribe_post_request.cpp \
    $${PWD}/OAI_users__id__put_request.cpp \
    $${PWD}/OAI_users_invite_end_user_post_request.cpp \
    $${PWD}/OAI_users_invite_vendor_user_post_request.cpp \
    $${PWD}/OAI_vendor_users_post_request.cpp \
    $${PWD}/OAI_votes_post_request.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
    $${PWD}/OAICommentApi.cpp \
    $${PWD}/OAIFeatureApi.cpp \
    $${PWD}/OAIHooksApi.cpp \
    $${PWD}/OAISystemApi.cpp \
    $${PWD}/OAITeamApi.cpp \
    $${PWD}/OAIUserApi.cpp \
    $${PWD}/OAIVotesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
