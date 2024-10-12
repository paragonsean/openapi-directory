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

#include "OAILeadSource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILeadSource::OAILeadSource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILeadSource::OAILeadSource() {
    this->initializeModel();
}

OAILeadSource::~OAILeadSource() {}

void OAILeadSource::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_affiliate_isSet = false;
    m_affiliate_isValid = false;

    m_campaign_isSet = false;
    m_campaign_isValid = false;

    m_click_id_isSet = false;
    m_click_id_isValid = false;

    m_content_isSet = false;
    m_content_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_medium_isSet = false;
    m_medium_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_referrer_isSet = false;
    m_referrer_isValid = false;

    m_sales_agent_isSet = false;
    m_sales_agent_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_sub_affiliate_isSet = false;
    m_sub_affiliate_isValid = false;

    m_term_isSet = false;
    m_term_isValid = false;

    m_original_isSet = false;
    m_original_isValid = false;
}

void OAILeadSource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILeadSource::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_affiliate_isValid = ::OpenAPI::fromJsonValue(m_affiliate, json[QString("affiliate")]);
    m_affiliate_isSet = !json[QString("affiliate")].isNull() && m_affiliate_isValid;

    m_campaign_isValid = ::OpenAPI::fromJsonValue(m_campaign, json[QString("campaign")]);
    m_campaign_isSet = !json[QString("campaign")].isNull() && m_campaign_isValid;

    m_click_id_isValid = ::OpenAPI::fromJsonValue(m_click_id, json[QString("clickId")]);
    m_click_id_isSet = !json[QString("clickId")].isNull() && m_click_id_isValid;

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_medium_isValid = ::OpenAPI::fromJsonValue(m_medium, json[QString("medium")]);
    m_medium_isSet = !json[QString("medium")].isNull() && m_medium_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_referrer_isValid = ::OpenAPI::fromJsonValue(m_referrer, json[QString("referrer")]);
    m_referrer_isSet = !json[QString("referrer")].isNull() && m_referrer_isValid;

    m_sales_agent_isValid = ::OpenAPI::fromJsonValue(m_sales_agent, json[QString("salesAgent")]);
    m_sales_agent_isSet = !json[QString("salesAgent")].isNull() && m_sales_agent_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_sub_affiliate_isValid = ::OpenAPI::fromJsonValue(m_sub_affiliate, json[QString("subAffiliate")]);
    m_sub_affiliate_isSet = !json[QString("subAffiliate")].isNull() && m_sub_affiliate_isValid;

    m_term_isValid = ::OpenAPI::fromJsonValue(m_term, json[QString("term")]);
    m_term_isSet = !json[QString("term")].isNull() && m_term_isValid;

    m_original_isValid = ::OpenAPI::fromJsonValue(m_original, json[QString("original")]);
    m_original_isSet = !json[QString("original")].isNull() && m_original_isValid;
}

QString OAILeadSource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILeadSource::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_affiliate_isSet) {
        obj.insert(QString("affiliate"), ::OpenAPI::toJsonValue(m_affiliate));
    }
    if (m_campaign_isSet) {
        obj.insert(QString("campaign"), ::OpenAPI::toJsonValue(m_campaign));
    }
    if (m_click_id_isSet) {
        obj.insert(QString("clickId"), ::OpenAPI::toJsonValue(m_click_id));
    }
    if (m_content_isSet) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_medium_isSet) {
        obj.insert(QString("medium"), ::OpenAPI::toJsonValue(m_medium));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_referrer_isSet) {
        obj.insert(QString("referrer"), ::OpenAPI::toJsonValue(m_referrer));
    }
    if (m_sales_agent_isSet) {
        obj.insert(QString("salesAgent"), ::OpenAPI::toJsonValue(m_sales_agent));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_sub_affiliate_isSet) {
        obj.insert(QString("subAffiliate"), ::OpenAPI::toJsonValue(m_sub_affiliate));
    }
    if (m_term_isSet) {
        obj.insert(QString("term"), ::OpenAPI::toJsonValue(m_term));
    }
    if (m_original.isSet()) {
        obj.insert(QString("original"), ::OpenAPI::toJsonValue(m_original));
    }
    return obj;
}

QList<OAIBankAccount_allOf__links> OAILeadSource::getLinks() const {
    return m__links;
}
void OAILeadSource::setLinks(const QList<OAIBankAccount_allOf__links> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAILeadSource::is__links_Set() const{
    return m__links_isSet;
}

bool OAILeadSource::is__links_Valid() const{
    return m__links_isValid;
}

QString OAILeadSource::getAffiliate() const {
    return m_affiliate;
}
void OAILeadSource::setAffiliate(const QString &affiliate) {
    m_affiliate = affiliate;
    m_affiliate_isSet = true;
}

bool OAILeadSource::is_affiliate_Set() const{
    return m_affiliate_isSet;
}

bool OAILeadSource::is_affiliate_Valid() const{
    return m_affiliate_isValid;
}

QString OAILeadSource::getCampaign() const {
    return m_campaign;
}
void OAILeadSource::setCampaign(const QString &campaign) {
    m_campaign = campaign;
    m_campaign_isSet = true;
}

bool OAILeadSource::is_campaign_Set() const{
    return m_campaign_isSet;
}

bool OAILeadSource::is_campaign_Valid() const{
    return m_campaign_isValid;
}

QString OAILeadSource::getClickId() const {
    return m_click_id;
}
void OAILeadSource::setClickId(const QString &click_id) {
    m_click_id = click_id;
    m_click_id_isSet = true;
}

bool OAILeadSource::is_click_id_Set() const{
    return m_click_id_isSet;
}

bool OAILeadSource::is_click_id_Valid() const{
    return m_click_id_isValid;
}

QString OAILeadSource::getContent() const {
    return m_content;
}
void OAILeadSource::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAILeadSource::is_content_Set() const{
    return m_content_isSet;
}

bool OAILeadSource::is_content_Valid() const{
    return m_content_isValid;
}

QDateTime OAILeadSource::getCreatedTime() const {
    return m_created_time;
}
void OAILeadSource::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAILeadSource::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAILeadSource::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAILeadSource::getMedium() const {
    return m_medium;
}
void OAILeadSource::setMedium(const QString &medium) {
    m_medium = medium;
    m_medium_isSet = true;
}

bool OAILeadSource::is_medium_Set() const{
    return m_medium_isSet;
}

bool OAILeadSource::is_medium_Valid() const{
    return m_medium_isValid;
}

QString OAILeadSource::getPath() const {
    return m_path;
}
void OAILeadSource::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAILeadSource::is_path_Set() const{
    return m_path_isSet;
}

bool OAILeadSource::is_path_Valid() const{
    return m_path_isValid;
}

QString OAILeadSource::getReferrer() const {
    return m_referrer;
}
void OAILeadSource::setReferrer(const QString &referrer) {
    m_referrer = referrer;
    m_referrer_isSet = true;
}

bool OAILeadSource::is_referrer_Set() const{
    return m_referrer_isSet;
}

bool OAILeadSource::is_referrer_Valid() const{
    return m_referrer_isValid;
}

QString OAILeadSource::getSalesAgent() const {
    return m_sales_agent;
}
void OAILeadSource::setSalesAgent(const QString &sales_agent) {
    m_sales_agent = sales_agent;
    m_sales_agent_isSet = true;
}

bool OAILeadSource::is_sales_agent_Set() const{
    return m_sales_agent_isSet;
}

bool OAILeadSource::is_sales_agent_Valid() const{
    return m_sales_agent_isValid;
}

QString OAILeadSource::getSource() const {
    return m_source;
}
void OAILeadSource::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAILeadSource::is_source_Set() const{
    return m_source_isSet;
}

bool OAILeadSource::is_source_Valid() const{
    return m_source_isValid;
}

QString OAILeadSource::getSubAffiliate() const {
    return m_sub_affiliate;
}
void OAILeadSource::setSubAffiliate(const QString &sub_affiliate) {
    m_sub_affiliate = sub_affiliate;
    m_sub_affiliate_isSet = true;
}

bool OAILeadSource::is_sub_affiliate_Set() const{
    return m_sub_affiliate_isSet;
}

bool OAILeadSource::is_sub_affiliate_Valid() const{
    return m_sub_affiliate_isValid;
}

QString OAILeadSource::getTerm() const {
    return m_term;
}
void OAILeadSource::setTerm(const QString &term) {
    m_term = term;
    m_term_isSet = true;
}

bool OAILeadSource::is_term_Set() const{
    return m_term_isSet;
}

bool OAILeadSource::is_term_Valid() const{
    return m_term_isValid;
}

OAILeadSourceData OAILeadSource::getOriginal() const {
    return m_original;
}
void OAILeadSource::setOriginal(const OAILeadSourceData &original) {
    m_original = original;
    m_original_isSet = true;
}

bool OAILeadSource::is_original_Set() const{
    return m_original_isSet;
}

bool OAILeadSource::is_original_Valid() const{
    return m_original_isValid;
}

bool OAILeadSource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_affiliate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_click_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_medium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referrer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_agent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_affiliate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_term_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILeadSource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
