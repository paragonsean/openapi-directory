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

#include "OAISales_data_invoice_extension_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISales_data_invoice_extension_interface::OAISales_data_invoice_extension_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISales_data_invoice_extension_interface::OAISales_data_invoice_extension_interface() {
    this->initializeModel();
}

OAISales_data_invoice_extension_interface::~OAISales_data_invoice_extension_interface() {}

void OAISales_data_invoice_extension_interface::initializeModel() {

    m_base_customer_balance_amount_isSet = false;
    m_base_customer_balance_amount_isValid = false;

    m_base_gift_cards_amount_isSet = false;
    m_base_gift_cards_amount_isValid = false;

    m_customer_balance_amount_isSet = false;
    m_customer_balance_amount_isValid = false;

    m_gift_cards_amount_isSet = false;
    m_gift_cards_amount_isValid = false;

    m_gw_base_price_isSet = false;
    m_gw_base_price_isValid = false;

    m_gw_base_tax_amount_isSet = false;
    m_gw_base_tax_amount_isValid = false;

    m_gw_card_base_price_isSet = false;
    m_gw_card_base_price_isValid = false;

    m_gw_card_base_tax_amount_isSet = false;
    m_gw_card_base_tax_amount_isValid = false;

    m_gw_card_price_isSet = false;
    m_gw_card_price_isValid = false;

    m_gw_card_tax_amount_isSet = false;
    m_gw_card_tax_amount_isValid = false;

    m_gw_items_base_price_isSet = false;
    m_gw_items_base_price_isValid = false;

    m_gw_items_base_tax_amount_isSet = false;
    m_gw_items_base_tax_amount_isValid = false;

    m_gw_items_price_isSet = false;
    m_gw_items_price_isValid = false;

    m_gw_items_tax_amount_isSet = false;
    m_gw_items_tax_amount_isValid = false;

    m_gw_price_isSet = false;
    m_gw_price_isValid = false;

    m_gw_tax_amount_isSet = false;
    m_gw_tax_amount_isValid = false;

    m_vertex_tax_calculation_billing_address_isSet = false;
    m_vertex_tax_calculation_billing_address_isValid = false;

    m_vertex_tax_calculation_order_isSet = false;
    m_vertex_tax_calculation_order_isValid = false;

    m_vertex_tax_calculation_shipping_address_isSet = false;
    m_vertex_tax_calculation_shipping_address_isValid = false;
}

void OAISales_data_invoice_extension_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISales_data_invoice_extension_interface::fromJsonObject(QJsonObject json) {

    m_base_customer_balance_amount_isValid = ::OpenAPI::fromJsonValue(m_base_customer_balance_amount, json[QString("base_customer_balance_amount")]);
    m_base_customer_balance_amount_isSet = !json[QString("base_customer_balance_amount")].isNull() && m_base_customer_balance_amount_isValid;

    m_base_gift_cards_amount_isValid = ::OpenAPI::fromJsonValue(m_base_gift_cards_amount, json[QString("base_gift_cards_amount")]);
    m_base_gift_cards_amount_isSet = !json[QString("base_gift_cards_amount")].isNull() && m_base_gift_cards_amount_isValid;

    m_customer_balance_amount_isValid = ::OpenAPI::fromJsonValue(m_customer_balance_amount, json[QString("customer_balance_amount")]);
    m_customer_balance_amount_isSet = !json[QString("customer_balance_amount")].isNull() && m_customer_balance_amount_isValid;

    m_gift_cards_amount_isValid = ::OpenAPI::fromJsonValue(m_gift_cards_amount, json[QString("gift_cards_amount")]);
    m_gift_cards_amount_isSet = !json[QString("gift_cards_amount")].isNull() && m_gift_cards_amount_isValid;

    m_gw_base_price_isValid = ::OpenAPI::fromJsonValue(m_gw_base_price, json[QString("gw_base_price")]);
    m_gw_base_price_isSet = !json[QString("gw_base_price")].isNull() && m_gw_base_price_isValid;

    m_gw_base_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_base_tax_amount, json[QString("gw_base_tax_amount")]);
    m_gw_base_tax_amount_isSet = !json[QString("gw_base_tax_amount")].isNull() && m_gw_base_tax_amount_isValid;

    m_gw_card_base_price_isValid = ::OpenAPI::fromJsonValue(m_gw_card_base_price, json[QString("gw_card_base_price")]);
    m_gw_card_base_price_isSet = !json[QString("gw_card_base_price")].isNull() && m_gw_card_base_price_isValid;

    m_gw_card_base_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_card_base_tax_amount, json[QString("gw_card_base_tax_amount")]);
    m_gw_card_base_tax_amount_isSet = !json[QString("gw_card_base_tax_amount")].isNull() && m_gw_card_base_tax_amount_isValid;

    m_gw_card_price_isValid = ::OpenAPI::fromJsonValue(m_gw_card_price, json[QString("gw_card_price")]);
    m_gw_card_price_isSet = !json[QString("gw_card_price")].isNull() && m_gw_card_price_isValid;

    m_gw_card_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_card_tax_amount, json[QString("gw_card_tax_amount")]);
    m_gw_card_tax_amount_isSet = !json[QString("gw_card_tax_amount")].isNull() && m_gw_card_tax_amount_isValid;

    m_gw_items_base_price_isValid = ::OpenAPI::fromJsonValue(m_gw_items_base_price, json[QString("gw_items_base_price")]);
    m_gw_items_base_price_isSet = !json[QString("gw_items_base_price")].isNull() && m_gw_items_base_price_isValid;

    m_gw_items_base_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_items_base_tax_amount, json[QString("gw_items_base_tax_amount")]);
    m_gw_items_base_tax_amount_isSet = !json[QString("gw_items_base_tax_amount")].isNull() && m_gw_items_base_tax_amount_isValid;

    m_gw_items_price_isValid = ::OpenAPI::fromJsonValue(m_gw_items_price, json[QString("gw_items_price")]);
    m_gw_items_price_isSet = !json[QString("gw_items_price")].isNull() && m_gw_items_price_isValid;

    m_gw_items_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_items_tax_amount, json[QString("gw_items_tax_amount")]);
    m_gw_items_tax_amount_isSet = !json[QString("gw_items_tax_amount")].isNull() && m_gw_items_tax_amount_isValid;

    m_gw_price_isValid = ::OpenAPI::fromJsonValue(m_gw_price, json[QString("gw_price")]);
    m_gw_price_isSet = !json[QString("gw_price")].isNull() && m_gw_price_isValid;

    m_gw_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_gw_tax_amount, json[QString("gw_tax_amount")]);
    m_gw_tax_amount_isSet = !json[QString("gw_tax_amount")].isNull() && m_gw_tax_amount_isValid;

    m_vertex_tax_calculation_billing_address_isValid = ::OpenAPI::fromJsonValue(m_vertex_tax_calculation_billing_address, json[QString("vertex_tax_calculation_billing_address")]);
    m_vertex_tax_calculation_billing_address_isSet = !json[QString("vertex_tax_calculation_billing_address")].isNull() && m_vertex_tax_calculation_billing_address_isValid;

    m_vertex_tax_calculation_order_isValid = ::OpenAPI::fromJsonValue(m_vertex_tax_calculation_order, json[QString("vertex_tax_calculation_order")]);
    m_vertex_tax_calculation_order_isSet = !json[QString("vertex_tax_calculation_order")].isNull() && m_vertex_tax_calculation_order_isValid;

    m_vertex_tax_calculation_shipping_address_isValid = ::OpenAPI::fromJsonValue(m_vertex_tax_calculation_shipping_address, json[QString("vertex_tax_calculation_shipping_address")]);
    m_vertex_tax_calculation_shipping_address_isSet = !json[QString("vertex_tax_calculation_shipping_address")].isNull() && m_vertex_tax_calculation_shipping_address_isValid;
}

QString OAISales_data_invoice_extension_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISales_data_invoice_extension_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_base_customer_balance_amount_isSet) {
        obj.insert(QString("base_customer_balance_amount"), ::OpenAPI::toJsonValue(m_base_customer_balance_amount));
    }
    if (m_base_gift_cards_amount_isSet) {
        obj.insert(QString("base_gift_cards_amount"), ::OpenAPI::toJsonValue(m_base_gift_cards_amount));
    }
    if (m_customer_balance_amount_isSet) {
        obj.insert(QString("customer_balance_amount"), ::OpenAPI::toJsonValue(m_customer_balance_amount));
    }
    if (m_gift_cards_amount_isSet) {
        obj.insert(QString("gift_cards_amount"), ::OpenAPI::toJsonValue(m_gift_cards_amount));
    }
    if (m_gw_base_price_isSet) {
        obj.insert(QString("gw_base_price"), ::OpenAPI::toJsonValue(m_gw_base_price));
    }
    if (m_gw_base_tax_amount_isSet) {
        obj.insert(QString("gw_base_tax_amount"), ::OpenAPI::toJsonValue(m_gw_base_tax_amount));
    }
    if (m_gw_card_base_price_isSet) {
        obj.insert(QString("gw_card_base_price"), ::OpenAPI::toJsonValue(m_gw_card_base_price));
    }
    if (m_gw_card_base_tax_amount_isSet) {
        obj.insert(QString("gw_card_base_tax_amount"), ::OpenAPI::toJsonValue(m_gw_card_base_tax_amount));
    }
    if (m_gw_card_price_isSet) {
        obj.insert(QString("gw_card_price"), ::OpenAPI::toJsonValue(m_gw_card_price));
    }
    if (m_gw_card_tax_amount_isSet) {
        obj.insert(QString("gw_card_tax_amount"), ::OpenAPI::toJsonValue(m_gw_card_tax_amount));
    }
    if (m_gw_items_base_price_isSet) {
        obj.insert(QString("gw_items_base_price"), ::OpenAPI::toJsonValue(m_gw_items_base_price));
    }
    if (m_gw_items_base_tax_amount_isSet) {
        obj.insert(QString("gw_items_base_tax_amount"), ::OpenAPI::toJsonValue(m_gw_items_base_tax_amount));
    }
    if (m_gw_items_price_isSet) {
        obj.insert(QString("gw_items_price"), ::OpenAPI::toJsonValue(m_gw_items_price));
    }
    if (m_gw_items_tax_amount_isSet) {
        obj.insert(QString("gw_items_tax_amount"), ::OpenAPI::toJsonValue(m_gw_items_tax_amount));
    }
    if (m_gw_price_isSet) {
        obj.insert(QString("gw_price"), ::OpenAPI::toJsonValue(m_gw_price));
    }
    if (m_gw_tax_amount_isSet) {
        obj.insert(QString("gw_tax_amount"), ::OpenAPI::toJsonValue(m_gw_tax_amount));
    }
    if (m_vertex_tax_calculation_billing_address.isSet()) {
        obj.insert(QString("vertex_tax_calculation_billing_address"), ::OpenAPI::toJsonValue(m_vertex_tax_calculation_billing_address));
    }
    if (m_vertex_tax_calculation_order.isSet()) {
        obj.insert(QString("vertex_tax_calculation_order"), ::OpenAPI::toJsonValue(m_vertex_tax_calculation_order));
    }
    if (m_vertex_tax_calculation_shipping_address.isSet()) {
        obj.insert(QString("vertex_tax_calculation_shipping_address"), ::OpenAPI::toJsonValue(m_vertex_tax_calculation_shipping_address));
    }
    return obj;
}

double OAISales_data_invoice_extension_interface::getBaseCustomerBalanceAmount() const {
    return m_base_customer_balance_amount;
}
void OAISales_data_invoice_extension_interface::setBaseCustomerBalanceAmount(const double &base_customer_balance_amount) {
    m_base_customer_balance_amount = base_customer_balance_amount;
    m_base_customer_balance_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_base_customer_balance_amount_Set() const{
    return m_base_customer_balance_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_base_customer_balance_amount_Valid() const{
    return m_base_customer_balance_amount_isValid;
}

double OAISales_data_invoice_extension_interface::getBaseGiftCardsAmount() const {
    return m_base_gift_cards_amount;
}
void OAISales_data_invoice_extension_interface::setBaseGiftCardsAmount(const double &base_gift_cards_amount) {
    m_base_gift_cards_amount = base_gift_cards_amount;
    m_base_gift_cards_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_base_gift_cards_amount_Set() const{
    return m_base_gift_cards_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_base_gift_cards_amount_Valid() const{
    return m_base_gift_cards_amount_isValid;
}

double OAISales_data_invoice_extension_interface::getCustomerBalanceAmount() const {
    return m_customer_balance_amount;
}
void OAISales_data_invoice_extension_interface::setCustomerBalanceAmount(const double &customer_balance_amount) {
    m_customer_balance_amount = customer_balance_amount;
    m_customer_balance_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_customer_balance_amount_Set() const{
    return m_customer_balance_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_customer_balance_amount_Valid() const{
    return m_customer_balance_amount_isValid;
}

double OAISales_data_invoice_extension_interface::getGiftCardsAmount() const {
    return m_gift_cards_amount;
}
void OAISales_data_invoice_extension_interface::setGiftCardsAmount(const double &gift_cards_amount) {
    m_gift_cards_amount = gift_cards_amount;
    m_gift_cards_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gift_cards_amount_Set() const{
    return m_gift_cards_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gift_cards_amount_Valid() const{
    return m_gift_cards_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwBasePrice() const {
    return m_gw_base_price;
}
void OAISales_data_invoice_extension_interface::setGwBasePrice(const QString &gw_base_price) {
    m_gw_base_price = gw_base_price;
    m_gw_base_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_base_price_Set() const{
    return m_gw_base_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_base_price_Valid() const{
    return m_gw_base_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwBaseTaxAmount() const {
    return m_gw_base_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwBaseTaxAmount(const QString &gw_base_tax_amount) {
    m_gw_base_tax_amount = gw_base_tax_amount;
    m_gw_base_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_base_tax_amount_Set() const{
    return m_gw_base_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_base_tax_amount_Valid() const{
    return m_gw_base_tax_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwCardBasePrice() const {
    return m_gw_card_base_price;
}
void OAISales_data_invoice_extension_interface::setGwCardBasePrice(const QString &gw_card_base_price) {
    m_gw_card_base_price = gw_card_base_price;
    m_gw_card_base_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_base_price_Set() const{
    return m_gw_card_base_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_base_price_Valid() const{
    return m_gw_card_base_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwCardBaseTaxAmount() const {
    return m_gw_card_base_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwCardBaseTaxAmount(const QString &gw_card_base_tax_amount) {
    m_gw_card_base_tax_amount = gw_card_base_tax_amount;
    m_gw_card_base_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_base_tax_amount_Set() const{
    return m_gw_card_base_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_base_tax_amount_Valid() const{
    return m_gw_card_base_tax_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwCardPrice() const {
    return m_gw_card_price;
}
void OAISales_data_invoice_extension_interface::setGwCardPrice(const QString &gw_card_price) {
    m_gw_card_price = gw_card_price;
    m_gw_card_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_price_Set() const{
    return m_gw_card_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_price_Valid() const{
    return m_gw_card_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwCardTaxAmount() const {
    return m_gw_card_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwCardTaxAmount(const QString &gw_card_tax_amount) {
    m_gw_card_tax_amount = gw_card_tax_amount;
    m_gw_card_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_tax_amount_Set() const{
    return m_gw_card_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_card_tax_amount_Valid() const{
    return m_gw_card_tax_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwItemsBasePrice() const {
    return m_gw_items_base_price;
}
void OAISales_data_invoice_extension_interface::setGwItemsBasePrice(const QString &gw_items_base_price) {
    m_gw_items_base_price = gw_items_base_price;
    m_gw_items_base_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_base_price_Set() const{
    return m_gw_items_base_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_base_price_Valid() const{
    return m_gw_items_base_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwItemsBaseTaxAmount() const {
    return m_gw_items_base_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwItemsBaseTaxAmount(const QString &gw_items_base_tax_amount) {
    m_gw_items_base_tax_amount = gw_items_base_tax_amount;
    m_gw_items_base_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_base_tax_amount_Set() const{
    return m_gw_items_base_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_base_tax_amount_Valid() const{
    return m_gw_items_base_tax_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwItemsPrice() const {
    return m_gw_items_price;
}
void OAISales_data_invoice_extension_interface::setGwItemsPrice(const QString &gw_items_price) {
    m_gw_items_price = gw_items_price;
    m_gw_items_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_price_Set() const{
    return m_gw_items_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_price_Valid() const{
    return m_gw_items_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwItemsTaxAmount() const {
    return m_gw_items_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwItemsTaxAmount(const QString &gw_items_tax_amount) {
    m_gw_items_tax_amount = gw_items_tax_amount;
    m_gw_items_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_tax_amount_Set() const{
    return m_gw_items_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_items_tax_amount_Valid() const{
    return m_gw_items_tax_amount_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwPrice() const {
    return m_gw_price;
}
void OAISales_data_invoice_extension_interface::setGwPrice(const QString &gw_price) {
    m_gw_price = gw_price;
    m_gw_price_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_price_Set() const{
    return m_gw_price_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_price_Valid() const{
    return m_gw_price_isValid;
}

QString OAISales_data_invoice_extension_interface::getGwTaxAmount() const {
    return m_gw_tax_amount;
}
void OAISales_data_invoice_extension_interface::setGwTaxAmount(const QString &gw_tax_amount) {
    m_gw_tax_amount = gw_tax_amount;
    m_gw_tax_amount_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_gw_tax_amount_Set() const{
    return m_gw_tax_amount_isSet;
}

bool OAISales_data_invoice_extension_interface::is_gw_tax_amount_Valid() const{
    return m_gw_tax_amount_isValid;
}

OAISales_data_order_address_interface OAISales_data_invoice_extension_interface::getVertexTaxCalculationBillingAddress() const {
    return m_vertex_tax_calculation_billing_address;
}
void OAISales_data_invoice_extension_interface::setVertexTaxCalculationBillingAddress(const OAISales_data_order_address_interface &vertex_tax_calculation_billing_address) {
    m_vertex_tax_calculation_billing_address = vertex_tax_calculation_billing_address;
    m_vertex_tax_calculation_billing_address_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_billing_address_Set() const{
    return m_vertex_tax_calculation_billing_address_isSet;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_billing_address_Valid() const{
    return m_vertex_tax_calculation_billing_address_isValid;
}

OAISales_data_order_interface OAISales_data_invoice_extension_interface::getVertexTaxCalculationOrder() const {
    return m_vertex_tax_calculation_order;
}
void OAISales_data_invoice_extension_interface::setVertexTaxCalculationOrder(const OAISales_data_order_interface &vertex_tax_calculation_order) {
    m_vertex_tax_calculation_order = vertex_tax_calculation_order;
    m_vertex_tax_calculation_order_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_order_Set() const{
    return m_vertex_tax_calculation_order_isSet;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_order_Valid() const{
    return m_vertex_tax_calculation_order_isValid;
}

OAISales_data_order_address_interface OAISales_data_invoice_extension_interface::getVertexTaxCalculationShippingAddress() const {
    return m_vertex_tax_calculation_shipping_address;
}
void OAISales_data_invoice_extension_interface::setVertexTaxCalculationShippingAddress(const OAISales_data_order_address_interface &vertex_tax_calculation_shipping_address) {
    m_vertex_tax_calculation_shipping_address = vertex_tax_calculation_shipping_address;
    m_vertex_tax_calculation_shipping_address_isSet = true;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_shipping_address_Set() const{
    return m_vertex_tax_calculation_shipping_address_isSet;
}

bool OAISales_data_invoice_extension_interface::is_vertex_tax_calculation_shipping_address_Valid() const{
    return m_vertex_tax_calculation_shipping_address_isValid;
}

bool OAISales_data_invoice_extension_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_customer_balance_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_gift_cards_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_balance_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_cards_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_base_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_base_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_card_base_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_card_base_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_card_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_card_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_items_base_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_items_base_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_items_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_items_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gw_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vertex_tax_calculation_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vertex_tax_calculation_order.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vertex_tax_calculation_shipping_address.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISales_data_invoice_extension_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
