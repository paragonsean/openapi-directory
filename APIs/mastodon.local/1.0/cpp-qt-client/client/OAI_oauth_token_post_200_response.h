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
 * OAI_oauth_token_post_200_response.h
 *
 * 
 */

#ifndef OAI_oauth_token_post_200_response_H
#define OAI_oauth_token_post_200_response_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_oauth_token_post_200_response : public OAIObject {
public:
    OAI_oauth_token_post_200_response();
    OAI_oauth_token_post_200_response(QString json);
    ~OAI_oauth_token_post_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessToken() const;
    void setAccessToken(const QString &access_token);
    bool is_access_token_Set() const;
    bool is_access_token_Valid() const;

    qint32 getCreatedAt() const;
    void setCreatedAt(const qint32 &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getTokenType() const;
    void setTokenType(const QString &token_type);
    bool is_token_type_Set() const;
    bool is_token_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_token;
    bool m_access_token_isSet;
    bool m_access_token_isValid;

    qint32 m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_token_type;
    bool m_token_type_isSet;
    bool m_token_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_oauth_token_post_200_response)

#endif // OAI_oauth_token_post_200_response_H
