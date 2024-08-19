QT += network

HEADERS += \
# Models
    $${PWD}/OAIFeedback.h \
    $${PWD}/OAIGet_all_posts_200_response.h \
    $${PWD}/OAIGet_all_posts_changes_200_response.h \
    $${PWD}/OAIGet_all_posts_changes_200_response_changes_inner.h \
    $${PWD}/OAIGet_post_and_related_data_200_response.h \
    $${PWD}/OAIGet_posts_200_response.h \
    $${PWD}/OAIGet_posts_by_ids_200_response.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIGroup_country.h \
    $${PWD}/OAIGroup_membership.h \
    $${PWD}/OAIGroup_membership_questionnaire.h \
    $${PWD}/OAIGroup_region.h \
    $${PWD}/OAIPhoto.h \
    $${PWD}/OAIPhoto_images_inner.h \
    $${PWD}/OAIPost.h \
    $${PWD}/OAIPostSearchResult.h \
    $${PWD}/OAISearch_groups_200_response.h \
    $${PWD}/OAISearch_posts_200_response.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUser_feedback.h \
# APIs
    $${PWD}/OAIGroupsApi.h \
    $${PWD}/OAIPostsApi.h \
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIFeedback.cpp \
    $${PWD}/OAIGet_all_posts_200_response.cpp \
    $${PWD}/OAIGet_all_posts_changes_200_response.cpp \
    $${PWD}/OAIGet_all_posts_changes_200_response_changes_inner.cpp \
    $${PWD}/OAIGet_post_and_related_data_200_response.cpp \
    $${PWD}/OAIGet_posts_200_response.cpp \
    $${PWD}/OAIGet_posts_by_ids_200_response.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIGroup_country.cpp \
    $${PWD}/OAIGroup_membership.cpp \
    $${PWD}/OAIGroup_membership_questionnaire.cpp \
    $${PWD}/OAIGroup_region.cpp \
    $${PWD}/OAIPhoto.cpp \
    $${PWD}/OAIPhoto_images_inner.cpp \
    $${PWD}/OAIPost.cpp \
    $${PWD}/OAIPostSearchResult.cpp \
    $${PWD}/OAISearch_groups_200_response.cpp \
    $${PWD}/OAISearch_posts_200_response.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUser_feedback.cpp \
# APIs
    $${PWD}/OAIGroupsApi.cpp \
    $${PWD}/OAIPostsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
