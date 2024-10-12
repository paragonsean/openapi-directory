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

#include "OAICatalog_inventory_data_stock_item_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalog_inventory_data_stock_item_interface::OAICatalog_inventory_data_stock_item_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalog_inventory_data_stock_item_interface::OAICatalog_inventory_data_stock_item_interface() {
    this->initializeModel();
}

OAICatalog_inventory_data_stock_item_interface::~OAICatalog_inventory_data_stock_item_interface() {}

void OAICatalog_inventory_data_stock_item_interface::initializeModel() {

    m_backorders_isSet = false;
    m_backorders_isValid = false;

    m_enable_qty_increments_isSet = false;
    m_enable_qty_increments_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_is_decimal_divided_isSet = false;
    m_is_decimal_divided_isValid = false;

    m_is_in_stock_isSet = false;
    m_is_in_stock_isValid = false;

    m_is_qty_decimal_isSet = false;
    m_is_qty_decimal_isValid = false;

    m_item_id_isSet = false;
    m_item_id_isValid = false;

    m_low_stock_date_isSet = false;
    m_low_stock_date_isValid = false;

    m_manage_stock_isSet = false;
    m_manage_stock_isValid = false;

    m_max_sale_qty_isSet = false;
    m_max_sale_qty_isValid = false;

    m_min_qty_isSet = false;
    m_min_qty_isValid = false;

    m_min_sale_qty_isSet = false;
    m_min_sale_qty_isValid = false;

    m_notify_stock_qty_isSet = false;
    m_notify_stock_qty_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_qty_isSet = false;
    m_qty_isValid = false;

    m_qty_increments_isSet = false;
    m_qty_increments_isValid = false;

    m_show_default_notification_message_isSet = false;
    m_show_default_notification_message_isValid = false;

    m_stock_id_isSet = false;
    m_stock_id_isValid = false;

    m_stock_status_changed_auto_isSet = false;
    m_stock_status_changed_auto_isValid = false;

    m_use_config_backorders_isSet = false;
    m_use_config_backorders_isValid = false;

    m_use_config_enable_qty_inc_isSet = false;
    m_use_config_enable_qty_inc_isValid = false;

    m_use_config_manage_stock_isSet = false;
    m_use_config_manage_stock_isValid = false;

    m_use_config_max_sale_qty_isSet = false;
    m_use_config_max_sale_qty_isValid = false;

    m_use_config_min_qty_isSet = false;
    m_use_config_min_qty_isValid = false;

    m_use_config_min_sale_qty_isSet = false;
    m_use_config_min_sale_qty_isValid = false;

    m_use_config_notify_stock_qty_isSet = false;
    m_use_config_notify_stock_qty_isValid = false;

    m_use_config_qty_increments_isSet = false;
    m_use_config_qty_increments_isValid = false;
}

void OAICatalog_inventory_data_stock_item_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalog_inventory_data_stock_item_interface::fromJsonObject(QJsonObject json) {

    m_backorders_isValid = ::OpenAPI::fromJsonValue(m_backorders, json[QString("backorders")]);
    m_backorders_isSet = !json[QString("backorders")].isNull() && m_backorders_isValid;

    m_enable_qty_increments_isValid = ::OpenAPI::fromJsonValue(m_enable_qty_increments, json[QString("enable_qty_increments")]);
    m_enable_qty_increments_isSet = !json[QString("enable_qty_increments")].isNull() && m_enable_qty_increments_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_is_decimal_divided_isValid = ::OpenAPI::fromJsonValue(m_is_decimal_divided, json[QString("is_decimal_divided")]);
    m_is_decimal_divided_isSet = !json[QString("is_decimal_divided")].isNull() && m_is_decimal_divided_isValid;

    m_is_in_stock_isValid = ::OpenAPI::fromJsonValue(m_is_in_stock, json[QString("is_in_stock")]);
    m_is_in_stock_isSet = !json[QString("is_in_stock")].isNull() && m_is_in_stock_isValid;

    m_is_qty_decimal_isValid = ::OpenAPI::fromJsonValue(m_is_qty_decimal, json[QString("is_qty_decimal")]);
    m_is_qty_decimal_isSet = !json[QString("is_qty_decimal")].isNull() && m_is_qty_decimal_isValid;

    m_item_id_isValid = ::OpenAPI::fromJsonValue(m_item_id, json[QString("item_id")]);
    m_item_id_isSet = !json[QString("item_id")].isNull() && m_item_id_isValid;

    m_low_stock_date_isValid = ::OpenAPI::fromJsonValue(m_low_stock_date, json[QString("low_stock_date")]);
    m_low_stock_date_isSet = !json[QString("low_stock_date")].isNull() && m_low_stock_date_isValid;

    m_manage_stock_isValid = ::OpenAPI::fromJsonValue(m_manage_stock, json[QString("manage_stock")]);
    m_manage_stock_isSet = !json[QString("manage_stock")].isNull() && m_manage_stock_isValid;

    m_max_sale_qty_isValid = ::OpenAPI::fromJsonValue(m_max_sale_qty, json[QString("max_sale_qty")]);
    m_max_sale_qty_isSet = !json[QString("max_sale_qty")].isNull() && m_max_sale_qty_isValid;

    m_min_qty_isValid = ::OpenAPI::fromJsonValue(m_min_qty, json[QString("min_qty")]);
    m_min_qty_isSet = !json[QString("min_qty")].isNull() && m_min_qty_isValid;

    m_min_sale_qty_isValid = ::OpenAPI::fromJsonValue(m_min_sale_qty, json[QString("min_sale_qty")]);
    m_min_sale_qty_isSet = !json[QString("min_sale_qty")].isNull() && m_min_sale_qty_isValid;

    m_notify_stock_qty_isValid = ::OpenAPI::fromJsonValue(m_notify_stock_qty, json[QString("notify_stock_qty")]);
    m_notify_stock_qty_isSet = !json[QString("notify_stock_qty")].isNull() && m_notify_stock_qty_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_qty_isValid = ::OpenAPI::fromJsonValue(m_qty, json[QString("qty")]);
    m_qty_isSet = !json[QString("qty")].isNull() && m_qty_isValid;

    m_qty_increments_isValid = ::OpenAPI::fromJsonValue(m_qty_increments, json[QString("qty_increments")]);
    m_qty_increments_isSet = !json[QString("qty_increments")].isNull() && m_qty_increments_isValid;

    m_show_default_notification_message_isValid = ::OpenAPI::fromJsonValue(m_show_default_notification_message, json[QString("show_default_notification_message")]);
    m_show_default_notification_message_isSet = !json[QString("show_default_notification_message")].isNull() && m_show_default_notification_message_isValid;

    m_stock_id_isValid = ::OpenAPI::fromJsonValue(m_stock_id, json[QString("stock_id")]);
    m_stock_id_isSet = !json[QString("stock_id")].isNull() && m_stock_id_isValid;

    m_stock_status_changed_auto_isValid = ::OpenAPI::fromJsonValue(m_stock_status_changed_auto, json[QString("stock_status_changed_auto")]);
    m_stock_status_changed_auto_isSet = !json[QString("stock_status_changed_auto")].isNull() && m_stock_status_changed_auto_isValid;

    m_use_config_backorders_isValid = ::OpenAPI::fromJsonValue(m_use_config_backorders, json[QString("use_config_backorders")]);
    m_use_config_backorders_isSet = !json[QString("use_config_backorders")].isNull() && m_use_config_backorders_isValid;

    m_use_config_enable_qty_inc_isValid = ::OpenAPI::fromJsonValue(m_use_config_enable_qty_inc, json[QString("use_config_enable_qty_inc")]);
    m_use_config_enable_qty_inc_isSet = !json[QString("use_config_enable_qty_inc")].isNull() && m_use_config_enable_qty_inc_isValid;

    m_use_config_manage_stock_isValid = ::OpenAPI::fromJsonValue(m_use_config_manage_stock, json[QString("use_config_manage_stock")]);
    m_use_config_manage_stock_isSet = !json[QString("use_config_manage_stock")].isNull() && m_use_config_manage_stock_isValid;

    m_use_config_max_sale_qty_isValid = ::OpenAPI::fromJsonValue(m_use_config_max_sale_qty, json[QString("use_config_max_sale_qty")]);
    m_use_config_max_sale_qty_isSet = !json[QString("use_config_max_sale_qty")].isNull() && m_use_config_max_sale_qty_isValid;

    m_use_config_min_qty_isValid = ::OpenAPI::fromJsonValue(m_use_config_min_qty, json[QString("use_config_min_qty")]);
    m_use_config_min_qty_isSet = !json[QString("use_config_min_qty")].isNull() && m_use_config_min_qty_isValid;

    m_use_config_min_sale_qty_isValid = ::OpenAPI::fromJsonValue(m_use_config_min_sale_qty, json[QString("use_config_min_sale_qty")]);
    m_use_config_min_sale_qty_isSet = !json[QString("use_config_min_sale_qty")].isNull() && m_use_config_min_sale_qty_isValid;

    m_use_config_notify_stock_qty_isValid = ::OpenAPI::fromJsonValue(m_use_config_notify_stock_qty, json[QString("use_config_notify_stock_qty")]);
    m_use_config_notify_stock_qty_isSet = !json[QString("use_config_notify_stock_qty")].isNull() && m_use_config_notify_stock_qty_isValid;

    m_use_config_qty_increments_isValid = ::OpenAPI::fromJsonValue(m_use_config_qty_increments, json[QString("use_config_qty_increments")]);
    m_use_config_qty_increments_isSet = !json[QString("use_config_qty_increments")].isNull() && m_use_config_qty_increments_isValid;
}

QString OAICatalog_inventory_data_stock_item_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalog_inventory_data_stock_item_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_backorders_isSet) {
        obj.insert(QString("backorders"), ::OpenAPI::toJsonValue(m_backorders));
    }
    if (m_enable_qty_increments_isSet) {
        obj.insert(QString("enable_qty_increments"), ::OpenAPI::toJsonValue(m_enable_qty_increments));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_is_decimal_divided_isSet) {
        obj.insert(QString("is_decimal_divided"), ::OpenAPI::toJsonValue(m_is_decimal_divided));
    }
    if (m_is_in_stock_isSet) {
        obj.insert(QString("is_in_stock"), ::OpenAPI::toJsonValue(m_is_in_stock));
    }
    if (m_is_qty_decimal_isSet) {
        obj.insert(QString("is_qty_decimal"), ::OpenAPI::toJsonValue(m_is_qty_decimal));
    }
    if (m_item_id_isSet) {
        obj.insert(QString("item_id"), ::OpenAPI::toJsonValue(m_item_id));
    }
    if (m_low_stock_date_isSet) {
        obj.insert(QString("low_stock_date"), ::OpenAPI::toJsonValue(m_low_stock_date));
    }
    if (m_manage_stock_isSet) {
        obj.insert(QString("manage_stock"), ::OpenAPI::toJsonValue(m_manage_stock));
    }
    if (m_max_sale_qty_isSet) {
        obj.insert(QString("max_sale_qty"), ::OpenAPI::toJsonValue(m_max_sale_qty));
    }
    if (m_min_qty_isSet) {
        obj.insert(QString("min_qty"), ::OpenAPI::toJsonValue(m_min_qty));
    }
    if (m_min_sale_qty_isSet) {
        obj.insert(QString("min_sale_qty"), ::OpenAPI::toJsonValue(m_min_sale_qty));
    }
    if (m_notify_stock_qty_isSet) {
        obj.insert(QString("notify_stock_qty"), ::OpenAPI::toJsonValue(m_notify_stock_qty));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_qty_isSet) {
        obj.insert(QString("qty"), ::OpenAPI::toJsonValue(m_qty));
    }
    if (m_qty_increments_isSet) {
        obj.insert(QString("qty_increments"), ::OpenAPI::toJsonValue(m_qty_increments));
    }
    if (m_show_default_notification_message_isSet) {
        obj.insert(QString("show_default_notification_message"), ::OpenAPI::toJsonValue(m_show_default_notification_message));
    }
    if (m_stock_id_isSet) {
        obj.insert(QString("stock_id"), ::OpenAPI::toJsonValue(m_stock_id));
    }
    if (m_stock_status_changed_auto_isSet) {
        obj.insert(QString("stock_status_changed_auto"), ::OpenAPI::toJsonValue(m_stock_status_changed_auto));
    }
    if (m_use_config_backorders_isSet) {
        obj.insert(QString("use_config_backorders"), ::OpenAPI::toJsonValue(m_use_config_backorders));
    }
    if (m_use_config_enable_qty_inc_isSet) {
        obj.insert(QString("use_config_enable_qty_inc"), ::OpenAPI::toJsonValue(m_use_config_enable_qty_inc));
    }
    if (m_use_config_manage_stock_isSet) {
        obj.insert(QString("use_config_manage_stock"), ::OpenAPI::toJsonValue(m_use_config_manage_stock));
    }
    if (m_use_config_max_sale_qty_isSet) {
        obj.insert(QString("use_config_max_sale_qty"), ::OpenAPI::toJsonValue(m_use_config_max_sale_qty));
    }
    if (m_use_config_min_qty_isSet) {
        obj.insert(QString("use_config_min_qty"), ::OpenAPI::toJsonValue(m_use_config_min_qty));
    }
    if (m_use_config_min_sale_qty_isSet) {
        obj.insert(QString("use_config_min_sale_qty"), ::OpenAPI::toJsonValue(m_use_config_min_sale_qty));
    }
    if (m_use_config_notify_stock_qty_isSet) {
        obj.insert(QString("use_config_notify_stock_qty"), ::OpenAPI::toJsonValue(m_use_config_notify_stock_qty));
    }
    if (m_use_config_qty_increments_isSet) {
        obj.insert(QString("use_config_qty_increments"), ::OpenAPI::toJsonValue(m_use_config_qty_increments));
    }
    return obj;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getBackorders() const {
    return m_backorders;
}
void OAICatalog_inventory_data_stock_item_interface::setBackorders(const qint32 &backorders) {
    m_backorders = backorders;
    m_backorders_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_backorders_Set() const{
    return m_backorders_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_backorders_Valid() const{
    return m_backorders_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isEnableQtyIncrements() const {
    return m_enable_qty_increments;
}
void OAICatalog_inventory_data_stock_item_interface::setEnableQtyIncrements(const bool &enable_qty_increments) {
    m_enable_qty_increments = enable_qty_increments;
    m_enable_qty_increments_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_enable_qty_increments_Set() const{
    return m_enable_qty_increments_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_enable_qty_increments_Valid() const{
    return m_enable_qty_increments_isValid;
}

OAIObject OAICatalog_inventory_data_stock_item_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAICatalog_inventory_data_stock_item_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isIsDecimalDivided() const {
    return m_is_decimal_divided;
}
void OAICatalog_inventory_data_stock_item_interface::setIsDecimalDivided(const bool &is_decimal_divided) {
    m_is_decimal_divided = is_decimal_divided;
    m_is_decimal_divided_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_decimal_divided_Set() const{
    return m_is_decimal_divided_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_decimal_divided_Valid() const{
    return m_is_decimal_divided_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isIsInStock() const {
    return m_is_in_stock;
}
void OAICatalog_inventory_data_stock_item_interface::setIsInStock(const bool &is_in_stock) {
    m_is_in_stock = is_in_stock;
    m_is_in_stock_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_in_stock_Set() const{
    return m_is_in_stock_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_in_stock_Valid() const{
    return m_is_in_stock_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isIsQtyDecimal() const {
    return m_is_qty_decimal;
}
void OAICatalog_inventory_data_stock_item_interface::setIsQtyDecimal(const bool &is_qty_decimal) {
    m_is_qty_decimal = is_qty_decimal;
    m_is_qty_decimal_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_qty_decimal_Set() const{
    return m_is_qty_decimal_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_is_qty_decimal_Valid() const{
    return m_is_qty_decimal_isValid;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getItemId() const {
    return m_item_id;
}
void OAICatalog_inventory_data_stock_item_interface::setItemId(const qint32 &item_id) {
    m_item_id = item_id;
    m_item_id_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_item_id_Set() const{
    return m_item_id_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_item_id_Valid() const{
    return m_item_id_isValid;
}

QString OAICatalog_inventory_data_stock_item_interface::getLowStockDate() const {
    return m_low_stock_date;
}
void OAICatalog_inventory_data_stock_item_interface::setLowStockDate(const QString &low_stock_date) {
    m_low_stock_date = low_stock_date;
    m_low_stock_date_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_low_stock_date_Set() const{
    return m_low_stock_date_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_low_stock_date_Valid() const{
    return m_low_stock_date_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isManageStock() const {
    return m_manage_stock;
}
void OAICatalog_inventory_data_stock_item_interface::setManageStock(const bool &manage_stock) {
    m_manage_stock = manage_stock;
    m_manage_stock_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_manage_stock_Set() const{
    return m_manage_stock_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_manage_stock_Valid() const{
    return m_manage_stock_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getMaxSaleQty() const {
    return m_max_sale_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setMaxSaleQty(const double &max_sale_qty) {
    m_max_sale_qty = max_sale_qty;
    m_max_sale_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_max_sale_qty_Set() const{
    return m_max_sale_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_max_sale_qty_Valid() const{
    return m_max_sale_qty_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getMinQty() const {
    return m_min_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setMinQty(const double &min_qty) {
    m_min_qty = min_qty;
    m_min_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_min_qty_Set() const{
    return m_min_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_min_qty_Valid() const{
    return m_min_qty_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getMinSaleQty() const {
    return m_min_sale_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setMinSaleQty(const double &min_sale_qty) {
    m_min_sale_qty = min_sale_qty;
    m_min_sale_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_min_sale_qty_Set() const{
    return m_min_sale_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_min_sale_qty_Valid() const{
    return m_min_sale_qty_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getNotifyStockQty() const {
    return m_notify_stock_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setNotifyStockQty(const double &notify_stock_qty) {
    m_notify_stock_qty = notify_stock_qty;
    m_notify_stock_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_notify_stock_qty_Set() const{
    return m_notify_stock_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_notify_stock_qty_Valid() const{
    return m_notify_stock_qty_isValid;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getProductId() const {
    return m_product_id;
}
void OAICatalog_inventory_data_stock_item_interface::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_product_id_Valid() const{
    return m_product_id_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getQty() const {
    return m_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setQty(const double &qty) {
    m_qty = qty;
    m_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_qty_Set() const{
    return m_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_qty_Valid() const{
    return m_qty_isValid;
}

double OAICatalog_inventory_data_stock_item_interface::getQtyIncrements() const {
    return m_qty_increments;
}
void OAICatalog_inventory_data_stock_item_interface::setQtyIncrements(const double &qty_increments) {
    m_qty_increments = qty_increments;
    m_qty_increments_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_qty_increments_Set() const{
    return m_qty_increments_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_qty_increments_Valid() const{
    return m_qty_increments_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isShowDefaultNotificationMessage() const {
    return m_show_default_notification_message;
}
void OAICatalog_inventory_data_stock_item_interface::setShowDefaultNotificationMessage(const bool &show_default_notification_message) {
    m_show_default_notification_message = show_default_notification_message;
    m_show_default_notification_message_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_show_default_notification_message_Set() const{
    return m_show_default_notification_message_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_show_default_notification_message_Valid() const{
    return m_show_default_notification_message_isValid;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getStockId() const {
    return m_stock_id;
}
void OAICatalog_inventory_data_stock_item_interface::setStockId(const qint32 &stock_id) {
    m_stock_id = stock_id;
    m_stock_id_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_stock_id_Set() const{
    return m_stock_id_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_stock_id_Valid() const{
    return m_stock_id_isValid;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getStockStatusChangedAuto() const {
    return m_stock_status_changed_auto;
}
void OAICatalog_inventory_data_stock_item_interface::setStockStatusChangedAuto(const qint32 &stock_status_changed_auto) {
    m_stock_status_changed_auto = stock_status_changed_auto;
    m_stock_status_changed_auto_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_stock_status_changed_auto_Set() const{
    return m_stock_status_changed_auto_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_stock_status_changed_auto_Valid() const{
    return m_stock_status_changed_auto_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigBackorders() const {
    return m_use_config_backorders;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigBackorders(const bool &use_config_backorders) {
    m_use_config_backorders = use_config_backorders;
    m_use_config_backorders_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_backorders_Set() const{
    return m_use_config_backorders_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_backorders_Valid() const{
    return m_use_config_backorders_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigEnableQtyInc() const {
    return m_use_config_enable_qty_inc;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigEnableQtyInc(const bool &use_config_enable_qty_inc) {
    m_use_config_enable_qty_inc = use_config_enable_qty_inc;
    m_use_config_enable_qty_inc_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_enable_qty_inc_Set() const{
    return m_use_config_enable_qty_inc_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_enable_qty_inc_Valid() const{
    return m_use_config_enable_qty_inc_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigManageStock() const {
    return m_use_config_manage_stock;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigManageStock(const bool &use_config_manage_stock) {
    m_use_config_manage_stock = use_config_manage_stock;
    m_use_config_manage_stock_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_manage_stock_Set() const{
    return m_use_config_manage_stock_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_manage_stock_Valid() const{
    return m_use_config_manage_stock_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigMaxSaleQty() const {
    return m_use_config_max_sale_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigMaxSaleQty(const bool &use_config_max_sale_qty) {
    m_use_config_max_sale_qty = use_config_max_sale_qty;
    m_use_config_max_sale_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_max_sale_qty_Set() const{
    return m_use_config_max_sale_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_max_sale_qty_Valid() const{
    return m_use_config_max_sale_qty_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigMinQty() const {
    return m_use_config_min_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigMinQty(const bool &use_config_min_qty) {
    m_use_config_min_qty = use_config_min_qty;
    m_use_config_min_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_min_qty_Set() const{
    return m_use_config_min_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_min_qty_Valid() const{
    return m_use_config_min_qty_isValid;
}

qint32 OAICatalog_inventory_data_stock_item_interface::getUseConfigMinSaleQty() const {
    return m_use_config_min_sale_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigMinSaleQty(const qint32 &use_config_min_sale_qty) {
    m_use_config_min_sale_qty = use_config_min_sale_qty;
    m_use_config_min_sale_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_min_sale_qty_Set() const{
    return m_use_config_min_sale_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_min_sale_qty_Valid() const{
    return m_use_config_min_sale_qty_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigNotifyStockQty() const {
    return m_use_config_notify_stock_qty;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigNotifyStockQty(const bool &use_config_notify_stock_qty) {
    m_use_config_notify_stock_qty = use_config_notify_stock_qty;
    m_use_config_notify_stock_qty_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_notify_stock_qty_Set() const{
    return m_use_config_notify_stock_qty_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_notify_stock_qty_Valid() const{
    return m_use_config_notify_stock_qty_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isUseConfigQtyIncrements() const {
    return m_use_config_qty_increments;
}
void OAICatalog_inventory_data_stock_item_interface::setUseConfigQtyIncrements(const bool &use_config_qty_increments) {
    m_use_config_qty_increments = use_config_qty_increments;
    m_use_config_qty_increments_isSet = true;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_qty_increments_Set() const{
    return m_use_config_qty_increments_isSet;
}

bool OAICatalog_inventory_data_stock_item_interface::is_use_config_qty_increments_Valid() const{
    return m_use_config_qty_increments_isValid;
}

bool OAICatalog_inventory_data_stock_item_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_backorders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_qty_increments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_decimal_divided_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_in_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_qty_decimal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_low_stock_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manage_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_sale_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_sale_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notify_stock_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_increments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_default_notification_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_status_changed_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_backorders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_enable_qty_inc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_manage_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_max_sale_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_min_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_min_sale_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_notify_stock_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_config_qty_increments_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalog_inventory_data_stock_item_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_backorders_isValid && m_enable_qty_increments_isValid && m_is_decimal_divided_isValid && m_is_in_stock_isValid && m_is_qty_decimal_isValid && m_low_stock_date_isValid && m_manage_stock_isValid && m_max_sale_qty_isValid && m_min_qty_isValid && m_min_sale_qty_isValid && m_notify_stock_qty_isValid && m_qty_isValid && m_qty_increments_isValid && m_show_default_notification_message_isValid && m_stock_status_changed_auto_isValid && m_use_config_backorders_isValid && m_use_config_enable_qty_inc_isValid && m_use_config_manage_stock_isValid && m_use_config_max_sale_qty_isValid && m_use_config_min_qty_isValid && m_use_config_min_sale_qty_isValid && m_use_config_notify_stock_qty_isValid && m_use_config_qty_increments_isValid && true;
}

} // namespace OpenAPI
