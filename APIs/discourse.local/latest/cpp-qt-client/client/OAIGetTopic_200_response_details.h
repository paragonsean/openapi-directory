/**
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetTopic_200_response_details.h
 *
 * 
 */

#ifndef OAIGetTopic_200_response_details_H
#define OAIGetTopic_200_response_details_H

#include <QJsonObject>

#include "OAIAdminGetUser_200_response_approved_by.h"
#include "OAIGetTopic_200_response_details_participants_inner.h"
#include <QJsonValue>
#include <QList>
#include <QMap>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetTopic_200_response_details : public OAIObject {
public:
    OAIGetTopic_200_response_details();
    OAIGetTopic_200_response_details(QString json);
    ~OAIGetTopic_200_response_details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCanArchiveTopic() const;
    void setCanArchiveTopic(const bool &can_archive_topic);
    bool is_can_archive_topic_Set() const;
    bool is_can_archive_topic_Valid() const;

    bool isCanCloseTopic() const;
    void setCanCloseTopic(const bool &can_close_topic);
    bool is_can_close_topic_Set() const;
    bool is_can_close_topic_Valid() const;

    bool isCanConvertTopic() const;
    void setCanConvertTopic(const bool &can_convert_topic);
    bool is_can_convert_topic_Set() const;
    bool is_can_convert_topic_Valid() const;

    bool isCanCreatePost() const;
    void setCanCreatePost(const bool &can_create_post);
    bool is_can_create_post_Set() const;
    bool is_can_create_post_Valid() const;

    bool isCanDelete() const;
    void setCanDelete(const bool &can_delete);
    bool is_can_delete_Set() const;
    bool is_can_delete_Valid() const;

    bool isCanEdit() const;
    void setCanEdit(const bool &can_edit);
    bool is_can_edit_Set() const;
    bool is_can_edit_Valid() const;

    bool isCanEditStaffNotes() const;
    void setCanEditStaffNotes(const bool &can_edit_staff_notes);
    bool is_can_edit_staff_notes_Set() const;
    bool is_can_edit_staff_notes_Valid() const;

    bool isCanFlagTopic() const;
    void setCanFlagTopic(const bool &can_flag_topic);
    bool is_can_flag_topic_Set() const;
    bool is_can_flag_topic_Valid() const;

    bool isCanInviteTo() const;
    void setCanInviteTo(const bool &can_invite_to);
    bool is_can_invite_to_Set() const;
    bool is_can_invite_to_Valid() const;

    bool isCanInviteViaEmail() const;
    void setCanInviteViaEmail(const bool &can_invite_via_email);
    bool is_can_invite_via_email_Set() const;
    bool is_can_invite_via_email_Valid() const;

    bool isCanModerateCategory() const;
    void setCanModerateCategory(const bool &can_moderate_category);
    bool is_can_moderate_category_Set() const;
    bool is_can_moderate_category_Valid() const;

    bool isCanMovePosts() const;
    void setCanMovePosts(const bool &can_move_posts);
    bool is_can_move_posts_Set() const;
    bool is_can_move_posts_Valid() const;

    bool isCanPinUnpinTopic() const;
    void setCanPinUnpinTopic(const bool &can_pin_unpin_topic);
    bool is_can_pin_unpin_topic_Set() const;
    bool is_can_pin_unpin_topic_Valid() const;

    bool isCanRemoveAllowedUsers() const;
    void setCanRemoveAllowedUsers(const bool &can_remove_allowed_users);
    bool is_can_remove_allowed_users_Set() const;
    bool is_can_remove_allowed_users_Valid() const;

    qint32 getCanRemoveSelfId() const;
    void setCanRemoveSelfId(const qint32 &can_remove_self_id);
    bool is_can_remove_self_id_Set() const;
    bool is_can_remove_self_id_Valid() const;

    bool isCanReplyAsNewTopic() const;
    void setCanReplyAsNewTopic(const bool &can_reply_as_new_topic);
    bool is_can_reply_as_new_topic_Set() const;
    bool is_can_reply_as_new_topic_Valid() const;

    bool isCanReviewTopic() const;
    void setCanReviewTopic(const bool &can_review_topic);
    bool is_can_review_topic_Set() const;
    bool is_can_review_topic_Valid() const;

    bool isCanSplitMergeTopic() const;
    void setCanSplitMergeTopic(const bool &can_split_merge_topic);
    bool is_can_split_merge_topic_Set() const;
    bool is_can_split_merge_topic_Valid() const;

    bool isCanToggleTopicVisibility() const;
    void setCanToggleTopicVisibility(const bool &can_toggle_topic_visibility);
    bool is_can_toggle_topic_visibility_Set() const;
    bool is_can_toggle_topic_visibility_Valid() const;

    OAIAdminGetUser_200_response_approved_by getCreatedBy() const;
    void setCreatedBy(const OAIAdminGetUser_200_response_approved_by &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    OAIAdminGetUser_200_response_approved_by getLastPoster() const;
    void setLastPoster(const OAIAdminGetUser_200_response_approved_by &last_poster);
    bool is_last_poster_Set() const;
    bool is_last_poster_Valid() const;

    qint32 getNotificationLevel() const;
    void setNotificationLevel(const qint32 &notification_level);
    bool is_notification_level_Set() const;
    bool is_notification_level_Valid() const;

    QList<OAIGetTopic_200_response_details_participants_inner> getParticipants() const;
    void setParticipants(const QList<OAIGetTopic_200_response_details_participants_inner> &participants);
    bool is_participants_Set() const;
    bool is_participants_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_can_archive_topic;
    bool m_can_archive_topic_isSet;
    bool m_can_archive_topic_isValid;

    bool m_can_close_topic;
    bool m_can_close_topic_isSet;
    bool m_can_close_topic_isValid;

    bool m_can_convert_topic;
    bool m_can_convert_topic_isSet;
    bool m_can_convert_topic_isValid;

    bool m_can_create_post;
    bool m_can_create_post_isSet;
    bool m_can_create_post_isValid;

    bool m_can_delete;
    bool m_can_delete_isSet;
    bool m_can_delete_isValid;

    bool m_can_edit;
    bool m_can_edit_isSet;
    bool m_can_edit_isValid;

    bool m_can_edit_staff_notes;
    bool m_can_edit_staff_notes_isSet;
    bool m_can_edit_staff_notes_isValid;

    bool m_can_flag_topic;
    bool m_can_flag_topic_isSet;
    bool m_can_flag_topic_isValid;

    bool m_can_invite_to;
    bool m_can_invite_to_isSet;
    bool m_can_invite_to_isValid;

    bool m_can_invite_via_email;
    bool m_can_invite_via_email_isSet;
    bool m_can_invite_via_email_isValid;

    bool m_can_moderate_category;
    bool m_can_moderate_category_isSet;
    bool m_can_moderate_category_isValid;

    bool m_can_move_posts;
    bool m_can_move_posts_isSet;
    bool m_can_move_posts_isValid;

    bool m_can_pin_unpin_topic;
    bool m_can_pin_unpin_topic_isSet;
    bool m_can_pin_unpin_topic_isValid;

    bool m_can_remove_allowed_users;
    bool m_can_remove_allowed_users_isSet;
    bool m_can_remove_allowed_users_isValid;

    qint32 m_can_remove_self_id;
    bool m_can_remove_self_id_isSet;
    bool m_can_remove_self_id_isValid;

    bool m_can_reply_as_new_topic;
    bool m_can_reply_as_new_topic_isSet;
    bool m_can_reply_as_new_topic_isValid;

    bool m_can_review_topic;
    bool m_can_review_topic_isSet;
    bool m_can_review_topic_isValid;

    bool m_can_split_merge_topic;
    bool m_can_split_merge_topic_isSet;
    bool m_can_split_merge_topic_isValid;

    bool m_can_toggle_topic_visibility;
    bool m_can_toggle_topic_visibility_isSet;
    bool m_can_toggle_topic_visibility_isValid;

    OAIAdminGetUser_200_response_approved_by m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    OAIAdminGetUser_200_response_approved_by m_last_poster;
    bool m_last_poster_isSet;
    bool m_last_poster_isValid;

    qint32 m_notification_level;
    bool m_notification_level_isSet;
    bool m_notification_level_isValid;

    QList<OAIGetTopic_200_response_details_participants_inner> m_participants;
    bool m_participants_isSet;
    bool m_participants_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTopic_200_response_details)

#endif // OAIGetTopic_200_response_details_H
