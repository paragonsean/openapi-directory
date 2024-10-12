/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreditCard.h
 *
 * credit card
 */

#ifndef OAICreditCard_H
#define OAICreditCard_H

#include <QJsonObject>

#include "OAICreditCardBrand.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreditCard : public OAIObject {
public:
    OAICreditCard();
    OAICreditCard(QString json);
    ~OAICreditCard() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICreditCardBrand getBrand() const;
    void setBrand(const OAICreditCardBrand &brand);
    bool is_brand_Set() const;
    bool is_brand_Valid() const;

    QString getExpiryDate() const;
    void setExpiryDate(const QString &expiry_date);
    bool is_expiry_date_Set() const;
    bool is_expiry_date_Valid() const;

    QString getHolder() const;
    void setHolder(const QString &holder);
    bool is_holder_Set() const;
    bool is_holder_Valid() const;

    QString getNumber() const;
    void setNumber(const QString &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    QList<QString> getFlightOfferIds() const;
    void setFlightOfferIds(const QList<QString> &flight_offer_ids);
    bool is_flight_offer_ids_Set() const;
    bool is_flight_offer_ids_Valid() const;

    QString getSecurityCode() const;
    void setSecurityCode(const QString &security_code);
    bool is_security_code_Set() const;
    bool is_security_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICreditCardBrand m_brand;
    bool m_brand_isSet;
    bool m_brand_isValid;

    QString m_expiry_date;
    bool m_expiry_date_isSet;
    bool m_expiry_date_isValid;

    QString m_holder;
    bool m_holder_isSet;
    bool m_holder_isValid;

    QString m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    QList<QString> m_flight_offer_ids;
    bool m_flight_offer_ids_isSet;
    bool m_flight_offer_ids_isValid;

    QString m_security_code;
    bool m_security_code_isSet;
    bool m_security_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreditCard)

#endif // OAICreditCard_H
