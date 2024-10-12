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
 * OAISliceDiceIndicator.h
 *
 * slice and Dice indicator, such as Local Availability, Sub OnD(Origin and Destination) 1 Availability and Sub OnD 2 Availability
 */

#ifndef OAISliceDiceIndicator_H
#define OAISliceDiceIndicator_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISliceDiceIndicator : public OAIEnum {
public:
    OAISliceDiceIndicator();
    OAISliceDiceIndicator(QString json);
    ~OAISliceDiceIndicator() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAISliceDiceIndicator {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        LOCAL_AVAILABILITY, 
        SUB_OD_AVAILABILITY_1, 
        SUB_OD_AVAILABILITY_2
    };
    OAISliceDiceIndicator::eOAISliceDiceIndicator getValue() const;
    void setValue(const OAISliceDiceIndicator::eOAISliceDiceIndicator& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAISliceDiceIndicator m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISliceDiceIndicator)

#endif // OAISliceDiceIndicator_H
