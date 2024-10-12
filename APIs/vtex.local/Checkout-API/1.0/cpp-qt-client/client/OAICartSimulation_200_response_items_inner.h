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
 * OAICartSimulation_200_response_items_inner.h
 *
 * 
 */

#ifndef OAICartSimulation_200_response_items_inner_H
#define OAICartSimulation_200_response_items_inner_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_items_inner_priceDefinition.h"
#include "OAICartSimulation_200_response_items_inner_priceTags_inner.h"
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_items_inner_priceDefinition;
class OAICartSimulation_200_response_items_inner_priceTags_inner;

class OAICartSimulation_200_response_items_inner : public OAIObject {
public:
    OAICartSimulation_200_response_items_inner();
    OAICartSimulation_200_response_items_inner(QString json);
    ~OAICartSimulation_200_response_items_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAvailability() const;
    void setAvailability(const QString &availability);
    bool is_availability_Set() const;
    bool is_availability_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getListPrice() const;
    void setListPrice(const qint32 &list_price);
    bool is_list_price_Set() const;
    bool is_list_price_Valid() const;

    QString getMeasurementUnit() const;
    void setMeasurementUnit(const QString &measurement_unit);
    bool is_measurement_unit_Set() const;
    bool is_measurement_unit_Valid() const;

    QList<QJsonValue> getOfferings() const;
    void setOfferings(const QList<QJsonValue> &offerings);
    bool is_offerings_Set() const;
    bool is_offerings_Valid() const;

    QString getParentAssemblyBinding() const;
    void setParentAssemblyBinding(const QString &parent_assembly_binding);
    bool is_parent_assembly_binding_Set() const;
    bool is_parent_assembly_binding_Valid() const;

    qint32 getParentItemIndex() const;
    void setParentItemIndex(const qint32 &parent_item_index);
    bool is_parent_item_index_Set() const;
    bool is_parent_item_index_Valid() const;

    qint32 getPrice() const;
    void setPrice(const qint32 &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    OAIAddCoupons_200_response_items_inner_priceDefinition getPriceDefinition() const;
    void setPriceDefinition(const OAIAddCoupons_200_response_items_inner_priceDefinition &price_definition);
    bool is_price_definition_Set() const;
    bool is_price_definition_Valid() const;

    QList<OAICartSimulation_200_response_items_inner_priceTags_inner> getPriceTags() const;
    void setPriceTags(const QList<OAICartSimulation_200_response_items_inner_priceTags_inner> &price_tags);
    bool is_price_tags_Set() const;
    bool is_price_tags_Valid() const;

    QString getPriceValidUntil() const;
    void setPriceValidUntil(const QString &price_valid_until);
    bool is_price_valid_until_Set() const;
    bool is_price_valid_until_Valid() const;

    qint32 getQuantity() const;
    void setQuantity(const qint32 &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    qint32 getRequestIndex() const;
    void setRequestIndex(const qint32 &request_index);
    bool is_request_index_Set() const;
    bool is_request_index_Valid() const;

    qint32 getRewardValue() const;
    void setRewardValue(const qint32 &reward_value);
    bool is_reward_value_Set() const;
    bool is_reward_value_Valid() const;

    QString getSeller() const;
    void setSeller(const QString &seller);
    bool is_seller_Set() const;
    bool is_seller_Valid() const;

    QList<QString> getSellerChain() const;
    void setSellerChain(const QList<QString> &seller_chain);
    bool is_seller_chain_Set() const;
    bool is_seller_chain_Valid() const;

    qint32 getSellingPrice() const;
    void setSellingPrice(const qint32 &selling_price);
    bool is_selling_price_Set() const;
    bool is_selling_price_Valid() const;

    qint32 getTax() const;
    void setTax(const qint32 &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    qint32 getUnitMultiplier() const;
    void setUnitMultiplier(const qint32 &unit_multiplier);
    bool is_unit_multiplier_Set() const;
    bool is_unit_multiplier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_availability;
    bool m_availability_isSet;
    bool m_availability_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_list_price;
    bool m_list_price_isSet;
    bool m_list_price_isValid;

    QString m_measurement_unit;
    bool m_measurement_unit_isSet;
    bool m_measurement_unit_isValid;

    QList<QJsonValue> m_offerings;
    bool m_offerings_isSet;
    bool m_offerings_isValid;

    QString m_parent_assembly_binding;
    bool m_parent_assembly_binding_isSet;
    bool m_parent_assembly_binding_isValid;

    qint32 m_parent_item_index;
    bool m_parent_item_index_isSet;
    bool m_parent_item_index_isValid;

    qint32 m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    OAIAddCoupons_200_response_items_inner_priceDefinition m_price_definition;
    bool m_price_definition_isSet;
    bool m_price_definition_isValid;

    QList<OAICartSimulation_200_response_items_inner_priceTags_inner> m_price_tags;
    bool m_price_tags_isSet;
    bool m_price_tags_isValid;

    QString m_price_valid_until;
    bool m_price_valid_until_isSet;
    bool m_price_valid_until_isValid;

    qint32 m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    qint32 m_request_index;
    bool m_request_index_isSet;
    bool m_request_index_isValid;

    qint32 m_reward_value;
    bool m_reward_value_isSet;
    bool m_reward_value_isValid;

    QString m_seller;
    bool m_seller_isSet;
    bool m_seller_isValid;

    QList<QString> m_seller_chain;
    bool m_seller_chain_isSet;
    bool m_seller_chain_isValid;

    qint32 m_selling_price;
    bool m_selling_price_isSet;
    bool m_selling_price_isValid;

    qint32 m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    qint32 m_unit_multiplier;
    bool m_unit_multiplier_isSet;
    bool m_unit_multiplier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartSimulation_200_response_items_inner)

#endif // OAICartSimulation_200_response_items_inner_H
