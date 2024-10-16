/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddWebhookRequestBody.h
 *
 * 
 */

#ifndef OAIAddWebhookRequestBody_H
#define OAIAddWebhookRequestBody_H

#include <QJsonObject>

#include "OAIWebhookTriggers.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhookTriggers;

class OAIAddWebhookRequestBody : public OAIObject {
public:
    OAIAddWebhookRequestBody();
    OAIAddWebhookRequestBody(QString json);
    ~OAIAddWebhookRequestBody() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEndpointUrl() const;
    void setEndpointUrl(const QString &endpoint_url);
    bool is_endpoint_url_Set() const;
    bool is_endpoint_url_Valid() const;

    QString getResource() const;
    void setResource(const QString &resource);
    bool is_resource_Set() const;
    bool is_resource_Valid() const;

    QString getResponseVersion() const;
    void setResponseVersion(const QString &response_version);
    bool is_response_version_Set() const;
    bool is_response_version_Valid() const;

    OAIWebhookTriggers getTriggers() const;
    void setTriggers(const OAIWebhookTriggers &triggers);
    bool is_triggers_Set() const;
    bool is_triggers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_endpoint_url;
    bool m_endpoint_url_isSet;
    bool m_endpoint_url_isValid;

    QString m_resource;
    bool m_resource_isSet;
    bool m_resource_isValid;

    QString m_response_version;
    bool m_response_version_isSet;
    bool m_response_version_isValid;

    OAIWebhookTriggers m_triggers;
    bool m_triggers_isSet;
    bool m_triggers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddWebhookRequestBody)

#endif // OAIAddWebhookRequestBody_H
