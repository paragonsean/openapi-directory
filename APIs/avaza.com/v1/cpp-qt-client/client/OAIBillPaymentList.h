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
 * OAIBillPaymentList.h
 *
 * 
 */

#ifndef OAIBillPaymentList_H
#define OAIBillPaymentList_H

#include <QJsonObject>

#include "OAIBillPayment.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBillPayment;

class OAIBillPaymentList : public OAIObject {
public:
    OAIBillPaymentList();
    OAIBillPaymentList(QString json);
    ~OAIBillPaymentList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getPageNumber() const;
    void setPageNumber(const qint32 &page_number);
    bool is_page_number_Set() const;
    bool is_page_number_Valid() const;

    qint32 getPageSize() const;
    void setPageSize(const qint32 &page_size);
    bool is_page_size_Set() const;
    bool is_page_size_Valid() const;

    QList<OAIBillPayment> getPayments() const;
    void setPayments(const QList<OAIBillPayment> &payments);
    bool is_payments_Set() const;
    bool is_payments_Valid() const;

    qint32 getTotalCount() const;
    void setTotalCount(const qint32 &total_count);
    bool is_total_count_Set() const;
    bool is_total_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_page_number;
    bool m_page_number_isSet;
    bool m_page_number_isValid;

    qint32 m_page_size;
    bool m_page_size_isSet;
    bool m_page_size_isValid;

    QList<OAIBillPayment> m_payments;
    bool m_payments_isSet;
    bool m_payments_isValid;

    qint32 m_total_count;
    bool m_total_count_isSet;
    bool m_total_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBillPaymentList)

#endif // OAIBillPaymentList_H
