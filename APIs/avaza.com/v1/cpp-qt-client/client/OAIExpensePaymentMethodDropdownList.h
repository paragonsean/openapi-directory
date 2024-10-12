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
 * OAIExpensePaymentMethodDropdownList.h
 *
 * 
 */

#ifndef OAIExpensePaymentMethodDropdownList_H
#define OAIExpensePaymentMethodDropdownList_H

#include <QJsonObject>

#include "OAIExpensePaymentMethodMinimal.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExpensePaymentMethodMinimal;

class OAIExpensePaymentMethodDropdownList : public OAIObject {
public:
    OAIExpensePaymentMethodDropdownList();
    OAIExpensePaymentMethodDropdownList(QString json);
    ~OAIExpensePaymentMethodDropdownList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIExpensePaymentMethodMinimal> getExpensePaymentMethods() const;
    void setExpensePaymentMethods(const QList<OAIExpensePaymentMethodMinimal> &expense_payment_methods);
    bool is_expense_payment_methods_Set() const;
    bool is_expense_payment_methods_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIExpensePaymentMethodMinimal> m_expense_payment_methods;
    bool m_expense_payment_methods_isSet;
    bool m_expense_payment_methods_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpensePaymentMethodDropdownList)

#endif // OAIExpensePaymentMethodDropdownList_H
