/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAllAccountsAggregatedBillingInformation.h
 *
 * Aggregated Billing Information for a user an the organizations in which the user is an admin.
 */

#ifndef OAIAllAccountsAggregatedBillingInformation_H
#define OAIAllAccountsAggregatedBillingInformation_H

#include <QJsonObject>

#include "OAIBillingAggregatedInformation_getByApp_200_response.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBillingAggregatedInformation_getByApp_200_response;

class OAIAllAccountsAggregatedBillingInformation : public OAIObject {
public:
    OAIAllAccountsAggregatedBillingInformation();
    OAIAllAccountsAggregatedBillingInformation(QString json);
    ~OAIAllAccountsAggregatedBillingInformation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBillingAggregatedInformation_getByApp_200_response getAggregatedBillings() const;
    void setAggregatedBillings(const OAIBillingAggregatedInformation_getByApp_200_response &aggregated_billings);
    bool is_aggregated_billings_Set() const;
    bool is_aggregated_billings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBillingAggregatedInformation_getByApp_200_response m_aggregated_billings;
    bool m_aggregated_billings_isSet;
    bool m_aggregated_billings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAllAccountsAggregatedBillingInformation)

#endif // OAIAllAccountsAggregatedBillingInformation_H
