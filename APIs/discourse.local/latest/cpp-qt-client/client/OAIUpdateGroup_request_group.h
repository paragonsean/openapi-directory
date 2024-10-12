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
 * OAIUpdateGroup_request_group.h
 *
 * 
 */

#ifndef OAIUpdateGroup_request_group_H
#define OAIUpdateGroup_request_group_H

#include <QJsonObject>

#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateGroup_request_group : public OAIObject {
public:
    OAIUpdateGroup_request_group();
    OAIUpdateGroup_request_group(QString json);
    ~OAIUpdateGroup_request_group() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAutomaticMembershipEmailDomains() const;
    void setAutomaticMembershipEmailDomains(const QString &automatic_membership_email_domains);
    bool is_automatic_membership_email_domains_Set() const;
    bool is_automatic_membership_email_domains_Valid() const;

    QString getBioRaw() const;
    void setBioRaw(const QString &bio_raw);
    bool is_bio_raw_Set() const;
    bool is_bio_raw_Valid() const;

    qint32 getDefaultNotificationLevel() const;
    void setDefaultNotificationLevel(const qint32 &default_notification_level);
    bool is_default_notification_level_Set() const;
    bool is_default_notification_level_Valid() const;

    QString getFlairBgColor() const;
    void setFlairBgColor(const QString &flair_bg_color);
    bool is_flair_bg_color_Set() const;
    bool is_flair_bg_color_Valid() const;

    QString getFlairIcon() const;
    void setFlairIcon(const QString &flair_icon);
    bool is_flair_icon_Set() const;
    bool is_flair_icon_Valid() const;

    qint32 getFlairUploadId() const;
    void setFlairUploadId(const qint32 &flair_upload_id);
    bool is_flair_upload_id_Set() const;
    bool is_flair_upload_id_Valid() const;

    QString getFullName() const;
    void setFullName(const QString &full_name);
    bool is_full_name_Set() const;
    bool is_full_name_Valid() const;

    QList<qint32> getMutedCategoryIds() const;
    void setMutedCategoryIds(const QList<qint32> &muted_category_ids);
    bool is_muted_category_ids_Set() const;
    bool is_muted_category_ids_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOwnerUsernames() const;
    void setOwnerUsernames(const QString &owner_usernames);
    bool is_owner_usernames_Set() const;
    bool is_owner_usernames_Valid() const;

    bool isPrimaryGroup() const;
    void setPrimaryGroup(const bool &primary_group);
    bool is_primary_group_Set() const;
    bool is_primary_group_Valid() const;

    bool isPublicAdmission() const;
    void setPublicAdmission(const bool &public_admission);
    bool is_public_admission_Set() const;
    bool is_public_admission_Valid() const;

    bool isPublicExit() const;
    void setPublicExit(const bool &public_exit);
    bool is_public_exit_Set() const;
    bool is_public_exit_Valid() const;

    QList<qint32> getRegularCategoryIds() const;
    void setRegularCategoryIds(const QList<qint32> &regular_category_ids);
    bool is_regular_category_ids_Set() const;
    bool is_regular_category_ids_Valid() const;

    QList<qint32> getTrackingCategoryIds() const;
    void setTrackingCategoryIds(const QList<qint32> &tracking_category_ids);
    bool is_tracking_category_ids_Set() const;
    bool is_tracking_category_ids_Valid() const;

    QString getUsernames() const;
    void setUsernames(const QString &usernames);
    bool is_usernames_Set() const;
    bool is_usernames_Valid() const;

    qint32 getVisibilityLevel() const;
    void setVisibilityLevel(const qint32 &visibility_level);
    bool is_visibility_level_Set() const;
    bool is_visibility_level_Valid() const;

    QList<qint32> getWatchingCategoryIds() const;
    void setWatchingCategoryIds(const QList<qint32> &watching_category_ids);
    bool is_watching_category_ids_Set() const;
    bool is_watching_category_ids_Valid() const;

    QList<qint32> getWatchingFirstPostCategoryIds() const;
    void setWatchingFirstPostCategoryIds(const QList<qint32> &watching_first_post_category_ids);
    bool is_watching_first_post_category_ids_Set() const;
    bool is_watching_first_post_category_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_automatic_membership_email_domains;
    bool m_automatic_membership_email_domains_isSet;
    bool m_automatic_membership_email_domains_isValid;

    QString m_bio_raw;
    bool m_bio_raw_isSet;
    bool m_bio_raw_isValid;

    qint32 m_default_notification_level;
    bool m_default_notification_level_isSet;
    bool m_default_notification_level_isValid;

    QString m_flair_bg_color;
    bool m_flair_bg_color_isSet;
    bool m_flair_bg_color_isValid;

    QString m_flair_icon;
    bool m_flair_icon_isSet;
    bool m_flair_icon_isValid;

    qint32 m_flair_upload_id;
    bool m_flair_upload_id_isSet;
    bool m_flair_upload_id_isValid;

    QString m_full_name;
    bool m_full_name_isSet;
    bool m_full_name_isValid;

    QList<qint32> m_muted_category_ids;
    bool m_muted_category_ids_isSet;
    bool m_muted_category_ids_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_owner_usernames;
    bool m_owner_usernames_isSet;
    bool m_owner_usernames_isValid;

    bool m_primary_group;
    bool m_primary_group_isSet;
    bool m_primary_group_isValid;

    bool m_public_admission;
    bool m_public_admission_isSet;
    bool m_public_admission_isValid;

    bool m_public_exit;
    bool m_public_exit_isSet;
    bool m_public_exit_isValid;

    QList<qint32> m_regular_category_ids;
    bool m_regular_category_ids_isSet;
    bool m_regular_category_ids_isValid;

    QList<qint32> m_tracking_category_ids;
    bool m_tracking_category_ids_isSet;
    bool m_tracking_category_ids_isValid;

    QString m_usernames;
    bool m_usernames_isSet;
    bool m_usernames_isValid;

    qint32 m_visibility_level;
    bool m_visibility_level_isSet;
    bool m_visibility_level_isValid;

    QList<qint32> m_watching_category_ids;
    bool m_watching_category_ids_isSet;
    bool m_watching_category_ids_isValid;

    QList<qint32> m_watching_first_post_category_ids;
    bool m_watching_first_post_category_ids_isSet;
    bool m_watching_first_post_category_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateGroup_request_group)

#endif // OAIUpdateGroup_request_group_H
