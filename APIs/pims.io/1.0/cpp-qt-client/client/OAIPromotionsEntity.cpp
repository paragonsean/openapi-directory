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

#include "OAIPromotionsEntity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPromotionsEntity::OAIPromotionsEntity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPromotionsEntity::OAIPromotionsEntity() {
    this->initializeModel();
}

OAIPromotionsEntity::~OAIPromotionsEntity() {}

void OAIPromotionsEntity::initializeModel() {

    m_applied_to_isSet = false;
    m_applied_to_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_cost_isSet = false;
    m_cost_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_file_isSet = false;
    m_file_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_supplier_isSet = false;
    m_supplier_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPromotionsEntity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPromotionsEntity::fromJsonObject(QJsonObject json) {

    m_applied_to_isValid = ::OpenAPI::fromJsonValue(m_applied_to, json[QString("applied_to")]);
    m_applied_to_isSet = !json[QString("applied_to")].isNull() && m_applied_to_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_cost_isValid = ::OpenAPI::fromJsonValue(m_cost, json[QString("cost")]);
    m_cost_isSet = !json[QString("cost")].isNull() && m_cost_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_file_isValid = ::OpenAPI::fromJsonValue(m_file, json[QString("file")]);
    m_file_isSet = !json[QString("file")].isNull() && m_file_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_supplier_isValid = ::OpenAPI::fromJsonValue(m_supplier, json[QString("supplier")]);
    m_supplier_isSet = !json[QString("supplier")].isNull() && m_supplier_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPromotionsEntity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPromotionsEntity::asJsonObject() const {
    QJsonObject obj;
    if (m_applied_to.size() > 0) {
        obj.insert(QString("applied_to"), ::OpenAPI::toJsonValue(m_applied_to));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_cost.isSet()) {
        obj.insert(QString("cost"), ::OpenAPI::toJsonValue(m_cost));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_file_isSet) {
        obj.insert(QString("file"), ::OpenAPI::toJsonValue(m_file));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_supplier.isSet()) {
        obj.insert(QString("supplier"), ::OpenAPI::toJsonValue(m_supplier));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<OAIPromotionsEntity_applied_to_inner> OAIPromotionsEntity::getAppliedTo() const {
    return m_applied_to;
}
void OAIPromotionsEntity::setAppliedTo(const QList<OAIPromotionsEntity_applied_to_inner> &applied_to) {
    m_applied_to = applied_to;
    m_applied_to_isSet = true;
}

bool OAIPromotionsEntity::is_applied_to_Set() const{
    return m_applied_to_isSet;
}

bool OAIPromotionsEntity::is_applied_to_Valid() const{
    return m_applied_to_isValid;
}

QString OAIPromotionsEntity::getComments() const {
    return m_comments;
}
void OAIPromotionsEntity::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIPromotionsEntity::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIPromotionsEntity::is_comments_Valid() const{
    return m_comments_isValid;
}

OAIPromotionsEntity_cost OAIPromotionsEntity::getCost() const {
    return m_cost;
}
void OAIPromotionsEntity::setCost(const OAIPromotionsEntity_cost &cost) {
    m_cost = cost;
    m_cost_isSet = true;
}

bool OAIPromotionsEntity::is_cost_Set() const{
    return m_cost_isSet;
}

bool OAIPromotionsEntity::is_cost_Valid() const{
    return m_cost_isValid;
}

QDate OAIPromotionsEntity::getEndDate() const {
    return m_end_date;
}
void OAIPromotionsEntity::setEndDate(const QDate &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIPromotionsEntity::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIPromotionsEntity::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAIPromotionsEntity::getFile() const {
    return m_file;
}
void OAIPromotionsEntity::setFile(const QString &file) {
    m_file = file;
    m_file_isSet = true;
}

bool OAIPromotionsEntity::is_file_Set() const{
    return m_file_isSet;
}

bool OAIPromotionsEntity::is_file_Valid() const{
    return m_file_isValid;
}

qint32 OAIPromotionsEntity::getId() const {
    return m_id;
}
void OAIPromotionsEntity::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPromotionsEntity::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPromotionsEntity::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPromotionsEntity::getLabel() const {
    return m_label;
}
void OAIPromotionsEntity::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIPromotionsEntity::is_label_Set() const{
    return m_label_isSet;
}

bool OAIPromotionsEntity::is_label_Valid() const{
    return m_label_isValid;
}

QDate OAIPromotionsEntity::getStartDate() const {
    return m_start_date;
}
void OAIPromotionsEntity::setStartDate(const QDate &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIPromotionsEntity::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIPromotionsEntity::is_start_date_Valid() const{
    return m_start_date_isValid;
}

OAIPromotionsEntity_supplier OAIPromotionsEntity::getSupplier() const {
    return m_supplier;
}
void OAIPromotionsEntity::setSupplier(const OAIPromotionsEntity_supplier &supplier) {
    m_supplier = supplier;
    m_supplier_isSet = true;
}

bool OAIPromotionsEntity::is_supplier_Set() const{
    return m_supplier_isSet;
}

bool OAIPromotionsEntity::is_supplier_Valid() const{
    return m_supplier_isValid;
}

OAIPromotionsEntity_type OAIPromotionsEntity::getType() const {
    return m_type;
}
void OAIPromotionsEntity::setType(const OAIPromotionsEntity_type &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPromotionsEntity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPromotionsEntity::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPromotionsEntity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_applied_to.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplier.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPromotionsEntity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_applied_to_isValid && m_comments_isValid && m_cost_isValid && m_end_date_isValid && m_id_isValid && m_label_isValid && m_start_date_isValid && m_supplier_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
