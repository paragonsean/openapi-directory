/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle_Image.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle_Image::OAIArticle_Image(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle_Image::OAIArticle_Image() {
    this->initializeModel();
}

OAIArticle_Image::~OAIArticle_Image() {}

void OAIArticle_Image::initializeModel() {

    m_large_hd_url_isSet = false;
    m_large_hd_url_isValid = false;

    m_large_url_isSet = false;
    m_large_url_isValid = false;

    m_medium_hd_url_isSet = false;
    m_medium_hd_url_isValid = false;

    m_medium_url_isSet = false;
    m_medium_url_isValid = false;

    m_order_number_isSet = false;
    m_order_number_isValid = false;

    m_small_hd_url_isSet = false;
    m_small_hd_url_isValid = false;

    m_small_url_isSet = false;
    m_small_url_isValid = false;

    m_thumbnail_hd_url_isSet = false;
    m_thumbnail_hd_url_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIArticle_Image::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle_Image::fromJsonObject(QJsonObject json) {

    m_large_hd_url_isValid = ::OpenAPI::fromJsonValue(m_large_hd_url, json[QString("largeHdUrl")]);
    m_large_hd_url_isSet = !json[QString("largeHdUrl")].isNull() && m_large_hd_url_isValid;

    m_large_url_isValid = ::OpenAPI::fromJsonValue(m_large_url, json[QString("largeUrl")]);
    m_large_url_isSet = !json[QString("largeUrl")].isNull() && m_large_url_isValid;

    m_medium_hd_url_isValid = ::OpenAPI::fromJsonValue(m_medium_hd_url, json[QString("mediumHdUrl")]);
    m_medium_hd_url_isSet = !json[QString("mediumHdUrl")].isNull() && m_medium_hd_url_isValid;

    m_medium_url_isValid = ::OpenAPI::fromJsonValue(m_medium_url, json[QString("mediumUrl")]);
    m_medium_url_isSet = !json[QString("mediumUrl")].isNull() && m_medium_url_isValid;

    m_order_number_isValid = ::OpenAPI::fromJsonValue(m_order_number, json[QString("orderNumber")]);
    m_order_number_isSet = !json[QString("orderNumber")].isNull() && m_order_number_isValid;

    m_small_hd_url_isValid = ::OpenAPI::fromJsonValue(m_small_hd_url, json[QString("smallHdUrl")]);
    m_small_hd_url_isSet = !json[QString("smallHdUrl")].isNull() && m_small_hd_url_isValid;

    m_small_url_isValid = ::OpenAPI::fromJsonValue(m_small_url, json[QString("smallUrl")]);
    m_small_url_isSet = !json[QString("smallUrl")].isNull() && m_small_url_isValid;

    m_thumbnail_hd_url_isValid = ::OpenAPI::fromJsonValue(m_thumbnail_hd_url, json[QString("thumbnailHdUrl")]);
    m_thumbnail_hd_url_isSet = !json[QString("thumbnailHdUrl")].isNull() && m_thumbnail_hd_url_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIArticle_Image::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle_Image::asJsonObject() const {
    QJsonObject obj;
    if (m_large_hd_url_isSet) {
        obj.insert(QString("largeHdUrl"), ::OpenAPI::toJsonValue(m_large_hd_url));
    }
    if (m_large_url_isSet) {
        obj.insert(QString("largeUrl"), ::OpenAPI::toJsonValue(m_large_url));
    }
    if (m_medium_hd_url_isSet) {
        obj.insert(QString("mediumHdUrl"), ::OpenAPI::toJsonValue(m_medium_hd_url));
    }
    if (m_medium_url_isSet) {
        obj.insert(QString("mediumUrl"), ::OpenAPI::toJsonValue(m_medium_url));
    }
    if (m_order_number_isSet) {
        obj.insert(QString("orderNumber"), ::OpenAPI::toJsonValue(m_order_number));
    }
    if (m_small_hd_url_isSet) {
        obj.insert(QString("smallHdUrl"), ::OpenAPI::toJsonValue(m_small_hd_url));
    }
    if (m_small_url_isSet) {
        obj.insert(QString("smallUrl"), ::OpenAPI::toJsonValue(m_small_url));
    }
    if (m_thumbnail_hd_url_isSet) {
        obj.insert(QString("thumbnailHdUrl"), ::OpenAPI::toJsonValue(m_thumbnail_hd_url));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIArticle_Image::getLargeHdUrl() const {
    return m_large_hd_url;
}
void OAIArticle_Image::setLargeHdUrl(const QString &large_hd_url) {
    m_large_hd_url = large_hd_url;
    m_large_hd_url_isSet = true;
}

bool OAIArticle_Image::is_large_hd_url_Set() const{
    return m_large_hd_url_isSet;
}

bool OAIArticle_Image::is_large_hd_url_Valid() const{
    return m_large_hd_url_isValid;
}

QString OAIArticle_Image::getLargeUrl() const {
    return m_large_url;
}
void OAIArticle_Image::setLargeUrl(const QString &large_url) {
    m_large_url = large_url;
    m_large_url_isSet = true;
}

bool OAIArticle_Image::is_large_url_Set() const{
    return m_large_url_isSet;
}

bool OAIArticle_Image::is_large_url_Valid() const{
    return m_large_url_isValid;
}

QString OAIArticle_Image::getMediumHdUrl() const {
    return m_medium_hd_url;
}
void OAIArticle_Image::setMediumHdUrl(const QString &medium_hd_url) {
    m_medium_hd_url = medium_hd_url;
    m_medium_hd_url_isSet = true;
}

bool OAIArticle_Image::is_medium_hd_url_Set() const{
    return m_medium_hd_url_isSet;
}

bool OAIArticle_Image::is_medium_hd_url_Valid() const{
    return m_medium_hd_url_isValid;
}

QString OAIArticle_Image::getMediumUrl() const {
    return m_medium_url;
}
void OAIArticle_Image::setMediumUrl(const QString &medium_url) {
    m_medium_url = medium_url;
    m_medium_url_isSet = true;
}

bool OAIArticle_Image::is_medium_url_Set() const{
    return m_medium_url_isSet;
}

bool OAIArticle_Image::is_medium_url_Valid() const{
    return m_medium_url_isValid;
}

qint32 OAIArticle_Image::getOrderNumber() const {
    return m_order_number;
}
void OAIArticle_Image::setOrderNumber(const qint32 &order_number) {
    m_order_number = order_number;
    m_order_number_isSet = true;
}

bool OAIArticle_Image::is_order_number_Set() const{
    return m_order_number_isSet;
}

bool OAIArticle_Image::is_order_number_Valid() const{
    return m_order_number_isValid;
}

QString OAIArticle_Image::getSmallHdUrl() const {
    return m_small_hd_url;
}
void OAIArticle_Image::setSmallHdUrl(const QString &small_hd_url) {
    m_small_hd_url = small_hd_url;
    m_small_hd_url_isSet = true;
}

bool OAIArticle_Image::is_small_hd_url_Set() const{
    return m_small_hd_url_isSet;
}

bool OAIArticle_Image::is_small_hd_url_Valid() const{
    return m_small_hd_url_isValid;
}

QString OAIArticle_Image::getSmallUrl() const {
    return m_small_url;
}
void OAIArticle_Image::setSmallUrl(const QString &small_url) {
    m_small_url = small_url;
    m_small_url_isSet = true;
}

bool OAIArticle_Image::is_small_url_Set() const{
    return m_small_url_isSet;
}

bool OAIArticle_Image::is_small_url_Valid() const{
    return m_small_url_isValid;
}

QString OAIArticle_Image::getThumbnailHdUrl() const {
    return m_thumbnail_hd_url;
}
void OAIArticle_Image::setThumbnailHdUrl(const QString &thumbnail_hd_url) {
    m_thumbnail_hd_url = thumbnail_hd_url;
    m_thumbnail_hd_url_isSet = true;
}

bool OAIArticle_Image::is_thumbnail_hd_url_Set() const{
    return m_thumbnail_hd_url_isSet;
}

bool OAIArticle_Image::is_thumbnail_hd_url_Valid() const{
    return m_thumbnail_hd_url_isValid;
}

QString OAIArticle_Image::getType() const {
    return m_type;
}
void OAIArticle_Image::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIArticle_Image::is_type_Set() const{
    return m_type_isSet;
}

bool OAIArticle_Image::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIArticle_Image::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_large_hd_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_large_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_medium_hd_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_medium_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_small_hd_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_small_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_hd_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle_Image::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_large_hd_url_isValid && m_large_url_isValid && m_medium_hd_url_isValid && m_medium_url_isValid && m_order_number_isValid && m_small_hd_url_isValid && m_small_url_isValid && m_thumbnail_hd_url_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
