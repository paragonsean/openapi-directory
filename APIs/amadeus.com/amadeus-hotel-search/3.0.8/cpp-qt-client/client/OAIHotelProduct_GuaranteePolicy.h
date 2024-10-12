/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHotelProduct_GuaranteePolicy.h
 *
 * the guarantee policy information applicable to the offer. It includes accepted payments
 */

#ifndef OAIHotelProduct_GuaranteePolicy_H
#define OAIHotelProduct_GuaranteePolicy_H

#include <QJsonObject>

#include "OAIHotelProduct_PaymentPolicy.h"
#include "OAIQualifiedFreeText.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHotelProduct_PaymentPolicy;
class OAIQualifiedFreeText;

class OAIHotelProduct_GuaranteePolicy : public OAIObject {
public:
    OAIHotelProduct_GuaranteePolicy();
    OAIHotelProduct_GuaranteePolicy(QString json);
    ~OAIHotelProduct_GuaranteePolicy() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIHotelProduct_PaymentPolicy getAcceptedPayments() const;
    void setAcceptedPayments(const OAIHotelProduct_PaymentPolicy &accepted_payments);
    bool is_accepted_payments_Set() const;
    bool is_accepted_payments_Valid() const;

    OAIQualifiedFreeText getDescription() const;
    void setDescription(const OAIQualifiedFreeText &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIHotelProduct_PaymentPolicy m_accepted_payments;
    bool m_accepted_payments_isSet;
    bool m_accepted_payments_isValid;

    OAIQualifiedFreeText m_description;
    bool m_description_isSet;
    bool m_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHotelProduct_GuaranteePolicy)

#endif // OAIHotelProduct_GuaranteePolicy_H
