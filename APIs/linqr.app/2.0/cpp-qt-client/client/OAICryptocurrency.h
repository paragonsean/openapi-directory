/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICryptocurrency.h
 *
 * An enumeration.
 */

#ifndef OAICryptocurrency_H
#define OAICryptocurrency_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICryptocurrency : public OAIEnum {
public:
    OAICryptocurrency();
    OAICryptocurrency(QString json);
    ~OAICryptocurrency() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAICryptocurrency {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        BITCOIN, 
        BITCOINCASH, 
        ETHEREUM, 
        LITECOIN, 
        DASH
    };
    OAICryptocurrency::eOAICryptocurrency getValue() const;
    void setValue(const OAICryptocurrency::eOAICryptocurrency& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAICryptocurrency m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICryptocurrency)

#endif // OAICryptocurrency_H
