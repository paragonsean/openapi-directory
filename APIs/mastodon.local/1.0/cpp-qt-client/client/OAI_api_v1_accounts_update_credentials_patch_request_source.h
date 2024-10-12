/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_api_v1_accounts_update_credentials_patch_request_source.h
 *
 * 
 */

#ifndef OAI_api_v1_accounts_update_credentials_patch_request_source_H
#define OAI_api_v1_accounts_update_credentials_patch_request_source_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v1_accounts_update_credentials_patch_request_source : public OAIObject {
public:
    OAI_api_v1_accounts_update_credentials_patch_request_source();
    OAI_api_v1_accounts_update_credentials_patch_request_source(QString json);
    ~OAI_api_v1_accounts_update_credentials_patch_request_source() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    QString getPrivacy() const;
    void setPrivacy(const QString &privacy);
    bool is_privacy_Set() const;
    bool is_privacy_Valid() const;

    bool isSensitive() const;
    void setSensitive(const bool &sensitive);
    bool is_sensitive_Set() const;
    bool is_sensitive_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_privacy;
    bool m_privacy_isSet;
    bool m_privacy_isValid;

    bool m_sensitive;
    bool m_sensitive_isSet;
    bool m_sensitive_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v1_accounts_update_credentials_patch_request_source)

#endif // OAI_api_v1_accounts_update_credentials_patch_request_source_H
