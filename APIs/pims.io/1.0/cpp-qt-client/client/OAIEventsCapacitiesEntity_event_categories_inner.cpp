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

#include "OAIEventsCapacitiesEntity_event_categories_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEventsCapacitiesEntity_event_categories_inner::OAIEventsCapacitiesEntity_event_categories_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEventsCapacitiesEntity_event_categories_inner::OAIEventsCapacitiesEntity_event_categories_inner() {
    this->initializeModel();
}

OAIEventsCapacitiesEntity_event_categories_inner::~OAIEventsCapacitiesEntity_event_categories_inner() {}

void OAIEventsCapacitiesEntity_event_categories_inner::initializeModel() {

    m_comps_isSet = false;
    m_comps_isValid = false;

    m_holds_isSet = false;
    m_holds_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_kills_isSet = false;
    m_kills_isValid = false;

    m_sellable_capacity_isSet = false;
    m_sellable_capacity_isValid = false;

    m_total_capacity_isSet = false;
    m_total_capacity_isValid = false;
}

void OAIEventsCapacitiesEntity_event_categories_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEventsCapacitiesEntity_event_categories_inner::fromJsonObject(QJsonObject json) {

    m_comps_isValid = ::OpenAPI::fromJsonValue(m_comps, json[QString("comps")]);
    m_comps_isSet = !json[QString("comps")].isNull() && m_comps_isValid;

    m_holds_isValid = ::OpenAPI::fromJsonValue(m_holds, json[QString("holds")]);
    m_holds_isSet = !json[QString("holds")].isNull() && m_holds_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_kills_isValid = ::OpenAPI::fromJsonValue(m_kills, json[QString("kills")]);
    m_kills_isSet = !json[QString("kills")].isNull() && m_kills_isValid;

    m_sellable_capacity_isValid = ::OpenAPI::fromJsonValue(m_sellable_capacity, json[QString("sellable_capacity")]);
    m_sellable_capacity_isSet = !json[QString("sellable_capacity")].isNull() && m_sellable_capacity_isValid;

    m_total_capacity_isValid = ::OpenAPI::fromJsonValue(m_total_capacity, json[QString("total_capacity")]);
    m_total_capacity_isSet = !json[QString("total_capacity")].isNull() && m_total_capacity_isValid;
}

QString OAIEventsCapacitiesEntity_event_categories_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEventsCapacitiesEntity_event_categories_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_comps_isSet) {
        obj.insert(QString("comps"), ::OpenAPI::toJsonValue(m_comps));
    }
    if (m_holds_isSet) {
        obj.insert(QString("holds"), ::OpenAPI::toJsonValue(m_holds));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_kills_isSet) {
        obj.insert(QString("kills"), ::OpenAPI::toJsonValue(m_kills));
    }
    if (m_sellable_capacity_isSet) {
        obj.insert(QString("sellable_capacity"), ::OpenAPI::toJsonValue(m_sellable_capacity));
    }
    if (m_total_capacity_isSet) {
        obj.insert(QString("total_capacity"), ::OpenAPI::toJsonValue(m_total_capacity));
    }
    return obj;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getComps() const {
    return m_comps;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setComps(const qint32 &comps) {
    m_comps = comps;
    m_comps_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_comps_Set() const{
    return m_comps_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_comps_Valid() const{
    return m_comps_isValid;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getHolds() const {
    return m_holds;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setHolds(const qint32 &holds) {
    m_holds = holds;
    m_holds_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_holds_Set() const{
    return m_holds_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_holds_Valid() const{
    return m_holds_isValid;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getId() const {
    return m_id;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getKills() const {
    return m_kills;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setKills(const qint32 &kills) {
    m_kills = kills;
    m_kills_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_kills_Set() const{
    return m_kills_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_kills_Valid() const{
    return m_kills_isValid;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getSellableCapacity() const {
    return m_sellable_capacity;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setSellableCapacity(const qint32 &sellable_capacity) {
    m_sellable_capacity = sellable_capacity;
    m_sellable_capacity_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_sellable_capacity_Set() const{
    return m_sellable_capacity_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_sellable_capacity_Valid() const{
    return m_sellable_capacity_isValid;
}

qint32 OAIEventsCapacitiesEntity_event_categories_inner::getTotalCapacity() const {
    return m_total_capacity;
}
void OAIEventsCapacitiesEntity_event_categories_inner::setTotalCapacity(const qint32 &total_capacity) {
    m_total_capacity = total_capacity;
    m_total_capacity_isSet = true;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_total_capacity_Set() const{
    return m_total_capacity_isSet;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::is_total_capacity_Valid() const{
    return m_total_capacity_isValid;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_comps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_holds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kills_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sellable_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEventsCapacitiesEntity_event_categories_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_comps_isValid && m_holds_isValid && m_id_isValid && m_kills_isValid && m_sellable_capacity_isValid && m_total_capacity_isValid && true;
}

} // namespace OpenAPI
