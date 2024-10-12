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
 * OAITravelerPricing.h
 *
 * 
 */

#ifndef OAITravelerPricing_H
#define OAITravelerPricing_H

#include <QJsonObject>

#include "OAIFareDetailsBySegment.h"
#include "OAIPrice.h"
#include "OAITravelerPricingFareOption.h"
#include "OAITravelerType.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFareDetailsBySegment;
class OAIPrice;

class OAITravelerPricing : public OAIObject {
public:
    OAITravelerPricing();
    OAITravelerPricing(QString json);
    ~OAITravelerPricing() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAssociatedAdultId() const;
    void setAssociatedAdultId(const QString &associated_adult_id);
    bool is_associated_adult_id_Set() const;
    bool is_associated_adult_id_Valid() const;

    QList<OAIFareDetailsBySegment> getFareDetailsBySegment() const;
    void setFareDetailsBySegment(const QList<OAIFareDetailsBySegment> &fare_details_by_segment);
    bool is_fare_details_by_segment_Set() const;
    bool is_fare_details_by_segment_Valid() const;

    OAITravelerPricingFareOption getFareOption() const;
    void setFareOption(const OAITravelerPricingFareOption &fare_option);
    bool is_fare_option_Set() const;
    bool is_fare_option_Valid() const;

    OAIPrice getPrice() const;
    void setPrice(const OAIPrice &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getTravelerId() const;
    void setTravelerId(const QString &traveler_id);
    bool is_traveler_id_Set() const;
    bool is_traveler_id_Valid() const;

    OAITravelerType getTravelerType() const;
    void setTravelerType(const OAITravelerType &traveler_type);
    bool is_traveler_type_Set() const;
    bool is_traveler_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_associated_adult_id;
    bool m_associated_adult_id_isSet;
    bool m_associated_adult_id_isValid;

    QList<OAIFareDetailsBySegment> m_fare_details_by_segment;
    bool m_fare_details_by_segment_isSet;
    bool m_fare_details_by_segment_isValid;

    OAITravelerPricingFareOption m_fare_option;
    bool m_fare_option_isSet;
    bool m_fare_option_isValid;

    OAIPrice m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_traveler_id;
    bool m_traveler_id_isSet;
    bool m_traveler_id_isValid;

    OAITravelerType m_traveler_type;
    bool m_traveler_type_isSet;
    bool m_traveler_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITravelerPricing)

#endif // OAITravelerPricing_H
