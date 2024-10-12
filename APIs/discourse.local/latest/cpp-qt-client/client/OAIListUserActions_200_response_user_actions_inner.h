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
 * OAIListUserActions_200_response_user_actions_inner.h
 *
 * 
 */

#ifndef OAIListUserActions_200_response_user_actions_inner_H
#define OAIListUserActions_200_response_user_actions_inner_H

#include <QJsonObject>

#include <QJsonValue>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIListUserActions_200_response_user_actions_inner : public OAIObject {
public:
    OAIListUserActions_200_response_user_actions_inner();
    OAIListUserActions_200_response_user_actions_inner(QString json);
    ~OAIListUserActions_200_response_user_actions_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getActingAvatarTemplate() const;
    void setActingAvatarTemplate(const QString &acting_avatar_template);
    bool is_acting_avatar_template_Set() const;
    bool is_acting_avatar_template_Valid() const;

    QString getActingName() const;
    void setActingName(const QString &acting_name);
    bool is_acting_name_Set() const;
    bool is_acting_name_Valid() const;

    qint32 getActingUserId() const;
    void setActingUserId(const qint32 &acting_user_id);
    bool is_acting_user_id_Set() const;
    bool is_acting_user_id_Valid() const;

    QString getActingUsername() const;
    void setActingUsername(const QString &acting_username);
    bool is_acting_username_Set() const;
    bool is_acting_username_Valid() const;

    QString getActionCode() const;
    void setActionCode(const QString &action_code);
    bool is_action_code_Set() const;
    bool is_action_code_Valid() const;

    qint32 getActionType() const;
    void setActionType(const qint32 &action_type);
    bool is_action_type_Set() const;
    bool is_action_type_Valid() const;

    bool isArchived() const;
    void setArchived(const bool &archived);
    bool is_archived_Set() const;
    bool is_archived_Valid() const;

    QString getAvatarTemplate() const;
    void setAvatarTemplate(const QString &avatar_template);
    bool is_avatar_template_Set() const;
    bool is_avatar_template_Valid() const;

    qint32 getCategoryId() const;
    void setCategoryId(const qint32 &category_id);
    bool is_category_id_Set() const;
    bool is_category_id_Valid() const;

    bool isClosed() const;
    void setClosed(const bool &closed);
    bool is_closed_Set() const;
    bool is_closed_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QString getExcerpt() const;
    void setExcerpt(const QString &excerpt);
    bool is_excerpt_Set() const;
    bool is_excerpt_Valid() const;

    QString getHidden() const;
    void setHidden(const QString &hidden);
    bool is_hidden_Set() const;
    bool is_hidden_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPostId() const;
    void setPostId(const QString &post_id);
    bool is_post_id_Set() const;
    bool is_post_id_Valid() const;

    qint32 getPostNumber() const;
    void setPostNumber(const qint32 &post_number);
    bool is_post_number_Set() const;
    bool is_post_number_Valid() const;

    QString getPostType() const;
    void setPostType(const QString &post_type);
    bool is_post_type_Set() const;
    bool is_post_type_Valid() const;

    QString getSlug() const;
    void setSlug(const QString &slug);
    bool is_slug_Set() const;
    bool is_slug_Valid() const;

    QString getTargetName() const;
    void setTargetName(const QString &target_name);
    bool is_target_name_Set() const;
    bool is_target_name_Valid() const;

    qint32 getTargetUserId() const;
    void setTargetUserId(const qint32 &target_user_id);
    bool is_target_user_id_Set() const;
    bool is_target_user_id_Valid() const;

    QString getTargetUsername() const;
    void setTargetUsername(const QString &target_username);
    bool is_target_username_Set() const;
    bool is_target_username_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    qint32 getTopicId() const;
    void setTopicId(const qint32 &topic_id);
    bool is_topic_id_Set() const;
    bool is_topic_id_Valid() const;

    qint32 getUserId() const;
    void setUserId(const qint32 &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_acting_avatar_template;
    bool m_acting_avatar_template_isSet;
    bool m_acting_avatar_template_isValid;

    QString m_acting_name;
    bool m_acting_name_isSet;
    bool m_acting_name_isValid;

    qint32 m_acting_user_id;
    bool m_acting_user_id_isSet;
    bool m_acting_user_id_isValid;

    QString m_acting_username;
    bool m_acting_username_isSet;
    bool m_acting_username_isValid;

    QString m_action_code;
    bool m_action_code_isSet;
    bool m_action_code_isValid;

    qint32 m_action_type;
    bool m_action_type_isSet;
    bool m_action_type_isValid;

    bool m_archived;
    bool m_archived_isSet;
    bool m_archived_isValid;

    QString m_avatar_template;
    bool m_avatar_template_isSet;
    bool m_avatar_template_isValid;

    qint32 m_category_id;
    bool m_category_id_isSet;
    bool m_category_id_isValid;

    bool m_closed;
    bool m_closed_isSet;
    bool m_closed_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_excerpt;
    bool m_excerpt_isSet;
    bool m_excerpt_isValid;

    QString m_hidden;
    bool m_hidden_isSet;
    bool m_hidden_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_post_id;
    bool m_post_id_isSet;
    bool m_post_id_isValid;

    qint32 m_post_number;
    bool m_post_number_isSet;
    bool m_post_number_isValid;

    QString m_post_type;
    bool m_post_type_isSet;
    bool m_post_type_isValid;

    QString m_slug;
    bool m_slug_isSet;
    bool m_slug_isValid;

    QString m_target_name;
    bool m_target_name_isSet;
    bool m_target_name_isValid;

    qint32 m_target_user_id;
    bool m_target_user_id_isSet;
    bool m_target_user_id_isValid;

    QString m_target_username;
    bool m_target_username_isSet;
    bool m_target_username_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    qint32 m_topic_id;
    bool m_topic_id_isSet;
    bool m_topic_id_isValid;

    qint32 m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIListUserActions_200_response_user_actions_inner)

#endif // OAIListUserActions_200_response_user_actions_inner_H
