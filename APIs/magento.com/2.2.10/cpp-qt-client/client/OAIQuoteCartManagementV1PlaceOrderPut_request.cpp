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

#include "OAIQuoteCartManagementV1PlaceOrderPut_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuoteCartManagementV1PlaceOrderPut_request::OAIQuoteCartManagementV1PlaceOrderPut_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuoteCartManagementV1PlaceOrderPut_request::OAIQuoteCartManagementV1PlaceOrderPut_request() {
    this->initializeModel();
}

OAIQuoteCartManagementV1PlaceOrderPut_request::~OAIQuoteCartManagementV1PlaceOrderPut_request() {}

void OAIQuoteCartManagementV1PlaceOrderPut_request::initializeModel() {

    m_payment_method_isSet = false;
    m_payment_method_isValid = false;
}

void OAIQuoteCartManagementV1PlaceOrderPut_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuoteCartManagementV1PlaceOrderPut_request::fromJsonObject(QJsonObject json) {

    m_payment_method_isValid = ::OpenAPI::fromJsonValue(m_payment_method, json[QString("paymentMethod")]);
    m_payment_method_isSet = !json[QString("paymentMethod")].isNull() && m_payment_method_isValid;
}

QString OAIQuoteCartManagementV1PlaceOrderPut_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuoteCartManagementV1PlaceOrderPut_request::asJsonObject() const {
    QJsonObject obj;
    if (m_payment_method.isSet()) {
        obj.insert(QString("paymentMethod"), ::OpenAPI::toJsonValue(m_payment_method));
    }
    return obj;
}

OAIQuote_data_payment_interface OAIQuoteCartManagementV1PlaceOrderPut_request::getPaymentMethod() const {
    return m_payment_method;
}
void OAIQuoteCartManagementV1PlaceOrderPut_request::setPaymentMethod(const OAIQuote_data_payment_interface &payment_method) {
    m_payment_method = payment_method;
    m_payment_method_isSet = true;
}

bool OAIQuoteCartManagementV1PlaceOrderPut_request::is_payment_method_Set() const{
    return m_payment_method_isSet;
}

bool OAIQuoteCartManagementV1PlaceOrderPut_request::is_payment_method_Valid() const{
    return m_payment_method_isValid;
}

bool OAIQuoteCartManagementV1PlaceOrderPut_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_payment_method.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuoteCartManagementV1PlaceOrderPut_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
