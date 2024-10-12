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

#include "OAIGetClientProfileByEmail_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetClientProfileByEmail_200_response::OAIGetClientProfileByEmail_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetClientProfileByEmail_200_response::OAIGetClientProfileByEmail_200_response() {
    this->initializeModel();
}

OAIGetClientProfileByEmail_200_response::~OAIGetClientProfileByEmail_200_response() {}

void OAIGetClientProfileByEmail_200_response::initializeModel() {

    m_available_accounts_isSet = false;
    m_available_accounts_isValid = false;

    m_available_addresses_isSet = false;
    m_available_addresses_isValid = false;

    m_is_complete_isSet = false;
    m_is_complete_isValid = false;

    m_profile_provider_isSet = false;
    m_profile_provider_isValid = false;

    m_user_profile_isSet = false;
    m_user_profile_isValid = false;

    m_user_profile_id_isSet = false;
    m_user_profile_id_isValid = false;
}

void OAIGetClientProfileByEmail_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetClientProfileByEmail_200_response::fromJsonObject(QJsonObject json) {

    m_available_accounts_isValid = ::OpenAPI::fromJsonValue(m_available_accounts, json[QString("availableAccounts")]);
    m_available_accounts_isSet = !json[QString("availableAccounts")].isNull() && m_available_accounts_isValid;

    m_available_addresses_isValid = ::OpenAPI::fromJsonValue(m_available_addresses, json[QString("availableAddresses")]);
    m_available_addresses_isSet = !json[QString("availableAddresses")].isNull() && m_available_addresses_isValid;

    m_is_complete_isValid = ::OpenAPI::fromJsonValue(m_is_complete, json[QString("isComplete")]);
    m_is_complete_isSet = !json[QString("isComplete")].isNull() && m_is_complete_isValid;

    m_profile_provider_isValid = ::OpenAPI::fromJsonValue(m_profile_provider, json[QString("profileProvider")]);
    m_profile_provider_isSet = !json[QString("profileProvider")].isNull() && m_profile_provider_isValid;

    m_user_profile_isValid = ::OpenAPI::fromJsonValue(m_user_profile, json[QString("userProfile")]);
    m_user_profile_isSet = !json[QString("userProfile")].isNull() && m_user_profile_isValid;

    m_user_profile_id_isValid = ::OpenAPI::fromJsonValue(m_user_profile_id, json[QString("userProfileId")]);
    m_user_profile_id_isSet = !json[QString("userProfileId")].isNull() && m_user_profile_id_isValid;
}

QString OAIGetClientProfileByEmail_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetClientProfileByEmail_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_available_accounts.size() > 0) {
        obj.insert(QString("availableAccounts"), ::OpenAPI::toJsonValue(m_available_accounts));
    }
    if (m_available_addresses.size() > 0) {
        obj.insert(QString("availableAddresses"), ::OpenAPI::toJsonValue(m_available_addresses));
    }
    if (m_is_complete_isSet) {
        obj.insert(QString("isComplete"), ::OpenAPI::toJsonValue(m_is_complete));
    }
    if (m_profile_provider_isSet) {
        obj.insert(QString("profileProvider"), ::OpenAPI::toJsonValue(m_profile_provider));
    }
    if (m_user_profile.isSet()) {
        obj.insert(QString("userProfile"), ::OpenAPI::toJsonValue(m_user_profile));
    }
    if (m_user_profile_id_isSet) {
        obj.insert(QString("userProfileId"), ::OpenAPI::toJsonValue(m_user_profile_id));
    }
    return obj;
}

QList<QString> OAIGetClientProfileByEmail_200_response::getAvailableAccounts() const {
    return m_available_accounts;
}
void OAIGetClientProfileByEmail_200_response::setAvailableAccounts(const QList<QString> &available_accounts) {
    m_available_accounts = available_accounts;
    m_available_accounts_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_available_accounts_Set() const{
    return m_available_accounts_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_available_accounts_Valid() const{
    return m_available_accounts_isValid;
}

QList<OAIAddCoupons_200_response_availableAddresses_inner> OAIGetClientProfileByEmail_200_response::getAvailableAddresses() const {
    return m_available_addresses;
}
void OAIGetClientProfileByEmail_200_response::setAvailableAddresses(const QList<OAIAddCoupons_200_response_availableAddresses_inner> &available_addresses) {
    m_available_addresses = available_addresses;
    m_available_addresses_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_available_addresses_Set() const{
    return m_available_addresses_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_available_addresses_Valid() const{
    return m_available_addresses_isValid;
}

bool OAIGetClientProfileByEmail_200_response::isIsComplete() const {
    return m_is_complete;
}
void OAIGetClientProfileByEmail_200_response::setIsComplete(const bool &is_complete) {
    m_is_complete = is_complete;
    m_is_complete_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_is_complete_Set() const{
    return m_is_complete_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_is_complete_Valid() const{
    return m_is_complete_isValid;
}

QString OAIGetClientProfileByEmail_200_response::getProfileProvider() const {
    return m_profile_provider;
}
void OAIGetClientProfileByEmail_200_response::setProfileProvider(const QString &profile_provider) {
    m_profile_provider = profile_provider;
    m_profile_provider_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_profile_provider_Set() const{
    return m_profile_provider_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_profile_provider_Valid() const{
    return m_profile_provider_isValid;
}

OAIGetClientProfileByEmail_200_response_userProfile OAIGetClientProfileByEmail_200_response::getUserProfile() const {
    return m_user_profile;
}
void OAIGetClientProfileByEmail_200_response::setUserProfile(const OAIGetClientProfileByEmail_200_response_userProfile &user_profile) {
    m_user_profile = user_profile;
    m_user_profile_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_user_profile_Set() const{
    return m_user_profile_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_user_profile_Valid() const{
    return m_user_profile_isValid;
}

QString OAIGetClientProfileByEmail_200_response::getUserProfileId() const {
    return m_user_profile_id;
}
void OAIGetClientProfileByEmail_200_response::setUserProfileId(const QString &user_profile_id) {
    m_user_profile_id = user_profile_id;
    m_user_profile_id_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response::is_user_profile_id_Set() const{
    return m_user_profile_id_isSet;
}

bool OAIGetClientProfileByEmail_200_response::is_user_profile_id_Valid() const{
    return m_user_profile_id_isValid;
}

bool OAIGetClientProfileByEmail_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_profile.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_profile_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetClientProfileByEmail_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
