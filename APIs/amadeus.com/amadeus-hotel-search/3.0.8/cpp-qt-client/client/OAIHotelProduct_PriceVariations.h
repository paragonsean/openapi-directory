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
 * OAIHotelProduct_PriceVariations.h
 *
 * Daily price variations and the average daily price (when available) is shown here
 */

#ifndef OAIHotelProduct_PriceVariations_H
#define OAIHotelProduct_PriceVariations_H

#include <QJsonObject>

#include "OAIHotelProduct_PriceVariation.h"
#include "OAIPrice.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPrice;
class OAIHotelProduct_PriceVariation;

class OAIHotelProduct_PriceVariations : public OAIObject {
public:
    OAIHotelProduct_PriceVariations();
    OAIHotelProduct_PriceVariations(QString json);
    ~OAIHotelProduct_PriceVariations() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPrice getAverage() const;
    void setAverage(const OAIPrice &average);
    bool is_average_Set() const;
    bool is_average_Valid() const;

    QList<OAIHotelProduct_PriceVariation> getChanges() const;
    void setChanges(const QList<OAIHotelProduct_PriceVariation> &changes);
    bool is_changes_Set() const;
    bool is_changes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPrice m_average;
    bool m_average_isSet;
    bool m_average_isValid;

    QList<OAIHotelProduct_PriceVariation> m_changes;
    bool m_changes_isSet;
    bool m_changes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHotelProduct_PriceVariations)

#endif // OAIHotelProduct_PriceVariations_H
