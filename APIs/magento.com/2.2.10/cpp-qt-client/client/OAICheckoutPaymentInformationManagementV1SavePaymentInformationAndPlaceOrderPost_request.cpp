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

#include "OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request() {
    this->initializeModel();
}

OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::~OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request() {}

void OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::initializeModel() {

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_payment_method_isSet = false;
    m_payment_method_isValid = false;
}

void OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::fromJsonObject(QJsonObject json) {

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_payment_method_isValid = ::OpenAPI::fromJsonValue(m_payment_method, json[QString("paymentMethod")]);
    m_payment_method_isSet = !json[QString("paymentMethod")].isNull() && m_payment_method_isValid;
}

QString OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_payment_method.isSet()) {
        obj.insert(QString("paymentMethod"), ::OpenAPI::toJsonValue(m_payment_method));
    }
    return obj;
}

OAIQuote_data_address_interface OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::getBillingAddress() const {
    return m_billing_address;
}
void OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::setBillingAddress(const OAIQuote_data_address_interface &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

OAIQuote_data_payment_interface OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::getPaymentMethod() const {
    return m_payment_method;
}
void OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::setPaymentMethod(const OAIQuote_data_payment_interface &payment_method) {
    m_payment_method = payment_method;
    m_payment_method_isSet = true;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::is_payment_method_Set() const{
    return m_payment_method_isSet;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::is_payment_method_Valid() const{
    return m_payment_method_isValid;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_method.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_payment_method_isValid && true;
}

} // namespace OpenAPI
