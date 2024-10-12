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
 * OAIAmenityType.h
 *
 * Amenity type
 */

#ifndef OAIAmenityType_H
#define OAIAmenityType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAmenityType : public OAIEnum {
public:
    OAIAmenityType();
    OAIAmenityType(QString json);
    ~OAIAmenityType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIAmenityType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        BUNDLED_SERVICE, 
        BRANDED_FARES, 
        BAGGAGE, 
        CARBON_OFFSET, 
        FREQUENT_FLYER, 
        GROUND, 
        ENTERTAINMENT, 
        LOUNGE, 
        MEDICAL, 
        MEAL, 
        PETS, 
        RULE_OVERRIDE, 
        STANDBY, 
        STORE, 
        TRAVEL_SERVICES, 
        UNACCOMPANIED_TRAVEL, 
        UPGRADES, 
        UNACCOMPANIED_TRAVEL_UNESCORTED, 
        PRE_RESERVED_SEAT
    };
    OAIAmenityType::eOAIAmenityType getValue() const;
    void setValue(const OAIAmenityType::eOAIAmenityType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIAmenityType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAmenityType)

#endif // OAIAmenityType_H
