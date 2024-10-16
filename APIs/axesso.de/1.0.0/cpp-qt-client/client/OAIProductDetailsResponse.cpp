/**
 * Axesso Api
 * Use this api to fetch information to Amazon products and more.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@axesso.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProductDetailsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductDetailsResponse::OAIProductDetailsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductDetailsResponse::OAIProductDetailsResponse() {
    this->initializeModel();
}

OAIProductDetailsResponse::~OAIProductDetailsResponse() {}

void OAIProductDetailsResponse::initializeModel() {

    m_answered_questions_isSet = false;
    m_answered_questions_isValid = false;

    m_asin_isSet = false;
    m_asin_isValid = false;

    m_count_review_isSet = false;
    m_count_review_isValid = false;

    m_features_isSet = false;
    m_features_isValid = false;

    m_fulfilled_by_isSet = false;
    m_fulfilled_by_isValid = false;

    m_manufacturer_isSet = false;
    m_manufacturer_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_saving_isSet = false;
    m_price_saving_isValid = false;

    m_price_shipping_information_isSet = false;
    m_price_shipping_information_isValid = false;

    m_prime_isSet = false;
    m_prime_isValid = false;

    m_product_rating_isSet = false;
    m_product_rating_isValid = false;

    m_product_title_isSet = false;
    m_product_title_isValid = false;

    m_response_message_isSet = false;
    m_response_message_isValid = false;

    m_response_status_isSet = false;
    m_response_status_isValid = false;

    m_retail_price_isSet = false;
    m_retail_price_isValid = false;

    m_size_selection_isSet = false;
    m_size_selection_isValid = false;

    m_sold_by_isSet = false;
    m_sold_by_isValid = false;

    m_warehouse_availability_isSet = false;
    m_warehouse_availability_isValid = false;
}

void OAIProductDetailsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductDetailsResponse::fromJsonObject(QJsonObject json) {

    m_answered_questions_isValid = ::OpenAPI::fromJsonValue(m_answered_questions, json[QString("answeredQuestions")]);
    m_answered_questions_isSet = !json[QString("answeredQuestions")].isNull() && m_answered_questions_isValid;

    m_asin_isValid = ::OpenAPI::fromJsonValue(m_asin, json[QString("asin")]);
    m_asin_isSet = !json[QString("asin")].isNull() && m_asin_isValid;

    m_count_review_isValid = ::OpenAPI::fromJsonValue(m_count_review, json[QString("countReview")]);
    m_count_review_isSet = !json[QString("countReview")].isNull() && m_count_review_isValid;

    m_features_isValid = ::OpenAPI::fromJsonValue(m_features, json[QString("features")]);
    m_features_isSet = !json[QString("features")].isNull() && m_features_isValid;

    m_fulfilled_by_isValid = ::OpenAPI::fromJsonValue(m_fulfilled_by, json[QString("fulfilledBy")]);
    m_fulfilled_by_isSet = !json[QString("fulfilledBy")].isNull() && m_fulfilled_by_isValid;

    m_manufacturer_isValid = ::OpenAPI::fromJsonValue(m_manufacturer, json[QString("manufacturer")]);
    m_manufacturer_isSet = !json[QString("manufacturer")].isNull() && m_manufacturer_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_saving_isValid = ::OpenAPI::fromJsonValue(m_price_saving, json[QString("priceSaving")]);
    m_price_saving_isSet = !json[QString("priceSaving")].isNull() && m_price_saving_isValid;

    m_price_shipping_information_isValid = ::OpenAPI::fromJsonValue(m_price_shipping_information, json[QString("priceShippingInformation")]);
    m_price_shipping_information_isSet = !json[QString("priceShippingInformation")].isNull() && m_price_shipping_information_isValid;

    m_prime_isValid = ::OpenAPI::fromJsonValue(m_prime, json[QString("prime")]);
    m_prime_isSet = !json[QString("prime")].isNull() && m_prime_isValid;

    m_product_rating_isValid = ::OpenAPI::fromJsonValue(m_product_rating, json[QString("productRating")]);
    m_product_rating_isSet = !json[QString("productRating")].isNull() && m_product_rating_isValid;

    m_product_title_isValid = ::OpenAPI::fromJsonValue(m_product_title, json[QString("productTitle")]);
    m_product_title_isSet = !json[QString("productTitle")].isNull() && m_product_title_isValid;

    m_response_message_isValid = ::OpenAPI::fromJsonValue(m_response_message, json[QString("responseMessage")]);
    m_response_message_isSet = !json[QString("responseMessage")].isNull() && m_response_message_isValid;

    m_response_status_isValid = ::OpenAPI::fromJsonValue(m_response_status, json[QString("responseStatus")]);
    m_response_status_isSet = !json[QString("responseStatus")].isNull() && m_response_status_isValid;

    m_retail_price_isValid = ::OpenAPI::fromJsonValue(m_retail_price, json[QString("retailPrice")]);
    m_retail_price_isSet = !json[QString("retailPrice")].isNull() && m_retail_price_isValid;

    m_size_selection_isValid = ::OpenAPI::fromJsonValue(m_size_selection, json[QString("sizeSelection")]);
    m_size_selection_isSet = !json[QString("sizeSelection")].isNull() && m_size_selection_isValid;

    m_sold_by_isValid = ::OpenAPI::fromJsonValue(m_sold_by, json[QString("soldBy")]);
    m_sold_by_isSet = !json[QString("soldBy")].isNull() && m_sold_by_isValid;

    m_warehouse_availability_isValid = ::OpenAPI::fromJsonValue(m_warehouse_availability, json[QString("warehouseAvailability")]);
    m_warehouse_availability_isSet = !json[QString("warehouseAvailability")].isNull() && m_warehouse_availability_isValid;
}

QString OAIProductDetailsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductDetailsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_answered_questions_isSet) {
        obj.insert(QString("answeredQuestions"), ::OpenAPI::toJsonValue(m_answered_questions));
    }
    if (m_asin_isSet) {
        obj.insert(QString("asin"), ::OpenAPI::toJsonValue(m_asin));
    }
    if (m_count_review_isSet) {
        obj.insert(QString("countReview"), ::OpenAPI::toJsonValue(m_count_review));
    }
    if (m_features.size() > 0) {
        obj.insert(QString("features"), ::OpenAPI::toJsonValue(m_features));
    }
    if (m_fulfilled_by_isSet) {
        obj.insert(QString("fulfilledBy"), ::OpenAPI::toJsonValue(m_fulfilled_by));
    }
    if (m_manufacturer_isSet) {
        obj.insert(QString("manufacturer"), ::OpenAPI::toJsonValue(m_manufacturer));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_saving_isSet) {
        obj.insert(QString("priceSaving"), ::OpenAPI::toJsonValue(m_price_saving));
    }
    if (m_price_shipping_information_isSet) {
        obj.insert(QString("priceShippingInformation"), ::OpenAPI::toJsonValue(m_price_shipping_information));
    }
    if (m_prime_isSet) {
        obj.insert(QString("prime"), ::OpenAPI::toJsonValue(m_prime));
    }
    if (m_product_rating_isSet) {
        obj.insert(QString("productRating"), ::OpenAPI::toJsonValue(m_product_rating));
    }
    if (m_product_title_isSet) {
        obj.insert(QString("productTitle"), ::OpenAPI::toJsonValue(m_product_title));
    }
    if (m_response_message_isSet) {
        obj.insert(QString("responseMessage"), ::OpenAPI::toJsonValue(m_response_message));
    }
    if (m_response_status_isSet) {
        obj.insert(QString("responseStatus"), ::OpenAPI::toJsonValue(m_response_status));
    }
    if (m_retail_price_isSet) {
        obj.insert(QString("retailPrice"), ::OpenAPI::toJsonValue(m_retail_price));
    }
    if (m_size_selection.size() > 0) {
        obj.insert(QString("sizeSelection"), ::OpenAPI::toJsonValue(m_size_selection));
    }
    if (m_sold_by_isSet) {
        obj.insert(QString("soldBy"), ::OpenAPI::toJsonValue(m_sold_by));
    }
    if (m_warehouse_availability_isSet) {
        obj.insert(QString("warehouseAvailability"), ::OpenAPI::toJsonValue(m_warehouse_availability));
    }
    return obj;
}

qint64 OAIProductDetailsResponse::getAnsweredQuestions() const {
    return m_answered_questions;
}
void OAIProductDetailsResponse::setAnsweredQuestions(const qint64 &answered_questions) {
    m_answered_questions = answered_questions;
    m_answered_questions_isSet = true;
}

bool OAIProductDetailsResponse::is_answered_questions_Set() const{
    return m_answered_questions_isSet;
}

bool OAIProductDetailsResponse::is_answered_questions_Valid() const{
    return m_answered_questions_isValid;
}

QString OAIProductDetailsResponse::getAsin() const {
    return m_asin;
}
void OAIProductDetailsResponse::setAsin(const QString &asin) {
    m_asin = asin;
    m_asin_isSet = true;
}

bool OAIProductDetailsResponse::is_asin_Set() const{
    return m_asin_isSet;
}

bool OAIProductDetailsResponse::is_asin_Valid() const{
    return m_asin_isValid;
}

qint64 OAIProductDetailsResponse::getCountReview() const {
    return m_count_review;
}
void OAIProductDetailsResponse::setCountReview(const qint64 &count_review) {
    m_count_review = count_review;
    m_count_review_isSet = true;
}

bool OAIProductDetailsResponse::is_count_review_Set() const{
    return m_count_review_isSet;
}

bool OAIProductDetailsResponse::is_count_review_Valid() const{
    return m_count_review_isValid;
}

QList<QString> OAIProductDetailsResponse::getFeatures() const {
    return m_features;
}
void OAIProductDetailsResponse::setFeatures(const QList<QString> &features) {
    m_features = features;
    m_features_isSet = true;
}

bool OAIProductDetailsResponse::is_features_Set() const{
    return m_features_isSet;
}

bool OAIProductDetailsResponse::is_features_Valid() const{
    return m_features_isValid;
}

QString OAIProductDetailsResponse::getFulfilledBy() const {
    return m_fulfilled_by;
}
void OAIProductDetailsResponse::setFulfilledBy(const QString &fulfilled_by) {
    m_fulfilled_by = fulfilled_by;
    m_fulfilled_by_isSet = true;
}

bool OAIProductDetailsResponse::is_fulfilled_by_Set() const{
    return m_fulfilled_by_isSet;
}

bool OAIProductDetailsResponse::is_fulfilled_by_Valid() const{
    return m_fulfilled_by_isValid;
}

QString OAIProductDetailsResponse::getManufacturer() const {
    return m_manufacturer;
}
void OAIProductDetailsResponse::setManufacturer(const QString &manufacturer) {
    m_manufacturer = manufacturer;
    m_manufacturer_isSet = true;
}

bool OAIProductDetailsResponse::is_manufacturer_Set() const{
    return m_manufacturer_isSet;
}

bool OAIProductDetailsResponse::is_manufacturer_Valid() const{
    return m_manufacturer_isValid;
}

double OAIProductDetailsResponse::getPrice() const {
    return m_price;
}
void OAIProductDetailsResponse::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIProductDetailsResponse::is_price_Set() const{
    return m_price_isSet;
}

bool OAIProductDetailsResponse::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIProductDetailsResponse::getPriceSaving() const {
    return m_price_saving;
}
void OAIProductDetailsResponse::setPriceSaving(const QString &price_saving) {
    m_price_saving = price_saving;
    m_price_saving_isSet = true;
}

bool OAIProductDetailsResponse::is_price_saving_Set() const{
    return m_price_saving_isSet;
}

bool OAIProductDetailsResponse::is_price_saving_Valid() const{
    return m_price_saving_isValid;
}

QString OAIProductDetailsResponse::getPriceShippingInformation() const {
    return m_price_shipping_information;
}
void OAIProductDetailsResponse::setPriceShippingInformation(const QString &price_shipping_information) {
    m_price_shipping_information = price_shipping_information;
    m_price_shipping_information_isSet = true;
}

bool OAIProductDetailsResponse::is_price_shipping_information_Set() const{
    return m_price_shipping_information_isSet;
}

bool OAIProductDetailsResponse::is_price_shipping_information_Valid() const{
    return m_price_shipping_information_isValid;
}

bool OAIProductDetailsResponse::isPrime() const {
    return m_prime;
}
void OAIProductDetailsResponse::setPrime(const bool &prime) {
    m_prime = prime;
    m_prime_isSet = true;
}

bool OAIProductDetailsResponse::is_prime_Set() const{
    return m_prime_isSet;
}

bool OAIProductDetailsResponse::is_prime_Valid() const{
    return m_prime_isValid;
}

QString OAIProductDetailsResponse::getProductRating() const {
    return m_product_rating;
}
void OAIProductDetailsResponse::setProductRating(const QString &product_rating) {
    m_product_rating = product_rating;
    m_product_rating_isSet = true;
}

bool OAIProductDetailsResponse::is_product_rating_Set() const{
    return m_product_rating_isSet;
}

bool OAIProductDetailsResponse::is_product_rating_Valid() const{
    return m_product_rating_isValid;
}

QString OAIProductDetailsResponse::getProductTitle() const {
    return m_product_title;
}
void OAIProductDetailsResponse::setProductTitle(const QString &product_title) {
    m_product_title = product_title;
    m_product_title_isSet = true;
}

bool OAIProductDetailsResponse::is_product_title_Set() const{
    return m_product_title_isSet;
}

bool OAIProductDetailsResponse::is_product_title_Valid() const{
    return m_product_title_isValid;
}

QString OAIProductDetailsResponse::getResponseMessage() const {
    return m_response_message;
}
void OAIProductDetailsResponse::setResponseMessage(const QString &response_message) {
    m_response_message = response_message;
    m_response_message_isSet = true;
}

bool OAIProductDetailsResponse::is_response_message_Set() const{
    return m_response_message_isSet;
}

bool OAIProductDetailsResponse::is_response_message_Valid() const{
    return m_response_message_isValid;
}

QString OAIProductDetailsResponse::getResponseStatus() const {
    return m_response_status;
}
void OAIProductDetailsResponse::setResponseStatus(const QString &response_status) {
    m_response_status = response_status;
    m_response_status_isSet = true;
}

bool OAIProductDetailsResponse::is_response_status_Set() const{
    return m_response_status_isSet;
}

bool OAIProductDetailsResponse::is_response_status_Valid() const{
    return m_response_status_isValid;
}

double OAIProductDetailsResponse::getRetailPrice() const {
    return m_retail_price;
}
void OAIProductDetailsResponse::setRetailPrice(const double &retail_price) {
    m_retail_price = retail_price;
    m_retail_price_isSet = true;
}

bool OAIProductDetailsResponse::is_retail_price_Set() const{
    return m_retail_price_isSet;
}

bool OAIProductDetailsResponse::is_retail_price_Valid() const{
    return m_retail_price_isValid;
}

QList<QString> OAIProductDetailsResponse::getSizeSelection() const {
    return m_size_selection;
}
void OAIProductDetailsResponse::setSizeSelection(const QList<QString> &size_selection) {
    m_size_selection = size_selection;
    m_size_selection_isSet = true;
}

bool OAIProductDetailsResponse::is_size_selection_Set() const{
    return m_size_selection_isSet;
}

bool OAIProductDetailsResponse::is_size_selection_Valid() const{
    return m_size_selection_isValid;
}

QString OAIProductDetailsResponse::getSoldBy() const {
    return m_sold_by;
}
void OAIProductDetailsResponse::setSoldBy(const QString &sold_by) {
    m_sold_by = sold_by;
    m_sold_by_isSet = true;
}

bool OAIProductDetailsResponse::is_sold_by_Set() const{
    return m_sold_by_isSet;
}

bool OAIProductDetailsResponse::is_sold_by_Valid() const{
    return m_sold_by_isValid;
}

QString OAIProductDetailsResponse::getWarehouseAvailability() const {
    return m_warehouse_availability;
}
void OAIProductDetailsResponse::setWarehouseAvailability(const QString &warehouse_availability) {
    m_warehouse_availability = warehouse_availability;
    m_warehouse_availability_isSet = true;
}

bool OAIProductDetailsResponse::is_warehouse_availability_Set() const{
    return m_warehouse_availability_isSet;
}

bool OAIProductDetailsResponse::is_warehouse_availability_Valid() const{
    return m_warehouse_availability_isValid;
}

bool OAIProductDetailsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_answered_questions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_asin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_review_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_features.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fulfilled_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_saving_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_shipping_information_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_rating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retail_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_selection.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sold_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warehouse_availability_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductDetailsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
