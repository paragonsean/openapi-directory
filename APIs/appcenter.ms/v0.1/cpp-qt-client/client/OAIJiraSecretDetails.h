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
 * OAIJiraSecretDetails.h
 *
 * Jira secret details
 */

#ifndef OAIJiraSecretDetails_H
#define OAIJiraSecretDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIJiraSecretDetails : public OAIObject {
public:
    OAIJiraSecretDetails();
    OAIJiraSecretDetails(QString json);
    ~OAIJiraSecretDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseUrl() const;
    void setBaseUrl(const QString &base_url);
    bool is_base_url_Set() const;
    bool is_base_url_Valid() const;

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

    QString m_base_url;
    bool m_base_url_isSet;
    bool m_base_url_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIJiraSecretDetails)

#endif // OAIJiraSecretDetails_H
