/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVmImage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVmImage::OAIVmImage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVmImage::OAIVmImage() {
    this->initializeModel();
}

OAIVmImage::~OAIVmImage() {}

void OAIVmImage::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_offer_isSet = false;
    m_offer_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIVmImage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVmImage::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_offer_isValid = ::OpenAPI::fromJsonValue(m_offer, json[QString("offer")]);
    m_offer_isSet = !json[QString("offer")].isNull() && m_offer_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("publisher")]);
    m_publisher_isSet = !json[QString("publisher")].isNull() && m_publisher_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIVmImage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVmImage::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_offer_isSet) {
        obj.insert(QString("offer"), ::OpenAPI::toJsonValue(m_offer));
    }
    if (m_publisher_isSet) {
        obj.insert(QString("publisher"), ::OpenAPI::toJsonValue(m_publisher));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIVmImage::getName() const {
    return m_name;
}
void OAIVmImage::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVmImage::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVmImage::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIVmImage::getOffer() const {
    return m_offer;
}
void OAIVmImage::setOffer(const QString &offer) {
    m_offer = offer;
    m_offer_isSet = true;
}

bool OAIVmImage::is_offer_Set() const{
    return m_offer_isSet;
}

bool OAIVmImage::is_offer_Valid() const{
    return m_offer_isValid;
}

QString OAIVmImage::getPublisher() const {
    return m_publisher;
}
void OAIVmImage::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIVmImage::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIVmImage::is_publisher_Valid() const{
    return m_publisher_isValid;
}

QString OAIVmImage::getSku() const {
    return m_sku;
}
void OAIVmImage::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIVmImage::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIVmImage::is_sku_Valid() const{
    return m_sku_isValid;
}

QString OAIVmImage::getVersion() const {
    return m_version;
}
void OAIVmImage::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIVmImage::is_version_Set() const{
    return m_version_isSet;
}

bool OAIVmImage::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIVmImage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVmImage::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_offer_isValid && m_publisher_isValid && m_sku_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
