/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITravelClass.h
 *
 * quality of service offered in the cabin where the seat is located in this flight. Economy, premium economy, business or first class
 */

#ifndef OAITravelClass_H
#define OAITravelClass_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITravelClass : public OAIEnum {
public:
    OAITravelClass();
    OAITravelClass(QString json);
    ~OAITravelClass() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAITravelClass {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        ECONOMY, 
        PREMIUM_ECONOMY, 
        BUSINESS, 
        FIRST
    };
    OAITravelClass::eOAITravelClass getValue() const;
    void setValue(const OAITravelClass::eOAITravelClass& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAITravelClass m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITravelClass)

#endif // OAITravelClass_H
