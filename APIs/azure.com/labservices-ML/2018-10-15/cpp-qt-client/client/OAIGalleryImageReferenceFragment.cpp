/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGalleryImageReferenceFragment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGalleryImageReferenceFragment::OAIGalleryImageReferenceFragment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGalleryImageReferenceFragment::OAIGalleryImageReferenceFragment() {
    this->initializeModel();
}

OAIGalleryImageReferenceFragment::~OAIGalleryImageReferenceFragment() {}

void OAIGalleryImageReferenceFragment::initializeModel() {

    m_offer_isSet = false;
    m_offer_isValid = false;

    m_os_type_isSet = false;
    m_os_type_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIGalleryImageReferenceFragment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGalleryImageReferenceFragment::fromJsonObject(QJsonObject json) {

    m_offer_isValid = ::OpenAPI::fromJsonValue(m_offer, json[QString("offer")]);
    m_offer_isSet = !json[QString("offer")].isNull() && m_offer_isValid;

    m_os_type_isValid = ::OpenAPI::fromJsonValue(m_os_type, json[QString("osType")]);
    m_os_type_isSet = !json[QString("osType")].isNull() && m_os_type_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("publisher")]);
    m_publisher_isSet = !json[QString("publisher")].isNull() && m_publisher_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIGalleryImageReferenceFragment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGalleryImageReferenceFragment::asJsonObject() const {
    QJsonObject obj;
    if (m_offer_isSet) {
        obj.insert(QString("offer"), ::OpenAPI::toJsonValue(m_offer));
    }
    if (m_os_type_isSet) {
        obj.insert(QString("osType"), ::OpenAPI::toJsonValue(m_os_type));
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

QString OAIGalleryImageReferenceFragment::getOffer() const {
    return m_offer;
}
void OAIGalleryImageReferenceFragment::setOffer(const QString &offer) {
    m_offer = offer;
    m_offer_isSet = true;
}

bool OAIGalleryImageReferenceFragment::is_offer_Set() const{
    return m_offer_isSet;
}

bool OAIGalleryImageReferenceFragment::is_offer_Valid() const{
    return m_offer_isValid;
}

QString OAIGalleryImageReferenceFragment::getOsType() const {
    return m_os_type;
}
void OAIGalleryImageReferenceFragment::setOsType(const QString &os_type) {
    m_os_type = os_type;
    m_os_type_isSet = true;
}

bool OAIGalleryImageReferenceFragment::is_os_type_Set() const{
    return m_os_type_isSet;
}

bool OAIGalleryImageReferenceFragment::is_os_type_Valid() const{
    return m_os_type_isValid;
}

QString OAIGalleryImageReferenceFragment::getPublisher() const {
    return m_publisher;
}
void OAIGalleryImageReferenceFragment::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIGalleryImageReferenceFragment::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIGalleryImageReferenceFragment::is_publisher_Valid() const{
    return m_publisher_isValid;
}

QString OAIGalleryImageReferenceFragment::getSku() const {
    return m_sku;
}
void OAIGalleryImageReferenceFragment::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIGalleryImageReferenceFragment::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIGalleryImageReferenceFragment::is_sku_Valid() const{
    return m_sku_isValid;
}

QString OAIGalleryImageReferenceFragment::getVersion() const {
    return m_version;
}
void OAIGalleryImageReferenceFragment::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIGalleryImageReferenceFragment::is_version_Set() const{
    return m_version_isSet;
}

bool OAIGalleryImageReferenceFragment::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIGalleryImageReferenceFragment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_offer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_type_isSet) {
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

bool OAIGalleryImageReferenceFragment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
