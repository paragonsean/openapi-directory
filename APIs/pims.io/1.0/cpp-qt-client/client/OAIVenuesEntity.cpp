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

#include "OAIVenuesEntity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVenuesEntity::OAIVenuesEntity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVenuesEntity::OAIVenuesEntity() {
    this->initializeModel();
}

OAIVenuesEntity::~OAIVenuesEntity() {}

void OAIVenuesEntity::initializeModel() {

    m_alternative_labels_isSet = false;
    m_alternative_labels_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_creation_timestamp_isSet = false;
    m_creation_timestamp_isValid = false;

    m_first_address_isSet = false;
    m_first_address_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_last_update_timestamp_isSet = false;
    m_last_update_timestamp_isValid = false;

    m_major_city_isSet = false;
    m_major_city_isValid = false;

    m_second_address_isSet = false;
    m_second_address_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_zip_code_isSet = false;
    m_zip_code_isValid = false;
}

void OAIVenuesEntity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVenuesEntity::fromJsonObject(QJsonObject json) {

    m_alternative_labels_isValid = ::OpenAPI::fromJsonValue(m_alternative_labels, json[QString("alternative_labels")]);
    m_alternative_labels_isSet = !json[QString("alternative_labels")].isNull() && m_alternative_labels_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("country_code")]);
    m_country_code_isSet = !json[QString("country_code")].isNull() && m_country_code_isValid;

    m_creation_timestamp_isValid = ::OpenAPI::fromJsonValue(m_creation_timestamp, json[QString("creation_timestamp")]);
    m_creation_timestamp_isSet = !json[QString("creation_timestamp")].isNull() && m_creation_timestamp_isValid;

    m_first_address_isValid = ::OpenAPI::fromJsonValue(m_first_address, json[QString("first_address")]);
    m_first_address_isSet = !json[QString("first_address")].isNull() && m_first_address_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_last_update_timestamp_isValid = ::OpenAPI::fromJsonValue(m_last_update_timestamp, json[QString("last_update_timestamp")]);
    m_last_update_timestamp_isSet = !json[QString("last_update_timestamp")].isNull() && m_last_update_timestamp_isValid;

    m_major_city_isValid = ::OpenAPI::fromJsonValue(m_major_city, json[QString("major_city")]);
    m_major_city_isSet = !json[QString("major_city")].isNull() && m_major_city_isValid;

    m_second_address_isValid = ::OpenAPI::fromJsonValue(m_second_address, json[QString("second_address")]);
    m_second_address_isSet = !json[QString("second_address")].isNull() && m_second_address_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_zip_code_isValid = ::OpenAPI::fromJsonValue(m_zip_code, json[QString("zip_code")]);
    m_zip_code_isSet = !json[QString("zip_code")].isNull() && m_zip_code_isValid;
}

QString OAIVenuesEntity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVenuesEntity::asJsonObject() const {
    QJsonObject obj;
    if (m_alternative_labels.size() > 0) {
        obj.insert(QString("alternative_labels"), ::OpenAPI::toJsonValue(m_alternative_labels));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_code_isSet) {
        obj.insert(QString("country_code"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_creation_timestamp_isSet) {
        obj.insert(QString("creation_timestamp"), ::OpenAPI::toJsonValue(m_creation_timestamp));
    }
    if (m_first_address_isSet) {
        obj.insert(QString("first_address"), ::OpenAPI::toJsonValue(m_first_address));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_last_update_timestamp_isSet) {
        obj.insert(QString("last_update_timestamp"), ::OpenAPI::toJsonValue(m_last_update_timestamp));
    }
    if (m_major_city_isSet) {
        obj.insert(QString("major_city"), ::OpenAPI::toJsonValue(m_major_city));
    }
    if (m_second_address_isSet) {
        obj.insert(QString("second_address"), ::OpenAPI::toJsonValue(m_second_address));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_zip_code_isSet) {
        obj.insert(QString("zip_code"), ::OpenAPI::toJsonValue(m_zip_code));
    }
    return obj;
}

QList<QString> OAIVenuesEntity::getAlternativeLabels() const {
    return m_alternative_labels;
}
void OAIVenuesEntity::setAlternativeLabels(const QList<QString> &alternative_labels) {
    m_alternative_labels = alternative_labels;
    m_alternative_labels_isSet = true;
}

bool OAIVenuesEntity::is_alternative_labels_Set() const{
    return m_alternative_labels_isSet;
}

bool OAIVenuesEntity::is_alternative_labels_Valid() const{
    return m_alternative_labels_isValid;
}

QString OAIVenuesEntity::getCity() const {
    return m_city;
}
void OAIVenuesEntity::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIVenuesEntity::is_city_Set() const{
    return m_city_isSet;
}

bool OAIVenuesEntity::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIVenuesEntity::getCountryCode() const {
    return m_country_code;
}
void OAIVenuesEntity::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAIVenuesEntity::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAIVenuesEntity::is_country_code_Valid() const{
    return m_country_code_isValid;
}

qint64 OAIVenuesEntity::getCreationTimestamp() const {
    return m_creation_timestamp;
}
void OAIVenuesEntity::setCreationTimestamp(const qint64 &creation_timestamp) {
    m_creation_timestamp = creation_timestamp;
    m_creation_timestamp_isSet = true;
}

bool OAIVenuesEntity::is_creation_timestamp_Set() const{
    return m_creation_timestamp_isSet;
}

bool OAIVenuesEntity::is_creation_timestamp_Valid() const{
    return m_creation_timestamp_isValid;
}

QString OAIVenuesEntity::getFirstAddress() const {
    return m_first_address;
}
void OAIVenuesEntity::setFirstAddress(const QString &first_address) {
    m_first_address = first_address;
    m_first_address_isSet = true;
}

bool OAIVenuesEntity::is_first_address_Set() const{
    return m_first_address_isSet;
}

bool OAIVenuesEntity::is_first_address_Valid() const{
    return m_first_address_isValid;
}

qint32 OAIVenuesEntity::getId() const {
    return m_id;
}
void OAIVenuesEntity::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVenuesEntity::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVenuesEntity::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVenuesEntity::getLabel() const {
    return m_label;
}
void OAIVenuesEntity::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIVenuesEntity::is_label_Set() const{
    return m_label_isSet;
}

bool OAIVenuesEntity::is_label_Valid() const{
    return m_label_isValid;
}

qint64 OAIVenuesEntity::getLastUpdateTimestamp() const {
    return m_last_update_timestamp;
}
void OAIVenuesEntity::setLastUpdateTimestamp(const qint64 &last_update_timestamp) {
    m_last_update_timestamp = last_update_timestamp;
    m_last_update_timestamp_isSet = true;
}

bool OAIVenuesEntity::is_last_update_timestamp_Set() const{
    return m_last_update_timestamp_isSet;
}

bool OAIVenuesEntity::is_last_update_timestamp_Valid() const{
    return m_last_update_timestamp_isValid;
}

QString OAIVenuesEntity::getMajorCity() const {
    return m_major_city;
}
void OAIVenuesEntity::setMajorCity(const QString &major_city) {
    m_major_city = major_city;
    m_major_city_isSet = true;
}

bool OAIVenuesEntity::is_major_city_Set() const{
    return m_major_city_isSet;
}

bool OAIVenuesEntity::is_major_city_Valid() const{
    return m_major_city_isValid;
}

QString OAIVenuesEntity::getSecondAddress() const {
    return m_second_address;
}
void OAIVenuesEntity::setSecondAddress(const QString &second_address) {
    m_second_address = second_address;
    m_second_address_isSet = true;
}

bool OAIVenuesEntity::is_second_address_Set() const{
    return m_second_address_isSet;
}

bool OAIVenuesEntity::is_second_address_Valid() const{
    return m_second_address_isValid;
}

OAIVenuesEntity_type OAIVenuesEntity::getType() const {
    return m_type;
}
void OAIVenuesEntity::setType(const OAIVenuesEntity_type &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIVenuesEntity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIVenuesEntity::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIVenuesEntity::getZipCode() const {
    return m_zip_code;
}
void OAIVenuesEntity::setZipCode(const QString &zip_code) {
    m_zip_code = zip_code;
    m_zip_code_isSet = true;
}

bool OAIVenuesEntity::is_zip_code_Set() const{
    return m_zip_code_isSet;
}

bool OAIVenuesEntity::is_zip_code_Valid() const{
    return m_zip_code_isValid;
}

bool OAIVenuesEntity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alternative_labels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_address_isSet) {
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

        if (m_last_update_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_major_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_second_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVenuesEntity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_city_isValid && m_country_code_isValid && m_creation_timestamp_isValid && m_first_address_isValid && m_id_isValid && m_label_isValid && m_last_update_timestamp_isValid && m_major_city_isValid && m_second_address_isValid && m_type_isValid && m_zip_code_isValid && true;
}

} // namespace OpenAPI
