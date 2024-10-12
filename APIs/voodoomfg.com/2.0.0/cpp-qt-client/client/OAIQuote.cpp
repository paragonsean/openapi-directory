/**
 * Voodoo Manufacturing 3D Print API
 * Welcome to the Voodoo Manufacturing API docs!  Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the \"api_key\" header of the request. <a href=\"https://voodoomfg.com/3d-print-api#get-access\" target=\"_blank\">You can request a key here.</a>  This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows:   - Get a list of the available materials with the /materials endpoint   - Upload models to the API with the /models endpoint   - Get quotes for shipping methods with the /order/shipping endpoint   - Get a quote for an order with the /order/create endpoint   - Confirm the order with the /order/confirm endpoint  Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively.  In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you've already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints. 
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@voodoomfg.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuote.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuote::OAIQuote(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuote::OAIQuote() {
    this->initializeModel();
}

OAIQuote::~OAIQuote() {}

void OAIQuote::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;

    m_grand_total_isSet = false;
    m_grand_total_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_shipping_isSet = false;
    m_shipping_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIQuote::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuote::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;

    m_grand_total_isValid = ::OpenAPI::fromJsonValue(m_grand_total, json[QString("grand_total")]);
    m_grand_total_isSet = !json[QString("grand_total")].isNull() && m_grand_total_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_shipping_isValid = ::OpenAPI::fromJsonValue(m_shipping, json[QString("shipping")]);
    m_shipping_isSet = !json[QString("shipping")].isNull() && m_shipping_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIQuote::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuote::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    if (m_grand_total_isSet) {
        obj.insert(QString("grand_total"), ::OpenAPI::toJsonValue(m_grand_total));
    }
    if (m_items_isSet) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_options.isSet()) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_shipping_isSet) {
        obj.insert(QString("shipping"), ::OpenAPI::toJsonValue(m_shipping));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QList<QString> OAIQuote::getErrors() const {
    return m_errors;
}
void OAIQuote::setErrors(const QList<QString> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIQuote::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIQuote::is_errors_Valid() const{
    return m_errors_isValid;
}

double OAIQuote::getGrandTotal() const {
    return m_grand_total;
}
void OAIQuote::setGrandTotal(const double &grand_total) {
    m_grand_total = grand_total;
    m_grand_total_isSet = true;
}

bool OAIQuote::is_grand_total_Set() const{
    return m_grand_total_isSet;
}

bool OAIQuote::is_grand_total_Valid() const{
    return m_grand_total_isValid;
}

double OAIQuote::getItems() const {
    return m_items;
}
void OAIQuote::setItems(const double &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIQuote::is_items_Set() const{
    return m_items_isSet;
}

bool OAIQuote::is_items_Valid() const{
    return m_items_isValid;
}

OAIProductionOptionsCosts OAIQuote::getOptions() const {
    return m_options;
}
void OAIQuote::setOptions(const OAIProductionOptionsCosts &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIQuote::is_options_Set() const{
    return m_options_isSet;
}

bool OAIQuote::is_options_Valid() const{
    return m_options_isValid;
}

double OAIQuote::getShipping() const {
    return m_shipping;
}
void OAIQuote::setShipping(const double &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAIQuote::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAIQuote::is_shipping_Valid() const{
    return m_shipping_isValid;
}

double OAIQuote::getTax() const {
    return m_tax;
}
void OAIQuote::setTax(const double &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIQuote::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIQuote::is_tax_Valid() const{
    return m_tax_isValid;
}

double OAIQuote::getTotal() const {
    return m_total;
}
void OAIQuote::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIQuote::is_total_Set() const{
    return m_total_isSet;
}

bool OAIQuote::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIQuote::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_grand_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuote::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
