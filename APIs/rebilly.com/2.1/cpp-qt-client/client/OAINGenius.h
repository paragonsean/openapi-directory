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
 * OAINGenius.h
 *
 * NGenius config.
 */

#ifndef OAINGenius_H
#define OAINGenius_H

#include <QJsonObject>

#include "OAIAcquirerName.h"
#include "OAIDigitalWallets.h"
#include "OAIGatewayAccount.h"
#include "OAIGatewayAccount__links_inner.h"
#include "OAIGatewayName.h"
#include "OAINGenius3dsServers.h"
#include "OAINGenius_allOf_credentials.h"
#include "OAIPaymentCardBrand.h"
#include "OAIPaymentMethod.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGatewayAccount__links_inner;
class OAIDigitalWallets;
class OAINGenius_allOf_credentials;
class OAINGenius3dsServers;

class OAINGenius : public OAIObject {
public:
    OAINGenius();
    OAINGenius(QString json);
    ~OAINGenius() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIGatewayAccount__links_inner> getLinks() const;
    void setLinks(const QList<OAIGatewayAccount__links_inner> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QList<QString> getAcceptedCurrencies() const;
    void setAcceptedCurrencies(const QList<QString> &accepted_currencies);
    bool is_accepted_currencies_Set() const;
    bool is_accepted_currencies_Valid() const;

    OAIAcquirerName getAcquirerName() const;
    void setAcquirerName(const OAIAcquirerName &acquirer_name);
    bool is_acquirer_name_Set() const;
    bool is_acquirer_name_Valid() const;

    QString getAdditionalFilters() const;
    void setAdditionalFilters(const QString &additional_filters);
    bool is_additional_filters_Set() const;
    bool is_additional_filters_Valid() const;

    qint32 getApprovalWindowTtl() const;
    void setApprovalWindowTtl(const qint32 &approval_window_ttl);
    bool is_approval_window_ttl_Set() const;
    bool is_approval_window_ttl_Valid() const;

    QString getCityField() const;
    void setCityField(const QString &city_field);
    bool is_city_field_Set() const;
    bool is_city_field_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QString getDccForceCurrency() const;
    void setDccForceCurrency(const QString &dcc_force_currency);
    bool is_dcc_force_currency_Set() const;
    bool is_dcc_force_currency_Valid() const;

    qint32 getDccMarkup() const;
    void setDccMarkup(const qint32 &dcc_markup);
    bool is_dcc_markup_Set() const;
    bool is_dcc_markup_Valid() const;

    QString getDescriptor() const;
    void setDescriptor(const QString &descriptor);
    bool is_descriptor_Set() const;
    bool is_descriptor_Valid() const;

    OAIDigitalWallets getDigitalWallets() const;
    void setDigitalWallets(const OAIDigitalWallets &digital_wallets);
    bool is_digital_wallets_Set() const;
    bool is_digital_wallets_Valid() const;

    bool isDynamicDescriptor() const;
    void setDynamicDescriptor(const bool &dynamic_descriptor);
    bool is_dynamic_descriptor_Set() const;
    bool is_dynamic_descriptor_Valid() const;

    QList<QString> getExcludedDccQuoteCurrencies() const;
    void setExcludedDccQuoteCurrencies(const QList<QString> &excluded_dcc_quote_currencies);
    bool is_excluded_dcc_quote_currencies_Set() const;
    bool is_excluded_dcc_quote_currencies_Valid() const;

    OAIGatewayName getGatewayName() const;
    void setGatewayName(const OAIGatewayName &gateway_name);
    bool is_gateway_name_Set() const;
    bool is_gateway_name_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsDown() const;
    void setIsDown(const bool &is_down);
    bool is_is_down_Set() const;
    bool is_is_down_Valid() const;

    QString getMerchantCategoryCode() const;
    void setMerchantCategoryCode(const QString &merchant_category_code);
    bool is_merchant_category_code_Set() const;
    bool is_merchant_category_code_Valid() const;

    OAIPaymentMethod getMethod() const;
    void setMethod(const OAIPaymentMethod &method);
    bool is_method_Set() const;
    bool is_method_Valid() const;

    double getMonthlyLimit() const;
    void setMonthlyLimit(const double &monthly_limit);
    bool is_monthly_limit_Set() const;
    bool is_monthly_limit_Valid() const;

    Q_DECL_DEPRECATED QString getOrganizationId() const;
    Q_DECL_DEPRECATED void setOrganizationId(const QString &organization_id);
    Q_DECL_DEPRECATED bool is_organization_id_Set() const;
    Q_DECL_DEPRECATED bool is_organization_id_Valid() const;

    QList<OAIPaymentCardBrand> getPaymentCardSchemes() const;
    void setPaymentCardSchemes(const QList<OAIPaymentCardBrand> &payment_card_schemes);
    bool is_payment_card_schemes_Set() const;
    bool is_payment_card_schemes_Valid() const;

    bool isReconciliationWindowEnabled() const;
    void setReconciliationWindowEnabled(const bool &reconciliation_window_enabled);
    bool is_reconciliation_window_enabled_Set() const;
    bool is_reconciliation_window_enabled_Valid() const;

    qint32 getReconciliationWindowTtl() const;
    void setReconciliationWindowTtl(const qint32 &reconciliation_window_ttl);
    bool is_reconciliation_window_ttl_Set() const;
    bool is_reconciliation_window_ttl_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    bool isSticky() const;
    void setSticky(const bool &sticky);
    bool is_sticky_Set() const;
    bool is_sticky_Valid() const;

    bool isThreeDSecure() const;
    void setThreeDSecure(const bool &three_d_secure);
    bool is_three_d_secure_Set() const;
    bool is_three_d_secure_Valid() const;

    qint32 getTimeout() const;
    void setTimeout(const qint32 &timeout);
    bool is_timeout_Set() const;
    bool is_timeout_Valid() const;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    QDateTime getUpdatedTime() const;
    void setUpdatedTime(const QDateTime &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    OAINGenius_allOf_credentials getCredentials() const;
    void setCredentials(const OAINGenius_allOf_credentials &credentials);
    bool is_credentials_Set() const;
    bool is_credentials_Valid() const;

    OAINGenius3dsServers getThreeDSecureServer() const;
    void setThreeDSecureServer(const OAINGenius3dsServers &three_d_secure_server);
    bool is_three_d_secure_server_Set() const;
    bool is_three_d_secure_server_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIGatewayAccount__links_inner> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QList<QString> m_accepted_currencies;
    bool m_accepted_currencies_isSet;
    bool m_accepted_currencies_isValid;

    OAIAcquirerName m_acquirer_name;
    bool m_acquirer_name_isSet;
    bool m_acquirer_name_isValid;

    QString m_additional_filters;
    bool m_additional_filters_isSet;
    bool m_additional_filters_isValid;

    qint32 m_approval_window_ttl;
    bool m_approval_window_ttl_isSet;
    bool m_approval_window_ttl_isValid;

    QString m_city_field;
    bool m_city_field_isSet;
    bool m_city_field_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QString m_dcc_force_currency;
    bool m_dcc_force_currency_isSet;
    bool m_dcc_force_currency_isValid;

    qint32 m_dcc_markup;
    bool m_dcc_markup_isSet;
    bool m_dcc_markup_isValid;

    QString m_descriptor;
    bool m_descriptor_isSet;
    bool m_descriptor_isValid;

    OAIDigitalWallets m_digital_wallets;
    bool m_digital_wallets_isSet;
    bool m_digital_wallets_isValid;

    bool m_dynamic_descriptor;
    bool m_dynamic_descriptor_isSet;
    bool m_dynamic_descriptor_isValid;

    QList<QString> m_excluded_dcc_quote_currencies;
    bool m_excluded_dcc_quote_currencies_isSet;
    bool m_excluded_dcc_quote_currencies_isValid;

    OAIGatewayName m_gateway_name;
    bool m_gateway_name_isSet;
    bool m_gateway_name_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_down;
    bool m_is_down_isSet;
    bool m_is_down_isValid;

    QString m_merchant_category_code;
    bool m_merchant_category_code_isSet;
    bool m_merchant_category_code_isValid;

    OAIPaymentMethod m_method;
    bool m_method_isSet;
    bool m_method_isValid;

    double m_monthly_limit;
    bool m_monthly_limit_isSet;
    bool m_monthly_limit_isValid;

    QString m_organization_id;
    bool m_organization_id_isSet;
    bool m_organization_id_isValid;

    QList<OAIPaymentCardBrand> m_payment_card_schemes;
    bool m_payment_card_schemes_isSet;
    bool m_payment_card_schemes_isValid;

    bool m_reconciliation_window_enabled;
    bool m_reconciliation_window_enabled_isSet;
    bool m_reconciliation_window_enabled_isValid;

    qint32 m_reconciliation_window_ttl;
    bool m_reconciliation_window_ttl_isSet;
    bool m_reconciliation_window_ttl_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    bool m_sticky;
    bool m_sticky_isSet;
    bool m_sticky_isValid;

    bool m_three_d_secure;
    bool m_three_d_secure_isSet;
    bool m_three_d_secure_isValid;

    qint32 m_timeout;
    bool m_timeout_isSet;
    bool m_timeout_isValid;

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;

    QDateTime m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    OAINGenius_allOf_credentials m_credentials;
    bool m_credentials_isSet;
    bool m_credentials_isValid;

    OAINGenius3dsServers m_three_d_secure_server;
    bool m_three_d_secure_server_isSet;
    bool m_three_d_secure_server_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINGenius)

#endif // OAINGenius_H
