/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINewBillPaymentAllocation.h
 *
 * 
 */

#ifndef OAINewBillPaymentAllocation_H
#define OAINewBillPaymentAllocation_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINewBillPaymentAllocation : public OAIObject {
public:
    OAINewBillPaymentAllocation();
    OAINewBillPaymentAllocation(QString json);
    ~OAINewBillPaymentAllocation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAllocationAmount() const;
    void setAllocationAmount(const double &allocation_amount);
    bool is_allocation_amount_Set() const;
    bool is_allocation_amount_Valid() const;

    QDateTime getAllocationDate() const;
    void setAllocationDate(const QDateTime &allocation_date);
    bool is_allocation_date_Set() const;
    bool is_allocation_date_Valid() const;

    qint64 getBillTransactionIdfk() const;
    void setBillTransactionIdfk(const qint64 &bill_transaction_idfk);
    bool is_bill_transaction_idfk_Set() const;
    bool is_bill_transaction_idfk_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_allocation_amount;
    bool m_allocation_amount_isSet;
    bool m_allocation_amount_isValid;

    QDateTime m_allocation_date;
    bool m_allocation_date_isSet;
    bool m_allocation_date_isValid;

    qint64 m_bill_transaction_idfk;
    bool m_bill_transaction_idfk_isSet;
    bool m_bill_transaction_idfk_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINewBillPaymentAllocation)

#endif // OAINewBillPaymentAllocation_H
