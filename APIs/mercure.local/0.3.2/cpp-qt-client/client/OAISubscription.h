/**
 * The Mercure protocol
 * [Mercure](https://mercure.rocks) is a protocol allowing to push data updates to web browsers and other HTTP clients in a convenient, fast, reliable and battery-efficient way.
 *
 * The version of the OpenAPI document: 0.3.2
 * Contact: contact@mercure.rocks
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISubscription.h
 *
 * 
 */

#ifndef OAISubscription_H
#define OAISubscription_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISubscription : public OAIObject {
public:
    OAISubscription();
    OAISubscription(QString json);
    ~OAISubscription() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContext() const;
    void setContext(const QString &context);
    bool is_context_Set() const;
    bool is_context_Valid() const;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLastEventId() const;
    void setLastEventId(const QString &last_event_id);
    bool is_last_event_id_Set() const;
    bool is_last_event_id_Valid() const;

    OAIObject getPayload() const;
    void setPayload(const OAIObject &payload);
    bool is_payload_Set() const;
    bool is_payload_Valid() const;

    QString getSubscriber() const;
    void setSubscriber(const QString &subscriber);
    bool is_subscriber_Set() const;
    bool is_subscriber_Valid() const;

    QString getTopic() const;
    void setTopic(const QString &topic);
    bool is_topic_Set() const;
    bool is_topic_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_context;
    bool m_context_isSet;
    bool m_context_isValid;

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last_event_id;
    bool m_last_event_id_isSet;
    bool m_last_event_id_isValid;

    OAIObject m_payload;
    bool m_payload_isSet;
    bool m_payload_isValid;

    QString m_subscriber;
    bool m_subscriber_isSet;
    bool m_subscriber_isValid;

    QString m_topic;
    bool m_topic_isSet;
    bool m_topic_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISubscription)

#endif // OAISubscription_H
