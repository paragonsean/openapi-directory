/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserProfileResponseInternal.h
 *
 * 
 */

#ifndef OAIUserProfileResponseInternal_H
#define OAIUserProfileResponseInternal_H

#include <QJsonObject>

#include "OAIUserProfileResponseInternal_allOf_settings.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUserProfileResponseInternal_allOf_settings;

class OAIUserProfileResponseInternal : public OAIObject {
public:
    OAIUserProfileResponseInternal();
    OAIUserProfileResponseInternal(QString json);
    ~OAIUserProfileResponseInternal() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAvatarUrl() const;
    void setAvatarUrl(const QString &avatar_url);
    bool is_avatar_url_Set() const;
    bool is_avatar_url_Valid() const;

    bool isCanChangePassword() const;
    void setCanChangePassword(const bool &can_change_password);
    bool is_can_change_password_Set() const;
    bool is_can_change_password_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrigin() const;
    void setOrigin(const QString &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    QList<QString> getPermissions() const;
    void setPermissions(const QList<QString> &permissions);
    bool is_permissions_Set() const;
    bool is_permissions_Valid() const;

    QString getAdminRole() const;
    void setAdminRole(const QString &admin_role);
    bool is_admin_role_Set() const;
    bool is_admin_role_Valid() const;

    QList<QString> getFeatureFlags() const;
    void setFeatureFlags(const QList<QString> &feature_flags);
    bool is_feature_flags_Set() const;
    bool is_feature_flags_Valid() const;

    OAIUserProfileResponseInternal_allOf_settings getSettings() const;
    void setSettings(const OAIUserProfileResponseInternal_allOf_settings &settings);
    bool is_settings_Set() const;
    bool is_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_avatar_url;
    bool m_avatar_url_isSet;
    bool m_avatar_url_isValid;

    bool m_can_change_password;
    bool m_can_change_password_isSet;
    bool m_can_change_password_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    QList<QString> m_permissions;
    bool m_permissions_isSet;
    bool m_permissions_isValid;

    QString m_admin_role;
    bool m_admin_role_isSet;
    bool m_admin_role_isValid;

    QList<QString> m_feature_flags;
    bool m_feature_flags_isSet;
    bool m_feature_flags_isValid;

    OAIUserProfileResponseInternal_allOf_settings m_settings;
    bool m_settings_isSet;
    bool m_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserProfileResponseInternal)

#endif // OAIUserProfileResponseInternal_H
