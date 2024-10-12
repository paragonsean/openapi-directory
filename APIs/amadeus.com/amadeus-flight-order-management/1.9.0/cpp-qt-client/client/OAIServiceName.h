/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIServiceName.h
 *
 * type of service
 */

#ifndef OAIServiceName_H
#define OAIServiceName_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIServiceName : public OAIEnum {
public:
    OAIServiceName();
    OAIServiceName(QString json);
    ~OAIServiceName() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIServiceName {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        PRIORITY_BOARDING, 
        AIRPORT_CHECKIN
    };
    OAIServiceName::eOAIServiceName getValue() const;
    void setValue(const OAIServiceName::eOAIServiceName& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIServiceName m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServiceName)

#endif // OAIServiceName_H
