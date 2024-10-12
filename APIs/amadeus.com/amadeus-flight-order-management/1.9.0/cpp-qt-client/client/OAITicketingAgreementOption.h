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
 * OAITicketingAgreementOption.h
 *
 * Ticketing agreement option * **CONFIRM**, when the payment is done * **DELAY_TO_QUEUE**, queue the reservation at a wished date if the payment is not done * **DELAY_TO_CANCEL**, cancel the reservation at a wished date if the payment is not done  Queueing and cancellation occurs at local date and time. When no time is specified, reservation is queued or cancelled at 00:00. 
 */

#ifndef OAITicketingAgreementOption_H
#define OAITicketingAgreementOption_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITicketingAgreementOption : public OAIEnum {
public:
    OAITicketingAgreementOption();
    OAITicketingAgreementOption(QString json);
    ~OAITicketingAgreementOption() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAITicketingAgreementOption {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        CONFIRM, 
        DELAY_TO_QUEUE, 
        DELAY_TO_CANCEL
    };
    OAITicketingAgreementOption::eOAITicketingAgreementOption getValue() const;
    void setValue(const OAITicketingAgreementOption::eOAITicketingAgreementOption& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAITicketingAgreementOption m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITicketingAgreementOption)

#endif // OAITicketingAgreementOption_H
