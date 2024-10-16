/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetTickersV2_200_response.h
 *
 * 
 */

#ifndef OAIGetTickersV2_200_response_H
#define OAIGetTickersV2_200_response_H

#include <QJsonObject>

#include "OAIObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetTickersV2_200_response : public OAIObject {
public:
    OAIGetTickersV2_200_response();
    OAIGetTickersV2_200_response(QString json);
    ~OAIGetTickersV2_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getRates() const;
    void setRates(const OAIObject &rates);
    bool is_rates_Set() const;
    bool is_rates_Valid() const;

    qint32 getTs() const;
    void setTs(const qint32 &ts);
    bool is_ts_Set() const;
    bool is_ts_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_rates;
    bool m_rates_isSet;
    bool m_rates_isValid;

    qint32 m_ts;
    bool m_ts_isSet;
    bool m_ts_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTickersV2_200_response)

#endif // OAIGetTickersV2_200_response_H
