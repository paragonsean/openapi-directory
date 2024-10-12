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
 * OAISubscriptions.h
 *
 * 
 */

#ifndef OAISubscriptions_H
#define OAISubscriptions_H

#include <QJsonObject>

#include "OAISubscription.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISubscription;

class OAISubscriptions : public OAIObject {
public:
    OAISubscriptions();
    OAISubscriptions(QString json);
    ~OAISubscriptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContext() const;
    void setContext(const QString &context);
    bool is_context_Set() const;
    bool is_context_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLastEventId() const;
    void setLastEventId(const QString &last_event_id);
    bool is_last_event_id_Set() const;
    bool is_last_event_id_Valid() const;

    QList<OAISubscription> getSubscriptions() const;
    void setSubscriptions(const QList<OAISubscription> &subscriptions);
    bool is_subscriptions_Set() const;
    bool is_subscriptions_Valid() const;

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

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last_event_id;
    bool m_last_event_id_isSet;
    bool m_last_event_id_isValid;

    QList<OAISubscription> m_subscriptions;
    bool m_subscriptions_isSet;
    bool m_subscriptions_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISubscriptions)

#endif // OAISubscriptions_H
