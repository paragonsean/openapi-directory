/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectCollaboratorInvite.h
 *
 * 
 */

#ifndef OAIProjectCollaboratorInvite_H
#define OAIProjectCollaboratorInvite_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProjectCollaboratorInvite : public OAIObject {
public:
    OAIProjectCollaboratorInvite();
    OAIProjectCollaboratorInvite(QString json);
    ~OAIProjectCollaboratorInvite() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComment() const;
    void setComment(const QString &comment);
    bool is_comment_Set() const;
    bool is_comment_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getRoleName() const;
    void setRoleName(const QString &role_name);
    bool is_role_name_Set() const;
    bool is_role_name_Valid() const;

    qint64 getUserId() const;
    void setUserId(const qint64 &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_comment;
    bool m_comment_isSet;
    bool m_comment_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_role_name;
    bool m_role_name_isSet;
    bool m_role_name_isValid;

    qint64 m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectCollaboratorInvite)

#endif // OAIProjectCollaboratorInvite_H
