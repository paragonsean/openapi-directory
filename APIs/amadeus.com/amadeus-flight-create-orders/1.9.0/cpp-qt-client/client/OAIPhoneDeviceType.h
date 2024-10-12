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
 * OAIPhoneDeviceType.h
 *
 * Type of the device (Landline, Mobile or Fax)
 */

#ifndef OAIPhoneDeviceType_H
#define OAIPhoneDeviceType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPhoneDeviceType : public OAIEnum {
public:
    OAIPhoneDeviceType();
    OAIPhoneDeviceType(QString json);
    ~OAIPhoneDeviceType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIPhoneDeviceType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        MOBILE, 
        LANDLINE, 
        FAX
    };
    OAIPhoneDeviceType::eOAIPhoneDeviceType getValue() const;
    void setValue(const OAIPhoneDeviceType::eOAIPhoneDeviceType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIPhoneDeviceType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPhoneDeviceType)

#endif // OAIPhoneDeviceType_H
