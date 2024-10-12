/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_webhooks_registrations_post_request.h
 *
 * 
 */

#ifndef OAI_webhooks_registrations_post_request_H
#define OAI_webhooks_registrations_post_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_webhooks_registrations_post_request : public OAIObject {
public:
    OAI_webhooks_registrations_post_request();
    OAI_webhooks_registrations_post_request(QString json);
    ~OAI_webhooks_registrations_post_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getTopic() const;
    void setTopic(const QString &topic);
    bool is_topic_Set() const;
    bool is_topic_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_topic;
    bool m_topic_isSet;
    bool m_topic_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_webhooks_registrations_post_request)

#endif // OAI_webhooks_registrations_post_request_H
