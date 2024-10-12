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
 * OAIFailedPayeeV3.h
 *
 * 
 */

#ifndef OAIFailedPayeeV3_H
#define OAIFailedPayeeV3_H

#include <QJsonObject>

#include "OAIChallengeV3.h"
#include "OAICompanyV3.h"
#include "OAICreateIndividualV3.h"
#include "OAICreatePayeeAddressV3.h"
#include "OAICreatePaymentChannelV3.h"
#include "OAIPayeePayorRefV3.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreatePayeeAddressV3;
class OAIChallengeV3;
class OAICompanyV3;
class OAICreateIndividualV3;
class OAICreatePaymentChannelV3;
class OAIPayeePayorRefV3;

class OAIFailedPayeeV3 : public OAIObject {
public:
    OAIFailedPayeeV3();
    OAIFailedPayeeV3(QString json);
    ~OAIFailedPayeeV3() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICreatePayeeAddressV3 getAddress() const;
    void setAddress(const OAICreatePayeeAddressV3 &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    OAIChallengeV3 getChallenge() const;
    void setChallenge(const OAIChallengeV3 &challenge);
    bool is_challenge_Set() const;
    bool is_challenge_Valid() const;

    OAICompanyV3 getCompany() const;
    void setCompany(const OAICompanyV3 &company);
    bool is_company_Set() const;
    bool is_company_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    OAICreateIndividualV3 getIndividual() const;
    void setIndividual(const OAICreateIndividualV3 &individual);
    bool is_individual_Set() const;
    bool is_individual_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    QString getPayeeId() const;
    void setPayeeId(const QString &payee_id);
    bool is_payee_id_Set() const;
    bool is_payee_id_Valid() const;

    OAICreatePaymentChannelV3 getPaymentChannel() const;
    void setPaymentChannel(const OAICreatePaymentChannelV3 &payment_channel);
    bool is_payment_channel_Set() const;
    bool is_payment_channel_Valid() const;

    QList<OAIPayeePayorRefV3> getPayorRefs() const;
    void setPayorRefs(const QList<OAIPayeePayorRefV3> &payor_refs);
    bool is_payor_refs_Set() const;
    bool is_payor_refs_Valid() const;

    QString getRemoteId() const;
    void setRemoteId(const QString &remote_id);
    bool is_remote_id_Set() const;
    bool is_remote_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICreatePayeeAddressV3 m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    OAIChallengeV3 m_challenge;
    bool m_challenge_isSet;
    bool m_challenge_isValid;

    OAICompanyV3 m_company;
    bool m_company_isSet;
    bool m_company_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    OAICreateIndividualV3 m_individual;
    bool m_individual_isSet;
    bool m_individual_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_payee_id;
    bool m_payee_id_isSet;
    bool m_payee_id_isValid;

    OAICreatePaymentChannelV3 m_payment_channel;
    bool m_payment_channel_isSet;
    bool m_payment_channel_isValid;

    QList<OAIPayeePayorRefV3> m_payor_refs;
    bool m_payor_refs_isSet;
    bool m_payor_refs_isValid;

    QString m_remote_id;
    bool m_remote_id_isSet;
    bool m_remote_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFailedPayeeV3)

#endif // OAIFailedPayeeV3_H
