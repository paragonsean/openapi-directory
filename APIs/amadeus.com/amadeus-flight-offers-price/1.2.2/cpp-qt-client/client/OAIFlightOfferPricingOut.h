/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightOfferPricingOut.h
 *
 * priced flight Offers and conditions
 */

#ifndef OAIFlightOfferPricingOut_H
#define OAIFlightOfferPricingOut_H

#include <QJsonObject>

#include "OAIBookingRequirements.h"
#include "OAIFlightOffer.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBookingRequirements;
class OAIFlightOffer;

class OAIFlightOfferPricingOut : public OAIObject {
public:
    OAIFlightOfferPricingOut();
    OAIFlightOfferPricingOut(QString json);
    ~OAIFlightOfferPricingOut() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBookingRequirements getBookingRequirements() const;
    void setBookingRequirements(const OAIBookingRequirements &booking_requirements);
    bool is_booking_requirements_Set() const;
    bool is_booking_requirements_Valid() const;

    QList<OAIFlightOffer> getFlightOffers() const;
    void setFlightOffers(const QList<OAIFlightOffer> &flight_offers);
    bool is_flight_offers_Set() const;
    bool is_flight_offers_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBookingRequirements m_booking_requirements;
    bool m_booking_requirements_isSet;
    bool m_booking_requirements_isValid;

    QList<OAIFlightOffer> m_flight_offers;
    bool m_flight_offers_isSet;
    bool m_flight_offers_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightOfferPricingOut)

#endif // OAIFlightOfferPricingOut_H
