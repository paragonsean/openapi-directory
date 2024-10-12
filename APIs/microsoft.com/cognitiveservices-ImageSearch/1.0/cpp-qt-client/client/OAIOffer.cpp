/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOffer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOffer::OAIOffer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOffer::OAIOffer() {
    this->initializeModel();
}

OAIOffer::~OAIOffer() {}

void OAIOffer::initializeModel() {

    m_aggregate_rating_isSet = false;
    m_aggregate_rating_isValid = false;

    m_availability_isSet = false;
    m_availability_isValid = false;

    m_last_updated_isSet = false;
    m_last_updated_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_currency_isSet = false;
    m_price_currency_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;

    m_alternate_name_isSet = false;
    m_alternate_name_isValid = false;

    m_bing_id_isSet = false;
    m_bing_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_read_link_isSet = false;
    m_read_link_isValid = false;

    m_web_search_url_isSet = false;
    m_web_search_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m__type_isSet = false;
    m__type_isValid = false;
}

void OAIOffer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOffer::fromJsonObject(QJsonObject json) {

    m_aggregate_rating_isValid = ::OpenAPI::fromJsonValue(m_aggregate_rating, json[QString("aggregateRating")]);
    m_aggregate_rating_isSet = !json[QString("aggregateRating")].isNull() && m_aggregate_rating_isValid;

    m_availability_isValid = ::OpenAPI::fromJsonValue(m_availability, json[QString("availability")]);
    m_availability_isSet = !json[QString("availability")].isNull() && m_availability_isValid;

    m_last_updated_isValid = ::OpenAPI::fromJsonValue(m_last_updated, json[QString("lastUpdated")]);
    m_last_updated_isSet = !json[QString("lastUpdated")].isNull() && m_last_updated_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_currency_isValid = ::OpenAPI::fromJsonValue(m_price_currency, json[QString("priceCurrency")]);
    m_price_currency_isSet = !json[QString("priceCurrency")].isNull() && m_price_currency_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;

    m_alternate_name_isValid = ::OpenAPI::fromJsonValue(m_alternate_name, json[QString("alternateName")]);
    m_alternate_name_isSet = !json[QString("alternateName")].isNull() && m_alternate_name_isValid;

    m_bing_id_isValid = ::OpenAPI::fromJsonValue(m_bing_id, json[QString("bingId")]);
    m_bing_id_isSet = !json[QString("bingId")].isNull() && m_bing_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_read_link_isValid = ::OpenAPI::fromJsonValue(m_read_link, json[QString("readLink")]);
    m_read_link_isSet = !json[QString("readLink")].isNull() && m_read_link_isValid;

    m_web_search_url_isValid = ::OpenAPI::fromJsonValue(m_web_search_url, json[QString("webSearchUrl")]);
    m_web_search_url_isSet = !json[QString("webSearchUrl")].isNull() && m_web_search_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m__type_isValid = ::OpenAPI::fromJsonValue(m__type, json[QString("_type")]);
    m__type_isSet = !json[QString("_type")].isNull() && m__type_isValid;
}

QString OAIOffer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOffer::asJsonObject() const {
    QJsonObject obj;
    if (m_aggregate_rating.isSet()) {
        obj.insert(QString("aggregateRating"), ::OpenAPI::toJsonValue(m_aggregate_rating));
    }
    if (m_availability_isSet) {
        obj.insert(QString("availability"), ::OpenAPI::toJsonValue(m_availability));
    }
    if (m_last_updated_isSet) {
        obj.insert(QString("lastUpdated"), ::OpenAPI::toJsonValue(m_last_updated));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_currency_isSet) {
        obj.insert(QString("priceCurrency"), ::OpenAPI::toJsonValue(m_price_currency));
    }
    if (m_seller.isSet()) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    if (m_alternate_name_isSet) {
        obj.insert(QString("alternateName"), ::OpenAPI::toJsonValue(m_alternate_name));
    }
    if (m_bing_id_isSet) {
        obj.insert(QString("bingId"), ::OpenAPI::toJsonValue(m_bing_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_image.isSet()) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_read_link_isSet) {
        obj.insert(QString("readLink"), ::OpenAPI::toJsonValue(m_read_link));
    }
    if (m_web_search_url_isSet) {
        obj.insert(QString("webSearchUrl"), ::OpenAPI::toJsonValue(m_web_search_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m__type_isSet) {
        obj.insert(QString("_type"), ::OpenAPI::toJsonValue(m__type));
    }
    return obj;
}

OAIAggregateRating OAIOffer::getAggregateRating() const {
    return m_aggregate_rating;
}
void OAIOffer::setAggregateRating(const OAIAggregateRating &aggregate_rating) {
    m_aggregate_rating = aggregate_rating;
    m_aggregate_rating_isSet = true;
}

bool OAIOffer::is_aggregate_rating_Set() const{
    return m_aggregate_rating_isSet;
}

bool OAIOffer::is_aggregate_rating_Valid() const{
    return m_aggregate_rating_isValid;
}

QString OAIOffer::getAvailability() const {
    return m_availability;
}
void OAIOffer::setAvailability(const QString &availability) {
    m_availability = availability;
    m_availability_isSet = true;
}

bool OAIOffer::is_availability_Set() const{
    return m_availability_isSet;
}

bool OAIOffer::is_availability_Valid() const{
    return m_availability_isValid;
}

QString OAIOffer::getLastUpdated() const {
    return m_last_updated;
}
void OAIOffer::setLastUpdated(const QString &last_updated) {
    m_last_updated = last_updated;
    m_last_updated_isSet = true;
}

bool OAIOffer::is_last_updated_Set() const{
    return m_last_updated_isSet;
}

bool OAIOffer::is_last_updated_Valid() const{
    return m_last_updated_isValid;
}

float OAIOffer::getPrice() const {
    return m_price;
}
void OAIOffer::setPrice(const float &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIOffer::is_price_Set() const{
    return m_price_isSet;
}

bool OAIOffer::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIOffer::getPriceCurrency() const {
    return m_price_currency;
}
void OAIOffer::setPriceCurrency(const QString &price_currency) {
    m_price_currency = price_currency;
    m_price_currency_isSet = true;
}

bool OAIOffer::is_price_currency_Set() const{
    return m_price_currency_isSet;
}

bool OAIOffer::is_price_currency_Valid() const{
    return m_price_currency_isValid;
}

OAIOrganization OAIOffer::getSeller() const {
    return m_seller;
}
void OAIOffer::setSeller(const OAIOrganization &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAIOffer::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAIOffer::is_seller_Valid() const{
    return m_seller_isValid;
}

QString OAIOffer::getAlternateName() const {
    return m_alternate_name;
}
void OAIOffer::setAlternateName(const QString &alternate_name) {
    m_alternate_name = alternate_name;
    m_alternate_name_isSet = true;
}

bool OAIOffer::is_alternate_name_Set() const{
    return m_alternate_name_isSet;
}

bool OAIOffer::is_alternate_name_Valid() const{
    return m_alternate_name_isValid;
}

QString OAIOffer::getBingId() const {
    return m_bing_id;
}
void OAIOffer::setBingId(const QString &bing_id) {
    m_bing_id = bing_id;
    m_bing_id_isSet = true;
}

bool OAIOffer::is_bing_id_Set() const{
    return m_bing_id_isSet;
}

bool OAIOffer::is_bing_id_Valid() const{
    return m_bing_id_isValid;
}

QString OAIOffer::getDescription() const {
    return m_description;
}
void OAIOffer::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIOffer::is_description_Set() const{
    return m_description_isSet;
}

bool OAIOffer::is_description_Valid() const{
    return m_description_isValid;
}

OAIImageObject OAIOffer::getImage() const {
    return m_image;
}
void OAIOffer::setImage(const OAIImageObject &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIOffer::is_image_Set() const{
    return m_image_isSet;
}

bool OAIOffer::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIOffer::getName() const {
    return m_name;
}
void OAIOffer::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOffer::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOffer::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIOffer::getUrl() const {
    return m_url;
}
void OAIOffer::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIOffer::is_url_Set() const{
    return m_url_isSet;
}

bool OAIOffer::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIOffer::getReadLink() const {
    return m_read_link;
}
void OAIOffer::setReadLink(const QString &read_link) {
    m_read_link = read_link;
    m_read_link_isSet = true;
}

bool OAIOffer::is_read_link_Set() const{
    return m_read_link_isSet;
}

bool OAIOffer::is_read_link_Valid() const{
    return m_read_link_isValid;
}

QString OAIOffer::getWebSearchUrl() const {
    return m_web_search_url;
}
void OAIOffer::setWebSearchUrl(const QString &web_search_url) {
    m_web_search_url = web_search_url;
    m_web_search_url_isSet = true;
}

bool OAIOffer::is_web_search_url_Set() const{
    return m_web_search_url_isSet;
}

bool OAIOffer::is_web_search_url_Valid() const{
    return m_web_search_url_isValid;
}

QString OAIOffer::getId() const {
    return m_id;
}
void OAIOffer::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOffer::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOffer::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOffer::getType() const {
    return m__type;
}
void OAIOffer::setType(const QString &_type) {
    m__type = _type;
    m__type_isSet = true;
}

bool OAIOffer::is__type_Set() const{
    return m__type_isSet;
}

bool OAIOffer::is__type_Valid() const{
    return m__type_isValid;
}

bool OAIOffer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aggregate_rating.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_availability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_alternate_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bing_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_search_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOffer::isValid() const {
    // only required properties are required for the object to be considered valid
    return m__type_isValid && true;
}

} // namespace OpenAPI
