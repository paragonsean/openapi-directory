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

#include "OAISales_data_creditmemo_item_creation_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISales_data_creditmemo_item_creation_interface::OAISales_data_creditmemo_item_creation_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISales_data_creditmemo_item_creation_interface::OAISales_data_creditmemo_item_creation_interface() {
    this->initializeModel();
}

OAISales_data_creditmemo_item_creation_interface::~OAISales_data_creditmemo_item_creation_interface() {}

void OAISales_data_creditmemo_item_creation_interface::initializeModel() {

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_order_item_id_isSet = false;
    m_order_item_id_isValid = false;

    m_qty_isSet = false;
    m_qty_isValid = false;
}

void OAISales_data_creditmemo_item_creation_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISales_data_creditmemo_item_creation_interface::fromJsonObject(QJsonObject json) {

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_order_item_id_isValid = ::OpenAPI::fromJsonValue(m_order_item_id, json[QString("order_item_id")]);
    m_order_item_id_isSet = !json[QString("order_item_id")].isNull() && m_order_item_id_isValid;

    m_qty_isValid = ::OpenAPI::fromJsonValue(m_qty, json[QString("qty")]);
    m_qty_isSet = !json[QString("qty")].isNull() && m_qty_isValid;
}

QString OAISales_data_creditmemo_item_creation_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISales_data_creditmemo_item_creation_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_order_item_id_isSet) {
        obj.insert(QString("order_item_id"), ::OpenAPI::toJsonValue(m_order_item_id));
    }
    if (m_qty_isSet) {
        obj.insert(QString("qty"), ::OpenAPI::toJsonValue(m_qty));
    }
    return obj;
}

OAIObject OAISales_data_creditmemo_item_creation_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAISales_data_creditmemo_item_creation_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAISales_data_creditmemo_item_creation_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAISales_data_creditmemo_item_creation_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

qint32 OAISales_data_creditmemo_item_creation_interface::getOrderItemId() const {
    return m_order_item_id;
}
void OAISales_data_creditmemo_item_creation_interface::setOrderItemId(const qint32 &order_item_id) {
    m_order_item_id = order_item_id;
    m_order_item_id_isSet = true;
}

bool OAISales_data_creditmemo_item_creation_interface::is_order_item_id_Set() const{
    return m_order_item_id_isSet;
}

bool OAISales_data_creditmemo_item_creation_interface::is_order_item_id_Valid() const{
    return m_order_item_id_isValid;
}

double OAISales_data_creditmemo_item_creation_interface::getQty() const {
    return m_qty;
}
void OAISales_data_creditmemo_item_creation_interface::setQty(const double &qty) {
    m_qty = qty;
    m_qty_isSet = true;
}

bool OAISales_data_creditmemo_item_creation_interface::is_qty_Set() const{
    return m_qty_isSet;
}

bool OAISales_data_creditmemo_item_creation_interface::is_qty_Valid() const{
    return m_qty_isValid;
}

bool OAISales_data_creditmemo_item_creation_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISales_data_creditmemo_item_creation_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_order_item_id_isValid && m_qty_isValid && true;
}

} // namespace OpenAPI
