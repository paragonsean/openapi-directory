/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEC2FirewallDirection.h
 *
 * 
 */

#ifndef OAIEC2FirewallDirection_H
#define OAIEC2FirewallDirection_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEC2FirewallDirection : public OAIEnum {
public:
    OAIEC2FirewallDirection();
    OAIEC2FirewallDirection(QString json);
    ~OAIEC2FirewallDirection() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIEC2FirewallDirection {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        INBOUND, 
        OUTBOUND
    };
    OAIEC2FirewallDirection::eOAIEC2FirewallDirection getValue() const;
    void setValue(const OAIEC2FirewallDirection::eOAIEC2FirewallDirection& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIEC2FirewallDirection m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEC2FirewallDirection)

#endif // OAIEC2FirewallDirection_H
