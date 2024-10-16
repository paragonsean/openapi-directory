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
 * OAIPaymentRefundRequest.h
 *
 * The Payment Refund Request Payload
 */

#ifndef OAIPaymentRefundRequest_H
#define OAIPaymentRefundRequest_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPaymentRefundRequest : public OAIObject {
public:
    OAIPaymentRefundRequest();
    OAIPaymentRefundRequest(QString json);
    ~OAIPaymentRefundRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAmount() const;
    void setAmount(const qint32 &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    qint32 getRefundAmountAvailable() const;
    void setRefundAmountAvailable(const qint32 &refund_amount_available);
    bool is_refund_amount_available_Set() const;
    bool is_refund_amount_available_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    qint32 m_refund_amount_available;
    bool m_refund_amount_available_isSet;
    bool m_refund_amount_available_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPaymentRefundRequest)

#endif // OAIPaymentRefundRequest_H
