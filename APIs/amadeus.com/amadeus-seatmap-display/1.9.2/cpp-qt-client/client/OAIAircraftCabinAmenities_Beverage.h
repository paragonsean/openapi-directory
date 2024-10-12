/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAircraftCabinAmenities_Beverage.h
 *
 * 
 */

#ifndef OAIAircraftCabinAmenities_Beverage_H
#define OAIAircraftCabinAmenities_Beverage_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAircraftCabinAmenities_Beverage : public OAIObject {
public:
    OAIAircraftCabinAmenities_Beverage();
    OAIAircraftCabinAmenities_Beverage(QString json);
    ~OAIAircraftCabinAmenities_Beverage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsChargeable() const;
    void setIsChargeable(const bool &is_chargeable);
    bool is_is_chargeable_Set() const;
    bool is_is_chargeable_Valid() const;

    QString getBeverageType() const;
    void setBeverageType(const QString &beverage_type);
    bool is_beverage_type_Set() const;
    bool is_beverage_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_chargeable;
    bool m_is_chargeable_isSet;
    bool m_is_chargeable_isValid;

    QString m_beverage_type;
    bool m_beverage_type_isSet;
    bool m_beverage_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAircraftCabinAmenities_Beverage)

#endif // OAIAircraftCabinAmenities_Beverage_H
