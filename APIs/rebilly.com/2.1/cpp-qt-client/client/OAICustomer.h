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
 * OAICustomer.h
 *
 * 
 */

#ifndef OAICustomer_H
#define OAICustomer_H

#include <QJsonObject>

#include "OAIContactObject.h"
#include "OAICustomerAverageValue.h"
#include "OAICustomerLifetimeRevenue.h"
#include "OAICustomer__embedded_inner.h"
#include "OAICustomer__links_inner.h"
#include "OAIObject.h"
#include "OAIPaymentInstrument.h"
#include "OAITag.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomer__embedded_inner;
class OAICustomer__links_inner;
class OAICustomerAverageValue;
class OAIPaymentInstrument;
class OAICustomerLifetimeRevenue;
class OAIContactObject;
class OAITag;

class OAICustomer : public OAIObject {
public:
    OAICustomer();
    OAICustomer(QString json);
    ~OAICustomer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICustomer__embedded_inner> getEmbedded() const;
    void setEmbedded(const QList<OAICustomer__embedded_inner> &_embedded);
    bool is__embedded_Set() const;
    bool is__embedded_Valid() const;

    QList<OAICustomer__links_inner> getLinks() const;
    void setLinks(const QList<OAICustomer__links_inner> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    OAICustomerAverageValue getAverageValue() const;
    void setAverageValue(const OAICustomerAverageValue &average_value);
    bool is_average_value_Set() const;
    bool is_average_value_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    OAIPaymentInstrument getDefaultPaymentInstrument() const;
    void setDefaultPaymentInstrument(const OAIPaymentInstrument &default_payment_instrument);
    bool is_default_payment_instrument_Set() const;
    bool is_default_payment_instrument_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getInvoiceCount() const;
    void setInvoiceCount(const qint32 &invoice_count);
    bool is_invoice_count_Set() const;
    bool is_invoice_count_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QDateTime getLastPaymentTime() const;
    void setLastPaymentTime(const QDateTime &last_payment_time);
    bool is_last_payment_time_Set() const;
    bool is_last_payment_time_Valid() const;

    OAICustomerLifetimeRevenue getLifetimeRevenue() const;
    void setLifetimeRevenue(const OAICustomerLifetimeRevenue &lifetime_revenue);
    bool is_lifetime_revenue_Set() const;
    bool is_lifetime_revenue_Valid() const;

    qint32 getPaymentCount() const;
    void setPaymentCount(const qint32 &payment_count);
    bool is_payment_count_Set() const;
    bool is_payment_count_Valid() const;

    QString getPaymentToken() const;
    void setPaymentToken(const QString &payment_token);
    bool is_payment_token_Set() const;
    bool is_payment_token_Valid() const;

    OAIContactObject getPrimaryAddress() const;
    void setPrimaryAddress(const OAIContactObject &primary_address);
    bool is_primary_address_Set() const;
    bool is_primary_address_Valid() const;

    qint32 getRevision() const;
    void setRevision(const qint32 &revision);
    bool is_revision_Set() const;
    bool is_revision_Valid() const;

    QList<OAITag> getTags() const;
    void setTags(const QList<OAITag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QDateTime getUpdatedTime() const;
    void setUpdatedTime(const QDateTime &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    QString getWebsiteId() const;
    void setWebsiteId(const QString &website_id);
    bool is_website_id_Set() const;
    bool is_website_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICustomer__embedded_inner> m__embedded;
    bool m__embedded_isSet;
    bool m__embedded_isValid;

    QList<OAICustomer__links_inner> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    OAICustomerAverageValue m_average_value;
    bool m_average_value_isSet;
    bool m_average_value_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    OAIPaymentInstrument m_default_payment_instrument;
    bool m_default_payment_instrument_isSet;
    bool m_default_payment_instrument_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_invoice_count;
    bool m_invoice_count_isSet;
    bool m_invoice_count_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QDateTime m_last_payment_time;
    bool m_last_payment_time_isSet;
    bool m_last_payment_time_isValid;

    OAICustomerLifetimeRevenue m_lifetime_revenue;
    bool m_lifetime_revenue_isSet;
    bool m_lifetime_revenue_isValid;

    qint32 m_payment_count;
    bool m_payment_count_isSet;
    bool m_payment_count_isValid;

    QString m_payment_token;
    bool m_payment_token_isSet;
    bool m_payment_token_isValid;

    OAIContactObject m_primary_address;
    bool m_primary_address_isSet;
    bool m_primary_address_isValid;

    qint32 m_revision;
    bool m_revision_isSet;
    bool m_revision_isValid;

    QList<OAITag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QDateTime m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    QString m_website_id;
    bool m_website_id_isSet;
    bool m_website_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomer)

#endif // OAICustomer_H
