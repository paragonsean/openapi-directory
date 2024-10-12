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
 * OAIUserInfo.h
 *
 * User information
 */

#ifndef OAIUserInfo_H
#define OAIUserInfo_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUserInfo : public OAIObject {
public:
    OAIUserInfo();
    OAIUserInfo(QString json);
    ~OAIUserInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAvatarUuid() const;
    void setAvatarUuid(const QString &avatar_uuid);
    bool is_avatar_uuid_Set() const;
    bool is_avatar_uuid_Valid() const;

    Q_DECL_DEPRECATED QString getDisplayName() const;
    Q_DECL_DEPRECATED void setDisplayName(const QString &display_name);
    Q_DECL_DEPRECATED bool is_display_name_Set() const;
    Q_DECL_DEPRECATED bool is_display_name_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    Q_DECL_DEPRECATED QString getTitle() const;
    Q_DECL_DEPRECATED void setTitle(const QString &title);
    Q_DECL_DEPRECATED bool is_title_Set() const;
    Q_DECL_DEPRECATED bool is_title_Valid() const;

    QString getUserName() const;
    void setUserName(const QString &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    QString getUserType() const;
    void setUserType(const QString &user_type);
    bool is_user_type_Set() const;
    bool is_user_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_avatar_uuid;
    bool m_avatar_uuid_isSet;
    bool m_avatar_uuid_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;

    QString m_user_type;
    bool m_user_type_isSet;
    bool m_user_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserInfo)

#endif // OAIUserInfo_H
