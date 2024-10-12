/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentifierType.h
 *
 * 
 */

#ifndef OAIIdentifierType_H
#define OAIIdentifierType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIdentifierType : public OAIEnum {
public:
    OAIIdentifierType();
    OAIIdentifierType(QString json);
    ~OAIIdentifierType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIIdentifierType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        MOBILE, 
        MR, 
        NDHM_HEALTH_NUMBER, 
        HEALTH_ID
    };
    OAIIdentifierType::eOAIIdentifierType getValue() const;
    void setValue(const OAIIdentifierType::eOAIIdentifierType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIIdentifierType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentifierType)

#endif // OAIIdentifierType_H
