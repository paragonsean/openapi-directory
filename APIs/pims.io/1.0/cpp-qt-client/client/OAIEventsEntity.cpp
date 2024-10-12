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

#include "OAIEventsEntity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEventsEntity::OAIEventsEntity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEventsEntity::OAIEventsEntity() {
    this->initializeModel();
}

OAIEventsEntity::~OAIEventsEntity() {}

void OAIEventsEntity::initializeModel() {

    m_break_even_isSet = false;
    m_break_even_isValid = false;

    m_cancellation_date_isSet = false;
    m_cancellation_date_isValid = false;

    m_contract_isSet = false;
    m_contract_isValid = false;

    m_costing_capacity_isSet = false;
    m_costing_capacity_isValid = false;

    m_creation_timestamp_isSet = false;
    m_creation_timestamp_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_datetime_isSet = false;
    m_datetime_isValid = false;

    m_free_isSet = false;
    m_free_isValid = false;

    m_general_sales_date_isSet = false;
    m_general_sales_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_input_type_isSet = false;
    m_input_type_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_last_update_timestamp_isSet = false;
    m_last_update_timestamp_isValid = false;

    m_max_capacity_isSet = false;
    m_max_capacity_isValid = false;

    m_presales_date_isSet = false;
    m_presales_date_isValid = false;

    m_series_id_isSet = false;
    m_series_id_isValid = false;

    m_sold_out_date_isSet = false;
    m_sold_out_date_isValid = false;

    m_venue_isSet = false;
    m_venue_isValid = false;
}

void OAIEventsEntity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEventsEntity::fromJsonObject(QJsonObject json) {

    m_break_even_isValid = ::OpenAPI::fromJsonValue(m_break_even, json[QString("break_even")]);
    m_break_even_isSet = !json[QString("break_even")].isNull() && m_break_even_isValid;

    m_cancellation_date_isValid = ::OpenAPI::fromJsonValue(m_cancellation_date, json[QString("cancellation_date")]);
    m_cancellation_date_isSet = !json[QString("cancellation_date")].isNull() && m_cancellation_date_isValid;

    m_contract_isValid = ::OpenAPI::fromJsonValue(m_contract, json[QString("contract")]);
    m_contract_isSet = !json[QString("contract")].isNull() && m_contract_isValid;

    m_costing_capacity_isValid = ::OpenAPI::fromJsonValue(m_costing_capacity, json[QString("costing_capacity")]);
    m_costing_capacity_isSet = !json[QString("costing_capacity")].isNull() && m_costing_capacity_isValid;

    m_creation_timestamp_isValid = ::OpenAPI::fromJsonValue(m_creation_timestamp, json[QString("creation_timestamp")]);
    m_creation_timestamp_isSet = !json[QString("creation_timestamp")].isNull() && m_creation_timestamp_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_datetime_isValid = ::OpenAPI::fromJsonValue(m_datetime, json[QString("datetime")]);
    m_datetime_isSet = !json[QString("datetime")].isNull() && m_datetime_isValid;

    m_free_isValid = ::OpenAPI::fromJsonValue(m_free, json[QString("free")]);
    m_free_isSet = !json[QString("free")].isNull() && m_free_isValid;

    m_general_sales_date_isValid = ::OpenAPI::fromJsonValue(m_general_sales_date, json[QString("general_sales_date")]);
    m_general_sales_date_isSet = !json[QString("general_sales_date")].isNull() && m_general_sales_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_input_type_isValid = ::OpenAPI::fromJsonValue(m_input_type, json[QString("input_type")]);
    m_input_type_isSet = !json[QString("input_type")].isNull() && m_input_type_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_last_update_timestamp_isValid = ::OpenAPI::fromJsonValue(m_last_update_timestamp, json[QString("last_update_timestamp")]);
    m_last_update_timestamp_isSet = !json[QString("last_update_timestamp")].isNull() && m_last_update_timestamp_isValid;

    m_max_capacity_isValid = ::OpenAPI::fromJsonValue(m_max_capacity, json[QString("max_capacity")]);
    m_max_capacity_isSet = !json[QString("max_capacity")].isNull() && m_max_capacity_isValid;

    m_presales_date_isValid = ::OpenAPI::fromJsonValue(m_presales_date, json[QString("presales_date")]);
    m_presales_date_isSet = !json[QString("presales_date")].isNull() && m_presales_date_isValid;

    m_series_id_isValid = ::OpenAPI::fromJsonValue(m_series_id, json[QString("series_id")]);
    m_series_id_isSet = !json[QString("series_id")].isNull() && m_series_id_isValid;

    m_sold_out_date_isValid = ::OpenAPI::fromJsonValue(m_sold_out_date, json[QString("sold_out_date")]);
    m_sold_out_date_isSet = !json[QString("sold_out_date")].isNull() && m_sold_out_date_isValid;

    m_venue_isValid = ::OpenAPI::fromJsonValue(m_venue, json[QString("venue")]);
    m_venue_isSet = !json[QString("venue")].isNull() && m_venue_isValid;
}

QString OAIEventsEntity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEventsEntity::asJsonObject() const {
    QJsonObject obj;
    if (m_break_even_isSet) {
        obj.insert(QString("break_even"), ::OpenAPI::toJsonValue(m_break_even));
    }
    if (m_cancellation_date_isSet) {
        obj.insert(QString("cancellation_date"), ::OpenAPI::toJsonValue(m_cancellation_date));
    }
    if (m_contract.isSet()) {
        obj.insert(QString("contract"), ::OpenAPI::toJsonValue(m_contract));
    }
    if (m_costing_capacity_isSet) {
        obj.insert(QString("costing_capacity"), ::OpenAPI::toJsonValue(m_costing_capacity));
    }
    if (m_creation_timestamp_isSet) {
        obj.insert(QString("creation_timestamp"), ::OpenAPI::toJsonValue(m_creation_timestamp));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_datetime_isSet) {
        obj.insert(QString("datetime"), ::OpenAPI::toJsonValue(m_datetime));
    }
    if (m_free_isSet) {
        obj.insert(QString("free"), ::OpenAPI::toJsonValue(m_free));
    }
    if (m_general_sales_date_isSet) {
        obj.insert(QString("general_sales_date"), ::OpenAPI::toJsonValue(m_general_sales_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_input_type.isSet()) {
        obj.insert(QString("input_type"), ::OpenAPI::toJsonValue(m_input_type));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_last_update_timestamp_isSet) {
        obj.insert(QString("last_update_timestamp"), ::OpenAPI::toJsonValue(m_last_update_timestamp));
    }
    if (m_max_capacity_isSet) {
        obj.insert(QString("max_capacity"), ::OpenAPI::toJsonValue(m_max_capacity));
    }
    if (m_presales_date_isSet) {
        obj.insert(QString("presales_date"), ::OpenAPI::toJsonValue(m_presales_date));
    }
    if (m_series_id_isSet) {
        obj.insert(QString("series_id"), ::OpenAPI::toJsonValue(m_series_id));
    }
    if (m_sold_out_date_isSet) {
        obj.insert(QString("sold_out_date"), ::OpenAPI::toJsonValue(m_sold_out_date));
    }
    if (m_venue.isSet()) {
        obj.insert(QString("venue"), ::OpenAPI::toJsonValue(m_venue));
    }
    return obj;
}

qint32 OAIEventsEntity::getBreakEven() const {
    return m_break_even;
}
void OAIEventsEntity::setBreakEven(const qint32 &break_even) {
    m_break_even = break_even;
    m_break_even_isSet = true;
}

bool OAIEventsEntity::is_break_even_Set() const{
    return m_break_even_isSet;
}

bool OAIEventsEntity::is_break_even_Valid() const{
    return m_break_even_isValid;
}

QDate OAIEventsEntity::getCancellationDate() const {
    return m_cancellation_date;
}
void OAIEventsEntity::setCancellationDate(const QDate &cancellation_date) {
    m_cancellation_date = cancellation_date;
    m_cancellation_date_isSet = true;
}

bool OAIEventsEntity::is_cancellation_date_Set() const{
    return m_cancellation_date_isSet;
}

bool OAIEventsEntity::is_cancellation_date_Valid() const{
    return m_cancellation_date_isValid;
}

OAIEventsEntity_contract OAIEventsEntity::getContract() const {
    return m_contract;
}
void OAIEventsEntity::setContract(const OAIEventsEntity_contract &contract) {
    m_contract = contract;
    m_contract_isSet = true;
}

bool OAIEventsEntity::is_contract_Set() const{
    return m_contract_isSet;
}

bool OAIEventsEntity::is_contract_Valid() const{
    return m_contract_isValid;
}

qint32 OAIEventsEntity::getCostingCapacity() const {
    return m_costing_capacity;
}
void OAIEventsEntity::setCostingCapacity(const qint32 &costing_capacity) {
    m_costing_capacity = costing_capacity;
    m_costing_capacity_isSet = true;
}

bool OAIEventsEntity::is_costing_capacity_Set() const{
    return m_costing_capacity_isSet;
}

bool OAIEventsEntity::is_costing_capacity_Valid() const{
    return m_costing_capacity_isValid;
}

qint64 OAIEventsEntity::getCreationTimestamp() const {
    return m_creation_timestamp;
}
void OAIEventsEntity::setCreationTimestamp(const qint64 &creation_timestamp) {
    m_creation_timestamp = creation_timestamp;
    m_creation_timestamp_isSet = true;
}

bool OAIEventsEntity::is_creation_timestamp_Set() const{
    return m_creation_timestamp_isSet;
}

bool OAIEventsEntity::is_creation_timestamp_Valid() const{
    return m_creation_timestamp_isValid;
}

QString OAIEventsEntity::getCurrency() const {
    return m_currency;
}
void OAIEventsEntity::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIEventsEntity::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIEventsEntity::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIEventsEntity::getDatetime() const {
    return m_datetime;
}
void OAIEventsEntity::setDatetime(const QString &datetime) {
    m_datetime = datetime;
    m_datetime_isSet = true;
}

bool OAIEventsEntity::is_datetime_Set() const{
    return m_datetime_isSet;
}

bool OAIEventsEntity::is_datetime_Valid() const{
    return m_datetime_isValid;
}

bool OAIEventsEntity::isFree() const {
    return m_free;
}
void OAIEventsEntity::setFree(const bool &free) {
    m_free = free;
    m_free_isSet = true;
}

bool OAIEventsEntity::is_free_Set() const{
    return m_free_isSet;
}

bool OAIEventsEntity::is_free_Valid() const{
    return m_free_isValid;
}

QDate OAIEventsEntity::getGeneralSalesDate() const {
    return m_general_sales_date;
}
void OAIEventsEntity::setGeneralSalesDate(const QDate &general_sales_date) {
    m_general_sales_date = general_sales_date;
    m_general_sales_date_isSet = true;
}

bool OAIEventsEntity::is_general_sales_date_Set() const{
    return m_general_sales_date_isSet;
}

bool OAIEventsEntity::is_general_sales_date_Valid() const{
    return m_general_sales_date_isValid;
}

qint32 OAIEventsEntity::getId() const {
    return m_id;
}
void OAIEventsEntity::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEventsEntity::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEventsEntity::is_id_Valid() const{
    return m_id_isValid;
}

OAIEventsEntity_input_type OAIEventsEntity::getInputType() const {
    return m_input_type;
}
void OAIEventsEntity::setInputType(const OAIEventsEntity_input_type &input_type) {
    m_input_type = input_type;
    m_input_type_isSet = true;
}

bool OAIEventsEntity::is_input_type_Set() const{
    return m_input_type_isSet;
}

bool OAIEventsEntity::is_input_type_Valid() const{
    return m_input_type_isValid;
}

QString OAIEventsEntity::getLabel() const {
    return m_label;
}
void OAIEventsEntity::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIEventsEntity::is_label_Set() const{
    return m_label_isSet;
}

bool OAIEventsEntity::is_label_Valid() const{
    return m_label_isValid;
}

qint64 OAIEventsEntity::getLastUpdateTimestamp() const {
    return m_last_update_timestamp;
}
void OAIEventsEntity::setLastUpdateTimestamp(const qint64 &last_update_timestamp) {
    m_last_update_timestamp = last_update_timestamp;
    m_last_update_timestamp_isSet = true;
}

bool OAIEventsEntity::is_last_update_timestamp_Set() const{
    return m_last_update_timestamp_isSet;
}

bool OAIEventsEntity::is_last_update_timestamp_Valid() const{
    return m_last_update_timestamp_isValid;
}

qint32 OAIEventsEntity::getMaxCapacity() const {
    return m_max_capacity;
}
void OAIEventsEntity::setMaxCapacity(const qint32 &max_capacity) {
    m_max_capacity = max_capacity;
    m_max_capacity_isSet = true;
}

bool OAIEventsEntity::is_max_capacity_Set() const{
    return m_max_capacity_isSet;
}

bool OAIEventsEntity::is_max_capacity_Valid() const{
    return m_max_capacity_isValid;
}

QDate OAIEventsEntity::getPresalesDate() const {
    return m_presales_date;
}
void OAIEventsEntity::setPresalesDate(const QDate &presales_date) {
    m_presales_date = presales_date;
    m_presales_date_isSet = true;
}

bool OAIEventsEntity::is_presales_date_Set() const{
    return m_presales_date_isSet;
}

bool OAIEventsEntity::is_presales_date_Valid() const{
    return m_presales_date_isValid;
}

qint32 OAIEventsEntity::getSeriesId() const {
    return m_series_id;
}
void OAIEventsEntity::setSeriesId(const qint32 &series_id) {
    m_series_id = series_id;
    m_series_id_isSet = true;
}

bool OAIEventsEntity::is_series_id_Set() const{
    return m_series_id_isSet;
}

bool OAIEventsEntity::is_series_id_Valid() const{
    return m_series_id_isValid;
}

QDate OAIEventsEntity::getSoldOutDate() const {
    return m_sold_out_date;
}
void OAIEventsEntity::setSoldOutDate(const QDate &sold_out_date) {
    m_sold_out_date = sold_out_date;
    m_sold_out_date_isSet = true;
}

bool OAIEventsEntity::is_sold_out_date_Set() const{
    return m_sold_out_date_isSet;
}

bool OAIEventsEntity::is_sold_out_date_Valid() const{
    return m_sold_out_date_isValid;
}

OAIVenuesEntity OAIEventsEntity::getVenue() const {
    return m_venue;
}
void OAIEventsEntity::setVenue(const OAIVenuesEntity &venue) {
    m_venue = venue;
    m_venue_isSet = true;
}

bool OAIEventsEntity::is_venue_Set() const{
    return m_venue_isSet;
}

bool OAIEventsEntity::is_venue_Valid() const{
    return m_venue_isValid;
}

bool OAIEventsEntity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_break_even_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cancellation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contract.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_costing_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_free_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_general_sales_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_update_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_presales_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_series_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sold_out_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_venue.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEventsEntity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_contract_isValid && m_creation_timestamp_isValid && m_datetime_isValid && m_free_isValid && m_id_isValid && m_input_type_isValid && m_label_isValid && m_last_update_timestamp_isValid && m_series_id_isValid && m_venue_isValid && true;
}

} // namespace OpenAPI
