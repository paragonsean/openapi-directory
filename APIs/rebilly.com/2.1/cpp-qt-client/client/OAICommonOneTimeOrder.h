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
 * OAICommonOneTimeOrder.h
 *
 * 
 */

#ifndef OAICommonOneTimeOrder_H
#define OAICommonOneTimeOrder_H

#include <QJsonObject>

#include "OAICommonSubscription_items_inner.h"
#include "OAIContactObject.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContactObject;
class OAICommonSubscription_items_inner;

class OAICommonOneTimeOrder : public OAIObject {
public:
    OAICommonOneTimeOrder();
    OAICommonOneTimeOrder(QString json);
    ~OAICommonOneTimeOrder() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getActivationTime() const;
    void setActivationTime(const QDateTime &activation_time);
    bool is_activation_time_Set() const;
    bool is_activation_time_Valid() const;

    OAIContactObject getBillingAddress() const;
    void setBillingAddress(const OAIContactObject &billing_address);
    bool is_billing_address_Set() const;
    bool is_billing_address_Valid() const;

    QString getBillingStatus() const;
    void setBillingStatus(const QString &billing_status);
    bool is_billing_status_Set() const;
    bool is_billing_status_Valid() const;

    QList<QString> getCouponIds() const;
    void setCouponIds(const QList<QString> &coupon_ids);
    bool is_coupon_ids_Set() const;
    bool is_coupon_ids_Valid() const;

    OAIContactObject getDeliveryAddress() const;
    void setDeliveryAddress(const OAIContactObject &delivery_address);
    bool is_delivery_address_Set() const;
    bool is_delivery_address_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInitialInvoiceId() const;
    void setInitialInvoiceId(const QString &initial_invoice_id);
    bool is_initial_invoice_id_Set() const;
    bool is_initial_invoice_id_Valid() const;

    QList<OAICommonSubscription_items_inner> getItems() const;
    void setItems(const QList<OAICommonSubscription_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getOrderType() const;
    void setOrderType(const QString &order_type);
    bool is_order_type_Set() const;
    bool is_order_type_Valid() const;

    QString getPoNumber() const;
    void setPoNumber(const QString &po_number);
    bool is_po_number_Set() const;
    bool is_po_number_Valid() const;

    QString getRecentInvoiceId() const;
    void setRecentInvoiceId(const QString &recent_invoice_id);
    bool is_recent_invoice_id_Set() const;
    bool is_recent_invoice_id_Valid() const;

    QDateTime getVoidTime() const;
    void setVoidTime(const QDateTime &void_time);
    bool is_void_time_Set() const;
    bool is_void_time_Valid() const;

    QString getWebsiteId() const;
    void setWebsiteId(const QString &website_id);
    bool is_website_id_Set() const;
    bool is_website_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_activation_time;
    bool m_activation_time_isSet;
    bool m_activation_time_isValid;

    OAIContactObject m_billing_address;
    bool m_billing_address_isSet;
    bool m_billing_address_isValid;

    QString m_billing_status;
    bool m_billing_status_isSet;
    bool m_billing_status_isValid;

    QList<QString> m_coupon_ids;
    bool m_coupon_ids_isSet;
    bool m_coupon_ids_isValid;

    OAIContactObject m_delivery_address;
    bool m_delivery_address_isSet;
    bool m_delivery_address_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_initial_invoice_id;
    bool m_initial_invoice_id_isSet;
    bool m_initial_invoice_id_isValid;

    QList<OAICommonSubscription_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_order_type;
    bool m_order_type_isSet;
    bool m_order_type_isValid;

    QString m_po_number;
    bool m_po_number_isSet;
    bool m_po_number_isValid;

    QString m_recent_invoice_id;
    bool m_recent_invoice_id_isSet;
    bool m_recent_invoice_id_isValid;

    QDateTime m_void_time;
    bool m_void_time_isSet;
    bool m_void_time_isValid;

    QString m_website_id;
    bool m_website_id_isSet;
    bool m_website_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICommonOneTimeOrder)

#endif // OAICommonOneTimeOrder_H
