/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPaymentCard.h
 *
 * 
 */

#ifndef OAIPaymentCard_H
#define OAIPaymentCard_H

#include <QJsonObject>

#include "OAIContactObject.h"
#include "OAIObject.h"
#include "OAIPaymentCardBrand.h"
#include "OAIPaymentCard_allOf__embedded.h"
#include "OAIPaymentCard_allOf__links.h"
#include "OAIRiskMetadata.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContactObject;
class OAIRiskMetadata;
class OAIPaymentCard_allOf__embedded;
class OAIPaymentCard_allOf__links;

class OAIPaymentCard : public OAIObject {
public:
    OAIPaymentCard();
    OAIPaymentCard(QString json);
    ~OAIPaymentCard() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBankCountry() const;
    void setBankCountry(const QString &bank_country);
    bool is_bank_country_Set() const;
    bool is_bank_country_Valid() const;

    QString getBankName() const;
    void setBankName(const QString &bank_name);
    bool is_bank_name_Set() const;
    bool is_bank_name_Valid() const;

    OAIContactObject getBillingAddress() const;
    void setBillingAddress(const OAIContactObject &billing_address);
    bool is_billing_address_Set() const;
    bool is_billing_address_Valid() const;

    QString getBin() const;
    void setBin(const QString &bin);
    bool is_bin_Set() const;
    bool is_bin_Valid() const;

    OAIPaymentCardBrand getBrand() const;
    void setBrand(const OAIPaymentCardBrand &brand);
    bool is_brand_Set() const;
    bool is_brand_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getCustomerId() const;
    void setCustomerId(const QString &customer_id);
    bool is_customer_id_Set() const;
    bool is_customer_id_Valid() const;

    QString getCvv() const;
    void setCvv(const QString &cvv);
    bool is_cvv_Set() const;
    bool is_cvv_Valid() const;

    qint32 getExpMonth() const;
    void setExpMonth(const qint32 &exp_month);
    bool is_exp_month_Set() const;
    bool is_exp_month_Valid() const;

    qint32 getExpYear() const;
    void setExpYear(const qint32 &exp_year);
    bool is_exp_year_Set() const;
    bool is_exp_year_Valid() const;

    QString getFingerprint() const;
    void setFingerprint(const QString &fingerprint);
    bool is_fingerprint_Set() const;
    bool is_fingerprint_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLast4() const;
    void setLast4(const QString &last4);
    bool is_last4_Set() const;
    bool is_last4_Valid() const;

    QString getMethod() const;
    void setMethod(const QString &method);
    bool is_method_Set() const;
    bool is_method_Valid() const;

    QString getPan() const;
    void setPan(const QString &pan);
    bool is_pan_Set() const;
    bool is_pan_Valid() const;

    OAIRiskMetadata getRiskMetadata() const;
    void setRiskMetadata(const OAIRiskMetadata &risk_metadata);
    bool is_risk_metadata_Set() const;
    bool is_risk_metadata_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QDateTime getUpdatedTime() const;
    void setUpdatedTime(const QDateTime &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    QList<OAIPaymentCard_allOf__embedded> getEmbedded() const;
    void setEmbedded(const QList<OAIPaymentCard_allOf__embedded> &_embedded);
    bool is__embedded_Set() const;
    bool is__embedded_Valid() const;

    QList<OAIPaymentCard_allOf__links> getLinks() const;
    void setLinks(const QList<OAIPaymentCard_allOf__links> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    qint32 getExpirationReminderNumber() const;
    void setExpirationReminderNumber(const qint32 &expiration_reminder_number);
    bool is_expiration_reminder_number_Set() const;
    bool is_expiration_reminder_number_Valid() const;

    QDateTime getExpirationReminderTime() const;
    void setExpirationReminderTime(const QDateTime &expiration_reminder_time);
    bool is_expiration_reminder_time_Set() const;
    bool is_expiration_reminder_time_Valid() const;

    QString getStickyGatewayAccountId() const;
    void setStickyGatewayAccountId(const QString &sticky_gateway_account_id);
    bool is_sticky_gateway_account_id_Set() const;
    bool is_sticky_gateway_account_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_bank_country;
    bool m_bank_country_isSet;
    bool m_bank_country_isValid;

    QString m_bank_name;
    bool m_bank_name_isSet;
    bool m_bank_name_isValid;

    OAIContactObject m_billing_address;
    bool m_billing_address_isSet;
    bool m_billing_address_isValid;

    QString m_bin;
    bool m_bin_isSet;
    bool m_bin_isValid;

    OAIPaymentCardBrand m_brand;
    bool m_brand_isSet;
    bool m_brand_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_customer_id;
    bool m_customer_id_isSet;
    bool m_customer_id_isValid;

    QString m_cvv;
    bool m_cvv_isSet;
    bool m_cvv_isValid;

    qint32 m_exp_month;
    bool m_exp_month_isSet;
    bool m_exp_month_isValid;

    qint32 m_exp_year;
    bool m_exp_year_isSet;
    bool m_exp_year_isValid;

    QString m_fingerprint;
    bool m_fingerprint_isSet;
    bool m_fingerprint_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last4;
    bool m_last4_isSet;
    bool m_last4_isValid;

    QString m_method;
    bool m_method_isSet;
    bool m_method_isValid;

    QString m_pan;
    bool m_pan_isSet;
    bool m_pan_isValid;

    OAIRiskMetadata m_risk_metadata;
    bool m_risk_metadata_isSet;
    bool m_risk_metadata_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QDateTime m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    QList<OAIPaymentCard_allOf__embedded> m__embedded;
    bool m__embedded_isSet;
    bool m__embedded_isValid;

    QList<OAIPaymentCard_allOf__links> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    qint32 m_expiration_reminder_number;
    bool m_expiration_reminder_number_isSet;
    bool m_expiration_reminder_number_isValid;

    QDateTime m_expiration_reminder_time;
    bool m_expiration_reminder_time_isSet;
    bool m_expiration_reminder_time_isValid;

    QString m_sticky_gateway_account_id;
    bool m_sticky_gateway_account_id_isSet;
    bool m_sticky_gateway_account_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPaymentCard)

#endif // OAIPaymentCard_H
