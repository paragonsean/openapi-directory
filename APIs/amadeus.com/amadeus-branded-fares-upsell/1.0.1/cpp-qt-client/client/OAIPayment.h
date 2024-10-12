/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPayment.h
 *
 * 
 */

#ifndef OAIPayment_H
#define OAIPayment_H

#include <QJsonObject>

#include "OAIPaymentBrand.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPayment : public OAIObject {
public:
    OAIPayment();
    OAIPayment(QString json);
    ~OAIPayment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getBinNumber() const;
    void setBinNumber(const qint32 &bin_number);
    bool is_bin_number_Set() const;
    bool is_bin_number_Valid() const;

    OAIPaymentBrand getBrand() const;
    void setBrand(const OAIPaymentBrand &brand);
    bool is_brand_Set() const;
    bool is_brand_Valid() const;

    QList<QString> getFlightOfferIds() const;
    void setFlightOfferIds(const QList<QString> &flight_offer_ids);
    bool is_flight_offer_ids_Set() const;
    bool is_flight_offer_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_bin_number;
    bool m_bin_number_isSet;
    bool m_bin_number_isValid;

    OAIPaymentBrand m_brand;
    bool m_brand_isSet;
    bool m_brand_isValid;

    QList<QString> m_flight_offer_ids;
    bool m_flight_offer_ids_isSet;
    bool m_flight_offer_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPayment)

#endif // OAIPayment_H
