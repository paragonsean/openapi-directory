/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICatalog_data_special_price_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalog_data_special_price_interface::OAICatalog_data_special_price_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalog_data_special_price_interface::OAICatalog_data_special_price_interface() {
    this->initializeModel();
}

OAICatalog_data_special_price_interface::~OAICatalog_data_special_price_interface() {}

void OAICatalog_data_special_price_interface::initializeModel() {

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_from_isSet = false;
    m_price_from_isValid = false;

    m_price_to_isSet = false;
    m_price_to_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;
}

void OAICatalog_data_special_price_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalog_data_special_price_interface::fromJsonObject(QJsonObject json) {

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_from_isValid = ::OpenAPI::fromJsonValue(m_price_from, json[QString("price_from")]);
    m_price_from_isSet = !json[QString("price_from")].isNull() && m_price_from_isValid;

    m_price_to_isValid = ::OpenAPI::fromJsonValue(m_price_to, json[QString("price_to")]);
    m_price_to_isSet = !json[QString("price_to")].isNull() && m_price_to_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("store_id")]);
    m_store_id_isSet = !json[QString("store_id")].isNull() && m_store_id_isValid;
}

QString OAICatalog_data_special_price_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalog_data_special_price_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_from_isSet) {
        obj.insert(QString("price_from"), ::OpenAPI::toJsonValue(m_price_from));
    }
    if (m_price_to_isSet) {
        obj.insert(QString("price_to"), ::OpenAPI::toJsonValue(m_price_to));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("store_id"), ::OpenAPI::toJsonValue(m_store_id));
    }
    return obj;
}

OAIObject OAICatalog_data_special_price_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAICatalog_data_special_price_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAICatalog_data_special_price_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

double OAICatalog_data_special_price_interface::getPrice() const {
    return m_price;
}
void OAICatalog_data_special_price_interface::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_price_Set() const{
    return m_price_isSet;
}

bool OAICatalog_data_special_price_interface::is_price_Valid() const{
    return m_price_isValid;
}

QString OAICatalog_data_special_price_interface::getPriceFrom() const {
    return m_price_from;
}
void OAICatalog_data_special_price_interface::setPriceFrom(const QString &price_from) {
    m_price_from = price_from;
    m_price_from_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_price_from_Set() const{
    return m_price_from_isSet;
}

bool OAICatalog_data_special_price_interface::is_price_from_Valid() const{
    return m_price_from_isValid;
}

QString OAICatalog_data_special_price_interface::getPriceTo() const {
    return m_price_to;
}
void OAICatalog_data_special_price_interface::setPriceTo(const QString &price_to) {
    m_price_to = price_to;
    m_price_to_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_price_to_Set() const{
    return m_price_to_isSet;
}

bool OAICatalog_data_special_price_interface::is_price_to_Valid() const{
    return m_price_to_isValid;
}

QString OAICatalog_data_special_price_interface::getSku() const {
    return m_sku;
}
void OAICatalog_data_special_price_interface::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAICatalog_data_special_price_interface::is_sku_Valid() const{
    return m_sku_isValid;
}

qint32 OAICatalog_data_special_price_interface::getStoreId() const {
    return m_store_id;
}
void OAICatalog_data_special_price_interface::setStoreId(const qint32 &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAICatalog_data_special_price_interface::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAICatalog_data_special_price_interface::is_store_id_Valid() const{
    return m_store_id_isValid;
}

bool OAICatalog_data_special_price_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalog_data_special_price_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_price_isValid && m_price_from_isValid && m_price_to_isValid && m_sku_isValid && m_store_id_isValid && true;
}

} // namespace OpenAPI
