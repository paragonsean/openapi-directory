/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightOfferSource.h
 *
 * source of the flight offer
 */

#ifndef OAIFlightOfferSource_H
#define OAIFlightOfferSource_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFlightOfferSource : public OAIEnum {
public:
    OAIFlightOfferSource();
    OAIFlightOfferSource(QString json);
    ~OAIFlightOfferSource() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIFlightOfferSource {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        GDS
    };
    OAIFlightOfferSource::eOAIFlightOfferSource getValue() const;
    void setValue(const OAIFlightOfferSource::eOAIFlightOfferSource& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIFlightOfferSource m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightOfferSource)

#endif // OAIFlightOfferSource_H
