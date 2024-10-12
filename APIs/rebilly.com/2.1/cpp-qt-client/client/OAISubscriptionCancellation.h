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
 * OAISubscriptionCancellation.h
 *
 * 
 */

#ifndef OAISubscriptionCancellation_H
#define OAISubscriptionCancellation_H

#include <QJsonObject>

#include "OAISelfLink.h"
#include "OAIUpcomingInvoiceItem.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISelfLink;
class OAIUpcomingInvoiceItem;

class OAISubscriptionCancellation : public OAIObject {
public:
    OAISubscriptionCancellation();
    OAISubscriptionCancellation(QString json);
    ~OAISubscriptionCancellation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISelfLink> getLinks() const;
    void setLinks(const QList<OAISelfLink> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QString getAppliedInvoiceId() const;
    void setAppliedInvoiceId(const QString &applied_invoice_id);
    bool is_applied_invoice_id_Set() const;
    bool is_applied_invoice_id_Valid() const;

    QString getCanceledBy() const;
    void setCanceledBy(const QString &canceled_by);
    bool is_canceled_by_Set() const;
    bool is_canceled_by_Valid() const;

    QDateTime getCanceledTime() const;
    void setCanceledTime(const QDateTime &canceled_time);
    bool is_canceled_time_Set() const;
    bool is_canceled_time_Valid() const;

    QDateTime getChurnTime() const;
    void setChurnTime(const QDateTime &churn_time);
    bool is_churn_time_Set() const;
    bool is_churn_time_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    double getLineItemSubtotal() const;
    void setLineItemSubtotal(const double &line_item_subtotal);
    bool is_line_item_subtotal_Set() const;
    bool is_line_item_subtotal_Valid() const;

    QList<OAIUpcomingInvoiceItem> getLineItems() const;
    void setLineItems(const QList<OAIUpcomingInvoiceItem> &line_items);
    bool is_line_items_Set() const;
    bool is_line_items_Valid() const;

    bool isProrated() const;
    void setProrated(const bool &prorated);
    bool is_prorated_Set() const;
    bool is_prorated_Valid() const;

    QString getProratedInvoiceId() const;
    void setProratedInvoiceId(const QString &prorated_invoice_id);
    bool is_prorated_invoice_id_Set() const;
    bool is_prorated_invoice_id_Valid() const;

    QString getReason() const;
    void setReason(const QString &reason);
    bool is_reason_Set() const;
    bool is_reason_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getSubscriptionId() const;
    void setSubscriptionId(const QString &subscription_id);
    bool is_subscription_id_Set() const;
    bool is_subscription_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISelfLink> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QString m_applied_invoice_id;
    bool m_applied_invoice_id_isSet;
    bool m_applied_invoice_id_isValid;

    QString m_canceled_by;
    bool m_canceled_by_isSet;
    bool m_canceled_by_isValid;

    QDateTime m_canceled_time;
    bool m_canceled_time_isSet;
    bool m_canceled_time_isValid;

    QDateTime m_churn_time;
    bool m_churn_time_isSet;
    bool m_churn_time_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    double m_line_item_subtotal;
    bool m_line_item_subtotal_isSet;
    bool m_line_item_subtotal_isValid;

    QList<OAIUpcomingInvoiceItem> m_line_items;
    bool m_line_items_isSet;
    bool m_line_items_isValid;

    bool m_prorated;
    bool m_prorated_isSet;
    bool m_prorated_isValid;

    QString m_prorated_invoice_id;
    bool m_prorated_invoice_id_isSet;
    bool m_prorated_invoice_id_isValid;

    QString m_reason;
    bool m_reason_isSet;
    bool m_reason_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_subscription_id;
    bool m_subscription_id_isSet;
    bool m_subscription_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISubscriptionCancellation)

#endif // OAISubscriptionCancellation_H
