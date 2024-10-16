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
 * OAIAppleSecretDetails.h
 *
 * Apple secret details
 */

#ifndef OAIAppleSecretDetails_H
#define OAIAppleSecretDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppleSecretDetails : public OAIObject {
public:
    OAIAppleSecretDetails();
    OAIAppleSecretDetails(QString json);
    ~OAIAppleSecretDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthCode() const;
    void setAuthCode(const QString &auth_code);
    bool is_auth_code_Set() const;
    bool is_auth_code_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_auth_code;
    bool m_auth_code_isSet;
    bool m_auth_code_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppleSecretDetails)

#endif // OAIAppleSecretDetails_H
