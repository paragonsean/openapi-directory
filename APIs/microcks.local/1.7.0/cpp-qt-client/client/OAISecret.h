/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISecret.h
 *
 * A Secret allows grouping informations on how to access a restricted resource such as a repsoitory URL. Secrets are typically used by ImpoortJobs.
 */

#ifndef OAISecret_H
#define OAISecret_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISecret : public OAIObject {
public:
    OAISecret();
    OAISecret(QString json);
    ~OAISecret() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCaCertPem() const;
    void setCaCertPem(const QString &ca_cert_pem);
    bool is_ca_cert_pem_Set() const;
    bool is_ca_cert_pem_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    QString getTokenHeader() const;
    void setTokenHeader(const QString &token_header);
    bool is_token_header_Set() const;
    bool is_token_header_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ca_cert_pem;
    bool m_ca_cert_pem_isSet;
    bool m_ca_cert_pem_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;

    QString m_token_header;
    bool m_token_header_isSet;
    bool m_token_header_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISecret)

#endif // OAISecret_H
