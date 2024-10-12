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
 * OAI_listings_post_request_shipping.h
 *
 * 
 */

#ifndef OAI_listings_post_request_shipping_H
#define OAI_listings_post_request_shipping_H

#include <QJsonObject>

#include "OAI_listings_post_request_shipping_rates_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAI_listings_post_request_shipping_rates_inner;

class OAI_listings_post_request_shipping : public OAIObject {
public:
    OAI_listings_post_request_shipping();
    OAI_listings_post_request_shipping(QString json);
    ~OAI_listings_post_request_shipping() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isLocal() const;
    void setLocal(const bool &local);
    bool is_local_Set() const;
    bool is_local_Valid() const;

    QList<OAI_listings_post_request_shipping_rates_inner> getRates() const;
    void setRates(const QList<OAI_listings_post_request_shipping_rates_inner> &rates);
    bool is_rates_Set() const;
    bool is_rates_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_local;
    bool m_local_isSet;
    bool m_local_isValid;

    QList<OAI_listings_post_request_shipping_rates_inner> m_rates;
    bool m_rates_isSet;
    bool m_rates_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_listings_post_request_shipping)

#endif // OAI_listings_post_request_shipping_H
