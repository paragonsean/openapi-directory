/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOrderRefundAdd.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderRefundAdd::OAIOrderRefundAdd(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderRefundAdd::OAIOrderRefundAdd() {
    this->initializeModel();
}

OAIOrderRefundAdd::~OAIOrderRefundAdd() {}

void OAIOrderRefundAdd::initializeModel() {

    m_date_isSet = false;
    m_date_isValid = false;

    m_fee_price_isSet = false;
    m_fee_price_isValid = false;

    m_is_online_isSet = false;
    m_is_online_isValid = false;

    m_item_restock_isSet = false;
    m_item_restock_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_order_id_isSet = false;
    m_order_id_isValid = false;

    m_send_notifications_isSet = false;
    m_send_notifications_isValid = false;

    m_shipping_price_isSet = false;
    m_shipping_price_isValid = false;

    m_total_price_isSet = false;
    m_total_price_isValid = false;
}

void OAIOrderRefundAdd::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderRefundAdd::fromJsonObject(QJsonObject json) {

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_fee_price_isValid = ::OpenAPI::fromJsonValue(m_fee_price, json[QString("fee_price")]);
    m_fee_price_isSet = !json[QString("fee_price")].isNull() && m_fee_price_isValid;

    m_is_online_isValid = ::OpenAPI::fromJsonValue(m_is_online, json[QString("is_online")]);
    m_is_online_isSet = !json[QString("is_online")].isNull() && m_is_online_isValid;

    m_item_restock_isValid = ::OpenAPI::fromJsonValue(m_item_restock, json[QString("item_restock")]);
    m_item_restock_isSet = !json[QString("item_restock")].isNull() && m_item_restock_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_order_id_isValid = ::OpenAPI::fromJsonValue(m_order_id, json[QString("order_id")]);
    m_order_id_isSet = !json[QString("order_id")].isNull() && m_order_id_isValid;

    m_send_notifications_isValid = ::OpenAPI::fromJsonValue(m_send_notifications, json[QString("send_notifications")]);
    m_send_notifications_isSet = !json[QString("send_notifications")].isNull() && m_send_notifications_isValid;

    m_shipping_price_isValid = ::OpenAPI::fromJsonValue(m_shipping_price, json[QString("shipping_price")]);
    m_shipping_price_isSet = !json[QString("shipping_price")].isNull() && m_shipping_price_isValid;

    m_total_price_isValid = ::OpenAPI::fromJsonValue(m_total_price, json[QString("total_price")]);
    m_total_price_isSet = !json[QString("total_price")].isNull() && m_total_price_isValid;
}

QString OAIOrderRefundAdd::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderRefundAdd::asJsonObject() const {
    QJsonObject obj;
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_fee_price_isSet) {
        obj.insert(QString("fee_price"), ::OpenAPI::toJsonValue(m_fee_price));
    }
    if (m_is_online_isSet) {
        obj.insert(QString("is_online"), ::OpenAPI::toJsonValue(m_is_online));
    }
    if (m_item_restock_isSet) {
        obj.insert(QString("item_restock"), ::OpenAPI::toJsonValue(m_item_restock));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_order_id_isSet) {
        obj.insert(QString("order_id"), ::OpenAPI::toJsonValue(m_order_id));
    }
    if (m_send_notifications_isSet) {
        obj.insert(QString("send_notifications"), ::OpenAPI::toJsonValue(m_send_notifications));
    }
    if (m_shipping_price_isSet) {
        obj.insert(QString("shipping_price"), ::OpenAPI::toJsonValue(m_shipping_price));
    }
    if (m_total_price_isSet) {
        obj.insert(QString("total_price"), ::OpenAPI::toJsonValue(m_total_price));
    }
    return obj;
}

QString OAIOrderRefundAdd::getDate() const {
    return m_date;
}
void OAIOrderRefundAdd::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIOrderRefundAdd::is_date_Set() const{
    return m_date_isSet;
}

bool OAIOrderRefundAdd::is_date_Valid() const{
    return m_date_isValid;
}

double OAIOrderRefundAdd::getFeePrice() const {
    return m_fee_price;
}
void OAIOrderRefundAdd::setFeePrice(const double &fee_price) {
    m_fee_price = fee_price;
    m_fee_price_isSet = true;
}

bool OAIOrderRefundAdd::is_fee_price_Set() const{
    return m_fee_price_isSet;
}

bool OAIOrderRefundAdd::is_fee_price_Valid() const{
    return m_fee_price_isValid;
}

bool OAIOrderRefundAdd::isIsOnline() const {
    return m_is_online;
}
void OAIOrderRefundAdd::setIsOnline(const bool &is_online) {
    m_is_online = is_online;
    m_is_online_isSet = true;
}

bool OAIOrderRefundAdd::is_is_online_Set() const{
    return m_is_online_isSet;
}

bool OAIOrderRefundAdd::is_is_online_Valid() const{
    return m_is_online_isValid;
}

bool OAIOrderRefundAdd::isItemRestock() const {
    return m_item_restock;
}
void OAIOrderRefundAdd::setItemRestock(const bool &item_restock) {
    m_item_restock = item_restock;
    m_item_restock_isSet = true;
}

bool OAIOrderRefundAdd::is_item_restock_Set() const{
    return m_item_restock_isSet;
}

bool OAIOrderRefundAdd::is_item_restock_Valid() const{
    return m_item_restock_isValid;
}

QList<OAIOrderRefundAdd_items_inner> OAIOrderRefundAdd::getItems() const {
    return m_items;
}
void OAIOrderRefundAdd::setItems(const QList<OAIOrderRefundAdd_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIOrderRefundAdd::is_items_Set() const{
    return m_items_isSet;
}

bool OAIOrderRefundAdd::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIOrderRefundAdd::getMessage() const {
    return m_message;
}
void OAIOrderRefundAdd::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIOrderRefundAdd::is_message_Set() const{
    return m_message_isSet;
}

bool OAIOrderRefundAdd::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIOrderRefundAdd::getOrderId() const {
    return m_order_id;
}
void OAIOrderRefundAdd::setOrderId(const QString &order_id) {
    m_order_id = order_id;
    m_order_id_isSet = true;
}

bool OAIOrderRefundAdd::is_order_id_Set() const{
    return m_order_id_isSet;
}

bool OAIOrderRefundAdd::is_order_id_Valid() const{
    return m_order_id_isValid;
}

bool OAIOrderRefundAdd::isSendNotifications() const {
    return m_send_notifications;
}
void OAIOrderRefundAdd::setSendNotifications(const bool &send_notifications) {
    m_send_notifications = send_notifications;
    m_send_notifications_isSet = true;
}

bool OAIOrderRefundAdd::is_send_notifications_Set() const{
    return m_send_notifications_isSet;
}

bool OAIOrderRefundAdd::is_send_notifications_Valid() const{
    return m_send_notifications_isValid;
}

double OAIOrderRefundAdd::getShippingPrice() const {
    return m_shipping_price;
}
void OAIOrderRefundAdd::setShippingPrice(const double &shipping_price) {
    m_shipping_price = shipping_price;
    m_shipping_price_isSet = true;
}

bool OAIOrderRefundAdd::is_shipping_price_Set() const{
    return m_shipping_price_isSet;
}

bool OAIOrderRefundAdd::is_shipping_price_Valid() const{
    return m_shipping_price_isValid;
}

double OAIOrderRefundAdd::getTotalPrice() const {
    return m_total_price;
}
void OAIOrderRefundAdd::setTotalPrice(const double &total_price) {
    m_total_price = total_price;
    m_total_price_isSet = true;
}

bool OAIOrderRefundAdd::is_total_price_Set() const{
    return m_total_price_isSet;
}

bool OAIOrderRefundAdd::is_total_price_Valid() const{
    return m_total_price_isValid;
}

bool OAIOrderRefundAdd::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fee_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_online_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_restock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_notifications_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_price_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrderRefundAdd::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
