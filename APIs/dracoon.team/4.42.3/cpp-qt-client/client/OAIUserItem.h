/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserItem.h
 *
 * User information
 */

#ifndef OAIUserItem_H
#define OAIUserItem_H

#include <QJsonObject>

#include "OAIRoleList.h"
#include "OAIUserAttributes.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUserAttributes;
class OAIRoleList;

class OAIUserItem : public OAIObject {
public:
    OAIUserItem();
    OAIUserItem(QString json);
    ~OAIUserItem() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAvatarUuid() const;
    void setAvatarUuid(const QString &avatar_uuid);
    bool is_avatar_uuid_Set() const;
    bool is_avatar_uuid_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QDateTime getExpireAt() const;
    void setExpireAt(const QDateTime &expire_at);
    bool is_expire_at_Set() const;
    bool is_expire_at_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    Q_DECL_DEPRECATED QString getGender() const;
    Q_DECL_DEPRECATED void setGender(const QString &gender);
    Q_DECL_DEPRECATED bool is_gender_Set() const;
    Q_DECL_DEPRECATED bool is_gender_Valid() const;

    Q_DECL_DEPRECATED bool isHasManageableRooms() const;
    Q_DECL_DEPRECATED void setHasManageableRooms(const bool &has_manageable_rooms);
    Q_DECL_DEPRECATED bool is_has_manageable_rooms_Set() const;
    Q_DECL_DEPRECATED bool is_has_manageable_rooms_Valid() const;

    qint64 getHomeRoomId() const;
    void setHomeRoomId(const qint64 &home_room_id);
    bool is_home_room_id_Set() const;
    bool is_home_room_id_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsEncryptionEnabled() const;
    void setIsEncryptionEnabled(const bool &is_encryption_enabled);
    bool is_is_encryption_enabled_Set() const;
    bool is_is_encryption_enabled_Valid() const;

    bool isIsLocked() const;
    void setIsLocked(const bool &is_locked);
    bool is_is_locked_Set() const;
    bool is_is_locked_Valid() const;

    QDateTime getLastLoginSuccessAt() const;
    void setLastLoginSuccessAt(const QDateTime &last_login_success_at);
    bool is_last_login_success_at_Set() const;
    bool is_last_login_success_at_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    Q_DECL_DEPRECATED qint32 getLockStatus() const;
    Q_DECL_DEPRECATED void setLockStatus(const qint32 &lock_status);
    Q_DECL_DEPRECATED bool is_lock_status_Set() const;
    Q_DECL_DEPRECATED bool is_lock_status_Valid() const;

    Q_DECL_DEPRECATED QString getLogin() const;
    Q_DECL_DEPRECATED void setLogin(const QString &login);
    Q_DECL_DEPRECATED bool is_login_Set() const;
    Q_DECL_DEPRECATED bool is_login_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    Q_DECL_DEPRECATED QString getTitle() const;
    Q_DECL_DEPRECATED void setTitle(const QString &title);
    Q_DECL_DEPRECATED bool is_title_Set() const;
    Q_DECL_DEPRECATED bool is_title_Valid() const;

    Q_DECL_DEPRECATED OAIUserAttributes getUserAttributes() const;
    Q_DECL_DEPRECATED void setUserAttributes(const OAIUserAttributes &user_attributes);
    Q_DECL_DEPRECATED bool is_user_attributes_Set() const;
    Q_DECL_DEPRECATED bool is_user_attributes_Valid() const;

    QString getUserName() const;
    void setUserName(const QString &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    OAIRoleList getUserRoles() const;
    void setUserRoles(const OAIRoleList &user_roles);
    bool is_user_roles_Set() const;
    bool is_user_roles_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_avatar_uuid;
    bool m_avatar_uuid_isSet;
    bool m_avatar_uuid_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QDateTime m_expire_at;
    bool m_expire_at_isSet;
    bool m_expire_at_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    bool m_has_manageable_rooms;
    bool m_has_manageable_rooms_isSet;
    bool m_has_manageable_rooms_isValid;

    qint64 m_home_room_id;
    bool m_home_room_id_isSet;
    bool m_home_room_id_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_encryption_enabled;
    bool m_is_encryption_enabled_isSet;
    bool m_is_encryption_enabled_isValid;

    bool m_is_locked;
    bool m_is_locked_isSet;
    bool m_is_locked_isValid;

    QDateTime m_last_login_success_at;
    bool m_last_login_success_at_isSet;
    bool m_last_login_success_at_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    qint32 m_lock_status;
    bool m_lock_status_isSet;
    bool m_lock_status_isValid;

    QString m_login;
    bool m_login_isSet;
    bool m_login_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    OAIUserAttributes m_user_attributes;
    bool m_user_attributes_isSet;
    bool m_user_attributes_isValid;

    QString m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;

    OAIRoleList m_user_roles;
    bool m_user_roles_isSet;
    bool m_user_roles_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserItem)

#endif // OAIUserItem_H
