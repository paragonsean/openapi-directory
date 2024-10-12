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

#include "OAIProcessOrder_500_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProcessOrder_500_response::OAIProcessOrder_500_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProcessOrder_500_response::OAIProcessOrder_500_response() {
    this->initializeModel();
}

OAIProcessOrder_500_response::~OAIProcessOrder_500_response() {}

void OAIProcessOrder_500_response::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_operation_id_isSet = false;
    m_operation_id_isValid = false;
}

void OAIProcessOrder_500_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProcessOrder_500_response::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_operation_id_isValid = ::OpenAPI::fromJsonValue(m_operation_id, json[QString("operationId")]);
    m_operation_id_isSet = !json[QString("operationId")].isNull() && m_operation_id_isValid;
}

QString OAIProcessOrder_500_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProcessOrder_500_response::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_operation_id_isSet) {
        obj.insert(QString("operationId"), ::OpenAPI::toJsonValue(m_operation_id));
    }
    return obj;
}

OAIProcessOrder_500_response_error OAIProcessOrder_500_response::getError() const {
    return m_error;
}
void OAIProcessOrder_500_response::setError(const OAIProcessOrder_500_response_error &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIProcessOrder_500_response::is_error_Set() const{
    return m_error_isSet;
}

bool OAIProcessOrder_500_response::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIProcessOrder_500_response::getOperationId() const {
    return m_operation_id;
}
void OAIProcessOrder_500_response::setOperationId(const QString &operation_id) {
    m_operation_id = operation_id;
    m_operation_id_isSet = true;
}

bool OAIProcessOrder_500_response::is_operation_id_Set() const{
    return m_operation_id_isSet;
}

bool OAIProcessOrder_500_response::is_operation_id_Valid() const{
    return m_operation_id_isValid;
}

bool OAIProcessOrder_500_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProcessOrder_500_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
