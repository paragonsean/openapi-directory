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
 * OAIBillIssuerDetails.h
 *
 * 
 */

#ifndef OAIBillIssuerDetails_H
#define OAIBillIssuerDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBillIssuerDetails : public OAIObject {
public:
    OAIBillIssuerDetails();
    OAIBillIssuerDetails(QString json);
    ~OAIBillIssuerDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBillingAddress() const;
    void setBillingAddress(const QString &billing_address);
    bool is_billing_address_Set() const;
    bool is_billing_address_Valid() const;

    QString getBillingAddressCity() const;
    void setBillingAddressCity(const QString &billing_address_city);
    bool is_billing_address_city_Set() const;
    bool is_billing_address_city_Valid() const;

    QString getBillingAddressLine() const;
    void setBillingAddressLine(const QString &billing_address_line);
    bool is_billing_address_line_Set() const;
    bool is_billing_address_line_Valid() const;

    QString getBillingAddressPostCode() const;
    void setBillingAddressPostCode(const QString &billing_address_post_code);
    bool is_billing_address_post_code_Set() const;
    bool is_billing_address_post_code_Valid() const;

    QString getBillingAddressState() const;
    void setBillingAddressState(const QString &billing_address_state);
    bool is_billing_address_state_Set() const;
    bool is_billing_address_state_Valid() const;

    QString getBillingCountryCode() const;
    void setBillingCountryCode(const QString &billing_country_code);
    bool is_billing_country_code_Set() const;
    bool is_billing_country_code_Valid() const;

    qint32 getCompanyIdfk() const;
    void setCompanyIdfk(const qint32 &company_idfk);
    bool is_company_idfk_Set() const;
    bool is_company_idfk_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_billing_address;
    bool m_billing_address_isSet;
    bool m_billing_address_isValid;

    QString m_billing_address_city;
    bool m_billing_address_city_isSet;
    bool m_billing_address_city_isValid;

    QString m_billing_address_line;
    bool m_billing_address_line_isSet;
    bool m_billing_address_line_isValid;

    QString m_billing_address_post_code;
    bool m_billing_address_post_code_isSet;
    bool m_billing_address_post_code_isValid;

    QString m_billing_address_state;
    bool m_billing_address_state_isSet;
    bool m_billing_address_state_isValid;

    QString m_billing_country_code;
    bool m_billing_country_code_isSet;
    bool m_billing_country_code_isValid;

    qint32 m_company_idfk;
    bool m_company_idfk_isSet;
    bool m_company_idfk_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBillIssuerDetails)

#endif // OAIBillIssuerDetails_H
