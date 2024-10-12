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
 * OAIFeeType.h
 *
 * type of fee
 */

#ifndef OAIFeeType_H
#define OAIFeeType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFeeType : public OAIEnum {
public:
    OAIFeeType();
    OAIFeeType(QString json);
    ~OAIFeeType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIFeeType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        TICKETING, 
        FORM_OF_PAYMENT, 
        SUPPLIER
    };
    OAIFeeType::eOAIFeeType getValue() const;
    void setValue(const OAIFeeType::eOAIFeeType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIFeeType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFeeType)

#endif // OAIFeeType_H
