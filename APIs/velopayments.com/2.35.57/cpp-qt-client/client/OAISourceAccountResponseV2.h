/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISourceAccountResponseV2.h
 *
 * 
 */

#ifndef OAISourceAccountResponseV2_H
#define OAISourceAccountResponseV2_H

#include <QJsonObject>

#include "OAIAutoTopUpConfigV2.h"
#include "OAINotificationsV2.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAutoTopUpConfigV2;
class OAINotificationsV2;

class OAISourceAccountResponseV2 : public OAIObject {
public:
    OAISourceAccountResponseV2();
    OAISourceAccountResponseV2(QString json);
    ~OAISourceAccountResponseV2() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountType() const;
    void setAccountType(const QString &account_type);
    bool is_account_type_Set() const;
    bool is_account_type_Valid() const;

    OAIAutoTopUpConfigV2 getAutoTopUpConfig() const;
    void setAutoTopUpConfig(const OAIAutoTopUpConfigV2 &auto_top_up_config);
    bool is_auto_top_up_config_Set() const;
    bool is_auto_top_up_config_Valid() const;

    qint64 getBalance() const;
    void setBalance(const qint64 &balance);
    bool is_balance_Set() const;
    bool is_balance_Valid() const;

    bool isBalanceVisible() const;
    void setBalanceVisible(const bool &balance_visible);
    bool is_balance_visible_Set() const;
    bool is_balance_visible_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QString getCustomerId() const;
    void setCustomerId(const QString &customer_id);
    bool is_customer_id_Set() const;
    bool is_customer_id_Valid() const;

    QString getFundingAccountId() const;
    void setFundingAccountId(const QString &funding_account_id);
    bool is_funding_account_id_Set() const;
    bool is_funding_account_id_Valid() const;

    QString getFundingRef() const;
    void setFundingRef(const QString &funding_ref);
    bool is_funding_ref_Set() const;
    bool is_funding_ref_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAINotificationsV2 getNotifications() const;
    void setNotifications(const OAINotificationsV2 &notifications);
    bool is_notifications_Set() const;
    bool is_notifications_Valid() const;

    QString getPayorId() const;
    void setPayorId(const QString &payor_id);
    bool is_payor_id_Set() const;
    bool is_payor_id_Valid() const;

    QString getPhysicalAccountId() const;
    void setPhysicalAccountId(const QString &physical_account_id);
    bool is_physical_account_id_Set() const;
    bool is_physical_account_id_Valid() const;

    QString getPhysicalAccountName() const;
    void setPhysicalAccountName(const QString &physical_account_name);
    bool is_physical_account_name_Set() const;
    bool is_physical_account_name_Valid() const;

    bool isPooled() const;
    void setPooled(const bool &pooled);
    bool is_pooled_Set() const;
    bool is_pooled_Valid() const;

    QString getRailsId() const;
    void setRailsId(const QString &rails_id);
    bool is_rails_id_Set() const;
    bool is_rails_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_type;
    bool m_account_type_isSet;
    bool m_account_type_isValid;

    OAIAutoTopUpConfigV2 m_auto_top_up_config;
    bool m_auto_top_up_config_isSet;
    bool m_auto_top_up_config_isValid;

    qint64 m_balance;
    bool m_balance_isSet;
    bool m_balance_isValid;

    bool m_balance_visible;
    bool m_balance_visible_isSet;
    bool m_balance_visible_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QString m_customer_id;
    bool m_customer_id_isSet;
    bool m_customer_id_isValid;

    QString m_funding_account_id;
    bool m_funding_account_id_isSet;
    bool m_funding_account_id_isValid;

    QString m_funding_ref;
    bool m_funding_ref_isSet;
    bool m_funding_ref_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAINotificationsV2 m_notifications;
    bool m_notifications_isSet;
    bool m_notifications_isValid;

    QString m_payor_id;
    bool m_payor_id_isSet;
    bool m_payor_id_isValid;

    QString m_physical_account_id;
    bool m_physical_account_id_isSet;
    bool m_physical_account_id_isValid;

    QString m_physical_account_name;
    bool m_physical_account_name_isSet;
    bool m_physical_account_name_isValid;

    bool m_pooled;
    bool m_pooled_isSet;
    bool m_pooled_isValid;

    QString m_rails_id;
    bool m_rails_id_isSet;
    bool m_rails_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISourceAccountResponseV2)

#endif // OAISourceAccountResponseV2_H
