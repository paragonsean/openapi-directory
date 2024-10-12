/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreditNoteLineItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreditNoteLineItem::OAICreditNoteLineItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreditNoteLineItem::OAICreditNoteLineItem() {
    this->initializeModel();
}

OAICreditNoteLineItem::~OAICreditNoteLineItem() {}

void OAICreditNoteLineItem::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_isSet = false;
    m_discount_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_tax_idfk_isSet = false;
    m_tax_idfk_isValid = false;

    m_transaction_line_item_id_isSet = false;
    m_transaction_line_item_id_isValid = false;

    m_unit_price_isSet = false;
    m_unit_price_isValid = false;
}

void OAICreditNoteLineItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreditNoteLineItem::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("Amount")]);
    m_amount_isSet = !json[QString("Amount")].isNull() && m_amount_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_discount_isValid = ::OpenAPI::fromJsonValue(m_discount, json[QString("Discount")]);
    m_discount_isSet = !json[QString("Discount")].isNull() && m_discount_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("Quantity")]);
    m_quantity_isSet = !json[QString("Quantity")].isNull() && m_quantity_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("TaxAmount")]);
    m_tax_amount_isSet = !json[QString("TaxAmount")].isNull() && m_tax_amount_isValid;

    m_tax_idfk_isValid = ::OpenAPI::fromJsonValue(m_tax_idfk, json[QString("TaxIDFK")]);
    m_tax_idfk_isSet = !json[QString("TaxIDFK")].isNull() && m_tax_idfk_isValid;

    m_transaction_line_item_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_line_item_id, json[QString("TransactionLineItemID")]);
    m_transaction_line_item_id_isSet = !json[QString("TransactionLineItemID")].isNull() && m_transaction_line_item_id_isValid;

    m_unit_price_isValid = ::OpenAPI::fromJsonValue(m_unit_price, json[QString("UnitPrice")]);
    m_unit_price_isSet = !json[QString("UnitPrice")].isNull() && m_unit_price_isValid;
}

QString OAICreditNoteLineItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreditNoteLineItem::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("Amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_isSet) {
        obj.insert(QString("Discount"), ::OpenAPI::toJsonValue(m_discount));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("Quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("TaxAmount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_tax_idfk_isSet) {
        obj.insert(QString("TaxIDFK"), ::OpenAPI::toJsonValue(m_tax_idfk));
    }
    if (m_transaction_line_item_id_isSet) {
        obj.insert(QString("TransactionLineItemID"), ::OpenAPI::toJsonValue(m_transaction_line_item_id));
    }
    if (m_unit_price_isSet) {
        obj.insert(QString("UnitPrice"), ::OpenAPI::toJsonValue(m_unit_price));
    }
    return obj;
}

double OAICreditNoteLineItem::getAmount() const {
    return m_amount;
}
void OAICreditNoteLineItem::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAICreditNoteLineItem::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAICreditNoteLineItem::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAICreditNoteLineItem::getDescription() const {
    return m_description;
}
void OAICreditNoteLineItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICreditNoteLineItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAICreditNoteLineItem::is_description_Valid() const{
    return m_description_isValid;
}

double OAICreditNoteLineItem::getDiscount() const {
    return m_discount;
}
void OAICreditNoteLineItem::setDiscount(const double &discount) {
    m_discount = discount;
    m_discount_isSet = true;
}

bool OAICreditNoteLineItem::is_discount_Set() const{
    return m_discount_isSet;
}

bool OAICreditNoteLineItem::is_discount_Valid() const{
    return m_discount_isValid;
}

double OAICreditNoteLineItem::getQuantity() const {
    return m_quantity;
}
void OAICreditNoteLineItem::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAICreditNoteLineItem::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAICreditNoteLineItem::is_quantity_Valid() const{
    return m_quantity_isValid;
}

double OAICreditNoteLineItem::getTaxAmount() const {
    return m_tax_amount;
}
void OAICreditNoteLineItem::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAICreditNoteLineItem::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAICreditNoteLineItem::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

qint32 OAICreditNoteLineItem::getTaxIdfk() const {
    return m_tax_idfk;
}
void OAICreditNoteLineItem::setTaxIdfk(const qint32 &tax_idfk) {
    m_tax_idfk = tax_idfk;
    m_tax_idfk_isSet = true;
}

bool OAICreditNoteLineItem::is_tax_idfk_Set() const{
    return m_tax_idfk_isSet;
}

bool OAICreditNoteLineItem::is_tax_idfk_Valid() const{
    return m_tax_idfk_isValid;
}

qint64 OAICreditNoteLineItem::getTransactionLineItemId() const {
    return m_transaction_line_item_id;
}
void OAICreditNoteLineItem::setTransactionLineItemId(const qint64 &transaction_line_item_id) {
    m_transaction_line_item_id = transaction_line_item_id;
    m_transaction_line_item_id_isSet = true;
}

bool OAICreditNoteLineItem::is_transaction_line_item_id_Set() const{
    return m_transaction_line_item_id_isSet;
}

bool OAICreditNoteLineItem::is_transaction_line_item_id_Valid() const{
    return m_transaction_line_item_id_isValid;
}

double OAICreditNoteLineItem::getUnitPrice() const {
    return m_unit_price;
}
void OAICreditNoteLineItem::setUnitPrice(const double &unit_price) {
    m_unit_price = unit_price;
    m_unit_price_isSet = true;
}

bool OAICreditNoteLineItem::is_unit_price_Set() const{
    return m_unit_price_isSet;
}

bool OAICreditNoteLineItem::is_unit_price_Valid() const{
    return m_unit_price_isValid;
}

bool OAICreditNoteLineItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_line_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_price_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreditNoteLineItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
