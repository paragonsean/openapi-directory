/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVerificationEmail.h
 *
 * 
 */

#ifndef OAIVerificationEmail_H
#define OAIVerificationEmail_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVerificationEmail : public OAIObject {
public:
    OAIVerificationEmail();
    OAIVerificationEmail(QString json);
    ~OAIVerificationEmail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    bool isVerified() const;
    void setVerified(const bool &verified);
    bool is_verified_Set() const;
    bool is_verified_Valid() const;

    QDateTime getVerifiedAt() const;
    void setVerifiedAt(const QDateTime &verified_at);
    bool is_verified_at_Set() const;
    bool is_verified_at_Valid() const;

    QString getVerifiedBy() const;
    void setVerifiedBy(const QString &verified_by);
    bool is_verified_by_Set() const;
    bool is_verified_by_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    bool m_verified;
    bool m_verified_isSet;
    bool m_verified_isValid;

    QDateTime m_verified_at;
    bool m_verified_at_isSet;
    bool m_verified_at_isValid;

    QString m_verified_by;
    bool m_verified_by_isSet;
    bool m_verified_by_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVerificationEmail)

#endif // OAIVerificationEmail_H
