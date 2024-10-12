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

#include "OAIQuote_data_cart_item_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuote_data_cart_item_interface::OAIQuote_data_cart_item_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuote_data_cart_item_interface::OAIQuote_data_cart_item_interface() {
    this->initializeModel();
}

OAIQuote_data_cart_item_interface::~OAIQuote_data_cart_item_interface() {}

void OAIQuote_data_cart_item_interface::initializeModel() {

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_item_id_isSet = false;
    m_item_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_product_option_isSet = false;
    m_product_option_isValid = false;

    m_product_type_isSet = false;
    m_product_type_isValid = false;

    m_qty_isSet = false;
    m_qty_isValid = false;

    m_quote_id_isSet = false;
    m_quote_id_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;
}

void OAIQuote_data_cart_item_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuote_data_cart_item_interface::fromJsonObject(QJsonObject json) {

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_item_id_isValid = ::OpenAPI::fromJsonValue(m_item_id, json[QString("item_id")]);
    m_item_id_isSet = !json[QString("item_id")].isNull() && m_item_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_product_option_isValid = ::OpenAPI::fromJsonValue(m_product_option, json[QString("product_option")]);
    m_product_option_isSet = !json[QString("product_option")].isNull() && m_product_option_isValid;

    m_product_type_isValid = ::OpenAPI::fromJsonValue(m_product_type, json[QString("product_type")]);
    m_product_type_isSet = !json[QString("product_type")].isNull() && m_product_type_isValid;

    m_qty_isValid = ::OpenAPI::fromJsonValue(m_qty, json[QString("qty")]);
    m_qty_isSet = !json[QString("qty")].isNull() && m_qty_isValid;

    m_quote_id_isValid = ::OpenAPI::fromJsonValue(m_quote_id, json[QString("quote_id")]);
    m_quote_id_isSet = !json[QString("quote_id")].isNull() && m_quote_id_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;
}

QString OAIQuote_data_cart_item_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuote_data_cart_item_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_attributes.isSet()) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_item_id_isSet) {
        obj.insert(QString("item_id"), ::OpenAPI::toJsonValue(m_item_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_product_option.isSet()) {
        obj.insert(QString("product_option"), ::OpenAPI::toJsonValue(m_product_option));
    }
    if (m_product_type_isSet) {
        obj.insert(QString("product_type"), ::OpenAPI::toJsonValue(m_product_type));
    }
    if (m_qty_isSet) {
        obj.insert(QString("qty"), ::OpenAPI::toJsonValue(m_qty));
    }
    if (m_quote_id_isSet) {
        obj.insert(QString("quote_id"), ::OpenAPI::toJsonValue(m_quote_id));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    return obj;
}

OAIQuote_data_cart_item_extension_interface OAIQuote_data_cart_item_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAIQuote_data_cart_item_interface::setExtensionAttributes(const OAIQuote_data_cart_item_extension_interface &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAIQuote_data_cart_item_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

qint32 OAIQuote_data_cart_item_interface::getItemId() const {
    return m_item_id;
}
void OAIQuote_data_cart_item_interface::setItemId(const qint32 &item_id) {
    m_item_id = item_id;
    m_item_id_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_item_id_Set() const{
    return m_item_id_isSet;
}

bool OAIQuote_data_cart_item_interface::is_item_id_Valid() const{
    return m_item_id_isValid;
}

QString OAIQuote_data_cart_item_interface::getName() const {
    return m_name;
}
void OAIQuote_data_cart_item_interface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_name_Set() const{
    return m_name_isSet;
}

bool OAIQuote_data_cart_item_interface::is_name_Valid() const{
    return m_name_isValid;
}

double OAIQuote_data_cart_item_interface::getPrice() const {
    return m_price;
}
void OAIQuote_data_cart_item_interface::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_price_Set() const{
    return m_price_isSet;
}

bool OAIQuote_data_cart_item_interface::is_price_Valid() const{
    return m_price_isValid;
}

OAIQuote_data_product_option_interface OAIQuote_data_cart_item_interface::getProductOption() const {
    return m_product_option;
}
void OAIQuote_data_cart_item_interface::setProductOption(const OAIQuote_data_product_option_interface &product_option) {
    m_product_option = product_option;
    m_product_option_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_product_option_Set() const{
    return m_product_option_isSet;
}

bool OAIQuote_data_cart_item_interface::is_product_option_Valid() const{
    return m_product_option_isValid;
}

QString OAIQuote_data_cart_item_interface::getProductType() const {
    return m_product_type;
}
void OAIQuote_data_cart_item_interface::setProductType(const QString &product_type) {
    m_product_type = product_type;
    m_product_type_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_product_type_Set() const{
    return m_product_type_isSet;
}

bool OAIQuote_data_cart_item_interface::is_product_type_Valid() const{
    return m_product_type_isValid;
}

double OAIQuote_data_cart_item_interface::getQty() const {
    return m_qty;
}
void OAIQuote_data_cart_item_interface::setQty(const double &qty) {
    m_qty = qty;
    m_qty_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_qty_Set() const{
    return m_qty_isSet;
}

bool OAIQuote_data_cart_item_interface::is_qty_Valid() const{
    return m_qty_isValid;
}

QString OAIQuote_data_cart_item_interface::getQuoteId() const {
    return m_quote_id;
}
void OAIQuote_data_cart_item_interface::setQuoteId(const QString &quote_id) {
    m_quote_id = quote_id;
    m_quote_id_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_quote_id_Set() const{
    return m_quote_id_isSet;
}

bool OAIQuote_data_cart_item_interface::is_quote_id_Valid() const{
    return m_quote_id_isValid;
}

QString OAIQuote_data_cart_item_interface::getSku() const {
    return m_sku;
}
void OAIQuote_data_cart_item_interface::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIQuote_data_cart_item_interface::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIQuote_data_cart_item_interface::is_sku_Valid() const{
    return m_sku_isValid;
}

bool OAIQuote_data_cart_item_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_option.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuote_data_cart_item_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_qty_isValid && m_quote_id_isValid && true;
}

} // namespace OpenAPI
