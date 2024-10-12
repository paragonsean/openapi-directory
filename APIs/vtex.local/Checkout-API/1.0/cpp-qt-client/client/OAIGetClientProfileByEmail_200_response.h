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

/*
 * OAIGetClientProfileByEmail_200_response.h
 *
 * 
 */

#ifndef OAIGetClientProfileByEmail_200_response_H
#define OAIGetClientProfileByEmail_200_response_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_availableAddresses_inner.h"
#include "OAIGetClientProfileByEmail_200_response_userProfile.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_availableAddresses_inner;
class OAIGetClientProfileByEmail_200_response_userProfile;

class OAIGetClientProfileByEmail_200_response : public OAIObject {
public:
    OAIGetClientProfileByEmail_200_response();
    OAIGetClientProfileByEmail_200_response(QString json);
    ~OAIGetClientProfileByEmail_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAvailableAccounts() const;
    void setAvailableAccounts(const QList<QString> &available_accounts);
    bool is_available_accounts_Set() const;
    bool is_available_accounts_Valid() const;

    QList<OAIAddCoupons_200_response_availableAddresses_inner> getAvailableAddresses() const;
    void setAvailableAddresses(const QList<OAIAddCoupons_200_response_availableAddresses_inner> &available_addresses);
    bool is_available_addresses_Set() const;
    bool is_available_addresses_Valid() const;

    bool isIsComplete() const;
    void setIsComplete(const bool &is_complete);
    bool is_is_complete_Set() const;
    bool is_is_complete_Valid() const;

    QString getProfileProvider() const;
    void setProfileProvider(const QString &profile_provider);
    bool is_profile_provider_Set() const;
    bool is_profile_provider_Valid() const;

    OAIGetClientProfileByEmail_200_response_userProfile getUserProfile() const;
    void setUserProfile(const OAIGetClientProfileByEmail_200_response_userProfile &user_profile);
    bool is_user_profile_Set() const;
    bool is_user_profile_Valid() const;

    QString getUserProfileId() const;
    void setUserProfileId(const QString &user_profile_id);
    bool is_user_profile_id_Set() const;
    bool is_user_profile_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_available_accounts;
    bool m_available_accounts_isSet;
    bool m_available_accounts_isValid;

    QList<OAIAddCoupons_200_response_availableAddresses_inner> m_available_addresses;
    bool m_available_addresses_isSet;
    bool m_available_addresses_isValid;

    bool m_is_complete;
    bool m_is_complete_isSet;
    bool m_is_complete_isValid;

    QString m_profile_provider;
    bool m_profile_provider_isSet;
    bool m_profile_provider_isValid;

    OAIGetClientProfileByEmail_200_response_userProfile m_user_profile;
    bool m_user_profile_isSet;
    bool m_user_profile_isValid;

    QString m_user_profile_id;
    bool m_user_profile_id_isSet;
    bool m_user_profile_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetClientProfileByEmail_200_response)

#endif // OAIGetClientProfileByEmail_200_response_H
