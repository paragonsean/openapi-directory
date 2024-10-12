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
 * OAICartSimulation_200_response_paymentData_paymentSystems_inner.h
 *
 * 
 */

#ifndef OAICartSimulation_200_response_paymentData_paymentSystems_inner_H
#define OAICartSimulation_200_response_paymentData_paymentSystems_inner_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICartSimulation_200_response_paymentData_paymentSystems_inner : public OAIObject {
public:
    OAICartSimulation_200_response_paymentData_paymentSystems_inner();
    OAICartSimulation_200_response_paymentData_paymentSystems_inner(QString json);
    ~OAICartSimulation_200_response_paymentData_paymentSystems_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAvailablePayments() const;
    void setAvailablePayments(const QString &available_payments);
    bool is_available_payments_Set() const;
    bool is_available_payments_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isDisplayDocument() const;
    void setDisplayDocument(const bool &display_document);
    bool is_display_document_Set() const;
    bool is_display_document_Valid() const;

    QString getDueDate() const;
    void setDueDate(const QString &due_date);
    bool is_due_date_Set() const;
    bool is_due_date_Valid() const;

    QString getGroupName() const;
    void setGroupName(const QString &group_name);
    bool is_group_name_Set() const;
    bool is_group_name_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsCustom() const;
    void setIsCustom(const bool &is_custom);
    bool is_is_custom_Set() const;
    bool is_is_custom_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isRequiresAuthentication() const;
    void setRequiresAuthentication(const bool &requires_authentication);
    bool is_requires_authentication_Set() const;
    bool is_requires_authentication_Valid() const;

    bool isRequiresDocument() const;
    void setRequiresDocument(const bool &requires_document);
    bool is_requires_document_Set() const;
    bool is_requires_document_Valid() const;

    QString getStringId() const;
    void setStringId(const QString &string_id);
    bool is_string_id_Set() const;
    bool is_string_id_Valid() const;

    QString getRTemplate() const;
    void setRTemplate(const QString &r_template);
    bool is_r_template_Set() const;
    bool is_r_template_Valid() const;

    OAIObject getValidator() const;
    void setValidator(const OAIObject &validator);
    bool is_validator_Set() const;
    bool is_validator_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_available_payments;
    bool m_available_payments_isSet;
    bool m_available_payments_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_display_document;
    bool m_display_document_isSet;
    bool m_display_document_isValid;

    QString m_due_date;
    bool m_due_date_isSet;
    bool m_due_date_isValid;

    QString m_group_name;
    bool m_group_name_isSet;
    bool m_group_name_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_custom;
    bool m_is_custom_isSet;
    bool m_is_custom_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_requires_authentication;
    bool m_requires_authentication_isSet;
    bool m_requires_authentication_isValid;

    bool m_requires_document;
    bool m_requires_document_isSet;
    bool m_requires_document_isValid;

    QString m_string_id;
    bool m_string_id_isSet;
    bool m_string_id_isValid;

    QString m_r_template;
    bool m_r_template_isSet;
    bool m_r_template_isValid;

    OAIObject m_validator;
    bool m_validator_isSet;
    bool m_validator_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartSimulation_200_response_paymentData_paymentSystems_inner)

#endif // OAICartSimulation_200_response_paymentData_paymentSystems_inner_H
