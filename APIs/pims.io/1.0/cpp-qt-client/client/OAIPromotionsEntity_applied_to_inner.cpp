/**
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPromotionsEntity_applied_to_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPromotionsEntity_applied_to_inner::OAIPromotionsEntity_applied_to_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPromotionsEntity_applied_to_inner::OAIPromotionsEntity_applied_to_inner() {
    this->initializeModel();
}

OAIPromotionsEntity_applied_to_inner::~OAIPromotionsEntity_applied_to_inner() {}

void OAIPromotionsEntity_applied_to_inner::initializeModel() {

    m_event_id_isSet = false;
    m_event_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_series_id_isSet = false;
    m_series_id_isValid = false;

    m_unit_cost_isSet = false;
    m_unit_cost_isValid = false;

    m_valorized_quantity_isSet = false;
    m_valorized_quantity_isValid = false;

    m_valorized_unit_cost_isSet = false;
    m_valorized_unit_cost_isValid = false;
}

void OAIPromotionsEntity_applied_to_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPromotionsEntity_applied_to_inner::fromJsonObject(QJsonObject json) {

    m_event_id_isValid = ::OpenAPI::fromJsonValue(m_event_id, json[QString("event_id")]);
    m_event_id_isSet = !json[QString("event_id")].isNull() && m_event_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_series_id_isValid = ::OpenAPI::fromJsonValue(m_series_id, json[QString("series_id")]);
    m_series_id_isSet = !json[QString("series_id")].isNull() && m_series_id_isValid;

    m_unit_cost_isValid = ::OpenAPI::fromJsonValue(m_unit_cost, json[QString("unit_cost")]);
    m_unit_cost_isSet = !json[QString("unit_cost")].isNull() && m_unit_cost_isValid;

    m_valorized_quantity_isValid = ::OpenAPI::fromJsonValue(m_valorized_quantity, json[QString("valorized_quantity")]);
    m_valorized_quantity_isSet = !json[QString("valorized_quantity")].isNull() && m_valorized_quantity_isValid;

    m_valorized_unit_cost_isValid = ::OpenAPI::fromJsonValue(m_valorized_unit_cost, json[QString("valorized_unit_cost")]);
    m_valorized_unit_cost_isSet = !json[QString("valorized_unit_cost")].isNull() && m_valorized_unit_cost_isValid;
}

QString OAIPromotionsEntity_applied_to_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPromotionsEntity_applied_to_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_event_id_isSet) {
        obj.insert(QString("event_id"), ::OpenAPI::toJsonValue(m_event_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_series_id_isSet) {
        obj.insert(QString("series_id"), ::OpenAPI::toJsonValue(m_series_id));
    }
    if (m_unit_cost_isSet) {
        obj.insert(QString("unit_cost"), ::OpenAPI::toJsonValue(m_unit_cost));
    }
    if (m_valorized_quantity_isSet) {
        obj.insert(QString("valorized_quantity"), ::OpenAPI::toJsonValue(m_valorized_quantity));
    }
    if (m_valorized_unit_cost_isSet) {
        obj.insert(QString("valorized_unit_cost"), ::OpenAPI::toJsonValue(m_valorized_unit_cost));
    }
    return obj;
}

qint32 OAIPromotionsEntity_applied_to_inner::getEventId() const {
    return m_event_id;
}
void OAIPromotionsEntity_applied_to_inner::setEventId(const qint32 &event_id) {
    m_event_id = event_id;
    m_event_id_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_event_id_Set() const{
    return m_event_id_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_event_id_Valid() const{
    return m_event_id_isValid;
}

float OAIPromotionsEntity_applied_to_inner::getQuantity() const {
    return m_quantity;
}
void OAIPromotionsEntity_applied_to_inner::setQuantity(const float &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

qint32 OAIPromotionsEntity_applied_to_inner::getSeriesId() const {
    return m_series_id;
}
void OAIPromotionsEntity_applied_to_inner::setSeriesId(const qint32 &series_id) {
    m_series_id = series_id;
    m_series_id_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_series_id_Set() const{
    return m_series_id_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_series_id_Valid() const{
    return m_series_id_isValid;
}

float OAIPromotionsEntity_applied_to_inner::getUnitCost() const {
    return m_unit_cost;
}
void OAIPromotionsEntity_applied_to_inner::setUnitCost(const float &unit_cost) {
    m_unit_cost = unit_cost;
    m_unit_cost_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_unit_cost_Set() const{
    return m_unit_cost_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_unit_cost_Valid() const{
    return m_unit_cost_isValid;
}

float OAIPromotionsEntity_applied_to_inner::getValorizedQuantity() const {
    return m_valorized_quantity;
}
void OAIPromotionsEntity_applied_to_inner::setValorizedQuantity(const float &valorized_quantity) {
    m_valorized_quantity = valorized_quantity;
    m_valorized_quantity_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_valorized_quantity_Set() const{
    return m_valorized_quantity_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_valorized_quantity_Valid() const{
    return m_valorized_quantity_isValid;
}

float OAIPromotionsEntity_applied_to_inner::getValorizedUnitCost() const {
    return m_valorized_unit_cost;
}
void OAIPromotionsEntity_applied_to_inner::setValorizedUnitCost(const float &valorized_unit_cost) {
    m_valorized_unit_cost = valorized_unit_cost;
    m_valorized_unit_cost_isSet = true;
}

bool OAIPromotionsEntity_applied_to_inner::is_valorized_unit_cost_Set() const{
    return m_valorized_unit_cost_isSet;
}

bool OAIPromotionsEntity_applied_to_inner::is_valorized_unit_cost_Valid() const{
    return m_valorized_unit_cost_isValid;
}

bool OAIPromotionsEntity_applied_to_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_event_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_series_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_cost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valorized_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valorized_unit_cost_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPromotionsEntity_applied_to_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
