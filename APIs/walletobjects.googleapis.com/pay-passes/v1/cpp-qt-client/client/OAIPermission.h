/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPermission.h
 *
 * 
 */

#ifndef OAIPermission_H
#define OAIPermission_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPermission : public OAIObject {
public:
    OAIPermission();
    OAIPermission(QString json);
    ~OAIPermission() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmailAddress() const;
    void setEmailAddress(const QString &email_address);
    bool is_email_address_Set() const;
    bool is_email_address_Valid() const;

    QString getRole() const;
    void setRole(const QString &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email_address;
    bool m_email_address_isSet;
    bool m_email_address_isValid;

    QString m_role;
    bool m_role_isSet;
    bool m_role_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPermission)

#endif // OAIPermission_H
