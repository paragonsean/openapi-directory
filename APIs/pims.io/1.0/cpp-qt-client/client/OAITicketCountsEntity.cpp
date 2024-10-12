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

#include "OAITicketCountsEntity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITicketCountsEntity::OAITicketCountsEntity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITicketCountsEntity::OAITicketCountsEntity() {
    this->initializeModel();
}

OAITicketCountsEntity::~OAITicketCountsEntity() {}

void OAITicketCountsEntity::initializeModel() {

    m_approved_isSet = false;
    m_approved_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_final_isSet = false;
    m_final_isValid = false;

    m_gross_isSet = false;
    m_gross_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_reservations_isSet = false;
    m_reservations_isValid = false;

    m_sales_isSet = false;
    m_sales_isValid = false;
}

void OAITicketCountsEntity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITicketCountsEntity::fromJsonObject(QJsonObject json) {

    m_approved_isValid = ::OpenAPI::fromJsonValue(m_approved, json[QString("approved")]);
    m_approved_isSet = !json[QString("approved")].isNull() && m_approved_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_final_isValid = ::OpenAPI::fromJsonValue(m_final, json[QString("final")]);
    m_final_isSet = !json[QString("final")].isNull() && m_final_isValid;

    m_gross_isValid = ::OpenAPI::fromJsonValue(m_gross, json[QString("gross")]);
    m_gross_isSet = !json[QString("gross")].isNull() && m_gross_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_reservations_isValid = ::OpenAPI::fromJsonValue(m_reservations, json[QString("reservations")]);
    m_reservations_isSet = !json[QString("reservations")].isNull() && m_reservations_isValid;

    m_sales_isValid = ::OpenAPI::fromJsonValue(m_sales, json[QString("sales")]);
    m_sales_isSet = !json[QString("sales")].isNull() && m_sales_isValid;
}

QString OAITicketCountsEntity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITicketCountsEntity::asJsonObject() const {
    QJsonObject obj;
    if (m_approved_isSet) {
        obj.insert(QString("approved"), ::OpenAPI::toJsonValue(m_approved));
    }
    if (m_comment_isSet) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_final_isSet) {
        obj.insert(QString("final"), ::OpenAPI::toJsonValue(m_final));
    }
    if (m_gross_isSet) {
        obj.insert(QString("gross"), ::OpenAPI::toJsonValue(m_gross));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_reservations_isSet) {
        obj.insert(QString("reservations"), ::OpenAPI::toJsonValue(m_reservations));
    }
    if (m_sales_isSet) {
        obj.insert(QString("sales"), ::OpenAPI::toJsonValue(m_sales));
    }
    return obj;
}

bool OAITicketCountsEntity::isApproved() const {
    return m_approved;
}
void OAITicketCountsEntity::setApproved(const bool &approved) {
    m_approved = approved;
    m_approved_isSet = true;
}

bool OAITicketCountsEntity::is_approved_Set() const{
    return m_approved_isSet;
}

bool OAITicketCountsEntity::is_approved_Valid() const{
    return m_approved_isValid;
}

QString OAITicketCountsEntity::getComment() const {
    return m_comment;
}
void OAITicketCountsEntity::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAITicketCountsEntity::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAITicketCountsEntity::is_comment_Valid() const{
    return m_comment_isValid;
}

QString OAITicketCountsEntity::getCurrency() const {
    return m_currency;
}
void OAITicketCountsEntity::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAITicketCountsEntity::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAITicketCountsEntity::is_currency_Valid() const{
    return m_currency_isValid;
}

QDate OAITicketCountsEntity::getDate() const {
    return m_date;
}
void OAITicketCountsEntity::setDate(const QDate &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAITicketCountsEntity::is_date_Set() const{
    return m_date_isSet;
}

bool OAITicketCountsEntity::is_date_Valid() const{
    return m_date_isValid;
}

bool OAITicketCountsEntity::isFinal() const {
    return m_final;
}
void OAITicketCountsEntity::setFinal(const bool &final) {
    m_final = final;
    m_final_isSet = true;
}

bool OAITicketCountsEntity::is_final_Set() const{
    return m_final_isSet;
}

bool OAITicketCountsEntity::is_final_Valid() const{
    return m_final_isValid;
}

float OAITicketCountsEntity::getGross() const {
    return m_gross;
}
void OAITicketCountsEntity::setGross(const float &gross) {
    m_gross = gross;
    m_gross_isSet = true;
}

bool OAITicketCountsEntity::is_gross_Set() const{
    return m_gross_isSet;
}

bool OAITicketCountsEntity::is_gross_Valid() const{
    return m_gross_isValid;
}

qint32 OAITicketCountsEntity::getId() const {
    return m_id;
}
void OAITicketCountsEntity::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITicketCountsEntity::is_id_Set() const{
    return m_id_isSet;
}

bool OAITicketCountsEntity::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAITicketCountsEntity::getReservations() const {
    return m_reservations;
}
void OAITicketCountsEntity::setReservations(const qint32 &reservations) {
    m_reservations = reservations;
    m_reservations_isSet = true;
}

bool OAITicketCountsEntity::is_reservations_Set() const{
    return m_reservations_isSet;
}

bool OAITicketCountsEntity::is_reservations_Valid() const{
    return m_reservations_isValid;
}

qint32 OAITicketCountsEntity::getSales() const {
    return m_sales;
}
void OAITicketCountsEntity::setSales(const qint32 &sales) {
    m_sales = sales;
    m_sales_isSet = true;
}

bool OAITicketCountsEntity::is_sales_Set() const{
    return m_sales_isSet;
}

bool OAITicketCountsEntity::is_sales_Valid() const{
    return m_sales_isValid;
}

bool OAITicketCountsEntity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_approved_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_final_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gross_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reservations_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITicketCountsEntity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_approved_isValid && m_comment_isValid && m_date_isValid && m_final_isValid && m_id_isValid && m_sales_isValid && true;
}

} // namespace OpenAPI
