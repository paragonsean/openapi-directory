/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPaymentEvent.h
 *
 * A List of Payment Events information
 */

#ifndef OAIPaymentEvent_H
#define OAIPaymentEvent_H

#include <QJsonObject>

#include "OAIPaymentEventLink.h"
#include "OAIPaymentState.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPaymentEventLink;
class OAIPaymentState;

class OAIPaymentEvent : public OAIObject {
public:
    OAIPaymentEvent();
    OAIPaymentEvent(QString json);
    ~OAIPaymentEvent() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPaymentEventLink getLinks() const;
    void setLinks(const OAIPaymentEventLink &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QString getPaymentId() const;
    void setPaymentId(const QString &payment_id);
    bool is_payment_id_Set() const;
    bool is_payment_id_Valid() const;

    OAIPaymentState getState() const;
    void setState(const OAIPaymentState &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPaymentEventLink m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QString m_payment_id;
    bool m_payment_id_isSet;
    bool m_payment_id_isValid;

    OAIPaymentState m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPaymentEvent)

#endif // OAIPaymentEvent_H
