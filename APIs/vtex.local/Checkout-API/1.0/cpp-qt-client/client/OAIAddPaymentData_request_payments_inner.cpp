/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddPaymentData_request_payments_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddPaymentData_request_payments_inner::OAIAddPaymentData_request_payments_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddPaymentData_request_payments_inner::OAIAddPaymentData_request_payments_inner() {
    this->initializeModel();
}

OAIAddPaymentData_request_payments_inner::~OAIAddPaymentData_request_payments_inner() {}

void OAIAddPaymentData_request_payments_inner::initializeModel() {

    m_group_isSet = false;
    m_group_isValid = false;

    m_has_default_billing_address_isSet = false;
    m_has_default_billing_address_isValid = false;

    m_installments_isSet = false;
    m_installments_isValid = false;

    m_installments_interest_rate_isSet = false;
    m_installments_interest_rate_isValid = false;

    m_installments_value_isSet = false;
    m_installments_value_isValid = false;

    m_payment_system_isSet = false;
    m_payment_system_isValid = false;

    m_payment_system_name_isSet = false;
    m_payment_system_name_isValid = false;

    m_reference_value_isSet = false;
    m_reference_value_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAddPaymentData_request_payments_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddPaymentData_request_payments_inner::fromJsonObject(QJsonObject json) {

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_has_default_billing_address_isValid = ::OpenAPI::fromJsonValue(m_has_default_billing_address, json[QString("hasDefaultBillingAddress")]);
    m_has_default_billing_address_isSet = !json[QString("hasDefaultBillingAddress")].isNull() && m_has_default_billing_address_isValid;

    m_installments_isValid = ::OpenAPI::fromJsonValue(m_installments, json[QString("installments")]);
    m_installments_isSet = !json[QString("installments")].isNull() && m_installments_isValid;

    m_installments_interest_rate_isValid = ::OpenAPI::fromJsonValue(m_installments_interest_rate, json[QString("installmentsInterestRate")]);
    m_installments_interest_rate_isSet = !json[QString("installmentsInterestRate")].isNull() && m_installments_interest_rate_isValid;

    m_installments_value_isValid = ::OpenAPI::fromJsonValue(m_installments_value, json[QString("installmentsValue")]);
    m_installments_value_isSet = !json[QString("installmentsValue")].isNull() && m_installments_value_isValid;

    m_payment_system_isValid = ::OpenAPI::fromJsonValue(m_payment_system, json[QString("paymentSystem")]);
    m_payment_system_isSet = !json[QString("paymentSystem")].isNull() && m_payment_system_isValid;

    m_payment_system_name_isValid = ::OpenAPI::fromJsonValue(m_payment_system_name, json[QString("paymentSystemName")]);
    m_payment_system_name_isSet = !json[QString("paymentSystemName")].isNull() && m_payment_system_name_isValid;

    m_reference_value_isValid = ::OpenAPI::fromJsonValue(m_reference_value, json[QString("referenceValue")]);
    m_reference_value_isSet = !json[QString("referenceValue")].isNull() && m_reference_value_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAddPaymentData_request_payments_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddPaymentData_request_payments_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_group_isSet) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_has_default_billing_address_isSet) {
        obj.insert(QString("hasDefaultBillingAddress"), ::OpenAPI::toJsonValue(m_has_default_billing_address));
    }
    if (m_installments_isSet) {
        obj.insert(QString("installments"), ::OpenAPI::toJsonValue(m_installments));
    }
    if (m_installments_interest_rate_isSet) {
        obj.insert(QString("installmentsInterestRate"), ::OpenAPI::toJsonValue(m_installments_interest_rate));
    }
    if (m_installments_value_isSet) {
        obj.insert(QString("installmentsValue"), ::OpenAPI::toJsonValue(m_installments_value));
    }
    if (m_payment_system_isSet) {
        obj.insert(QString("paymentSystem"), ::OpenAPI::toJsonValue(m_payment_system));
    }
    if (m_payment_system_name_isSet) {
        obj.insert(QString("paymentSystemName"), ::OpenAPI::toJsonValue(m_payment_system_name));
    }
    if (m_reference_value_isSet) {
        obj.insert(QString("referenceValue"), ::OpenAPI::toJsonValue(m_reference_value));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAddPaymentData_request_payments_inner::getGroup() const {
    return m_group;
}
void OAIAddPaymentData_request_payments_inner::setGroup(const QString &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_group_Set() const{
    return m_group_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_group_Valid() const{
    return m_group_isValid;
}

bool OAIAddPaymentData_request_payments_inner::isHasDefaultBillingAddress() const {
    return m_has_default_billing_address;
}
void OAIAddPaymentData_request_payments_inner::setHasDefaultBillingAddress(const bool &has_default_billing_address) {
    m_has_default_billing_address = has_default_billing_address;
    m_has_default_billing_address_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_has_default_billing_address_Set() const{
    return m_has_default_billing_address_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_has_default_billing_address_Valid() const{
    return m_has_default_billing_address_isValid;
}

qint32 OAIAddPaymentData_request_payments_inner::getInstallments() const {
    return m_installments;
}
void OAIAddPaymentData_request_payments_inner::setInstallments(const qint32 &installments) {
    m_installments = installments;
    m_installments_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_Set() const{
    return m_installments_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_Valid() const{
    return m_installments_isValid;
}

double OAIAddPaymentData_request_payments_inner::getInstallmentsInterestRate() const {
    return m_installments_interest_rate;
}
void OAIAddPaymentData_request_payments_inner::setInstallmentsInterestRate(const double &installments_interest_rate) {
    m_installments_interest_rate = installments_interest_rate;
    m_installments_interest_rate_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_interest_rate_Set() const{
    return m_installments_interest_rate_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_interest_rate_Valid() const{
    return m_installments_interest_rate_isValid;
}

qint32 OAIAddPaymentData_request_payments_inner::getInstallmentsValue() const {
    return m_installments_value;
}
void OAIAddPaymentData_request_payments_inner::setInstallmentsValue(const qint32 &installments_value) {
    m_installments_value = installments_value;
    m_installments_value_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_value_Set() const{
    return m_installments_value_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_installments_value_Valid() const{
    return m_installments_value_isValid;
}

qint32 OAIAddPaymentData_request_payments_inner::getPaymentSystem() const {
    return m_payment_system;
}
void OAIAddPaymentData_request_payments_inner::setPaymentSystem(const qint32 &payment_system) {
    m_payment_system = payment_system;
    m_payment_system_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_payment_system_Set() const{
    return m_payment_system_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_payment_system_Valid() const{
    return m_payment_system_isValid;
}

QString OAIAddPaymentData_request_payments_inner::getPaymentSystemName() const {
    return m_payment_system_name;
}
void OAIAddPaymentData_request_payments_inner::setPaymentSystemName(const QString &payment_system_name) {
    m_payment_system_name = payment_system_name;
    m_payment_system_name_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_payment_system_name_Set() const{
    return m_payment_system_name_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_payment_system_name_Valid() const{
    return m_payment_system_name_isValid;
}

qint32 OAIAddPaymentData_request_payments_inner::getReferenceValue() const {
    return m_reference_value;
}
void OAIAddPaymentData_request_payments_inner::setReferenceValue(const qint32 &reference_value) {
    m_reference_value = reference_value;
    m_reference_value_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_reference_value_Set() const{
    return m_reference_value_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_reference_value_Valid() const{
    return m_reference_value_isValid;
}

qint32 OAIAddPaymentData_request_payments_inner::getValue() const {
    return m_value;
}
void OAIAddPaymentData_request_payments_inner::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAddPaymentData_request_payments_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAddPaymentData_request_payments_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAddPaymentData_request_payments_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_default_billing_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_interest_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_system_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_system_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddPaymentData_request_payments_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
