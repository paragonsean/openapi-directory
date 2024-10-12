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
 * OAIUpdateorderFormconfigurationRequest.h
 *
 * 
 */

#ifndef OAIUpdateorderFormconfigurationRequest_H
#define OAIUpdateorderFormconfigurationRequest_H

#include <QJsonObject>

#include "OAIPaymentConfiguration.h"
#include "OAIUpdateorderFormconfigurationRequest_apps_inner.h"
#include "OAIUpdateorderFormconfigurationRequest_taxConfiguration.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateorderFormconfigurationRequest_apps_inner;
class OAIPaymentConfiguration;
class OAIUpdateorderFormconfigurationRequest_taxConfiguration;

class OAIUpdateorderFormconfigurationRequest : public OAIObject {
public:
    OAIUpdateorderFormconfigurationRequest();
    OAIUpdateorderFormconfigurationRequest(QString json);
    ~OAIUpdateorderFormconfigurationRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowManualPrice() const;
    void setAllowManualPrice(const bool &allow_manual_price);
    bool is_allow_manual_price_Set() const;
    bool is_allow_manual_price_Valid() const;

    bool isAllowMultipleDeliveries() const;
    void setAllowMultipleDeliveries(const bool &allow_multiple_deliveries);
    bool is_allow_multiple_deliveries_Set() const;
    bool is_allow_multiple_deliveries_Valid() const;

    QList<OAIUpdateorderFormconfigurationRequest_apps_inner> getApps() const;
    void setApps(const QList<OAIUpdateorderFormconfigurationRequest_apps_inner> &apps);
    bool is_apps_Set() const;
    bool is_apps_Valid() const;

    qint32 getDecimalDigitsPrecision() const;
    void setDecimalDigitsPrecision(const qint32 &decimal_digits_precision);
    bool is_decimal_digits_precision_Set() const;
    bool is_decimal_digits_precision_Valid() const;

    bool isMaskFirstPurchaseData() const;
    void setMaskFirstPurchaseData(const bool &mask_first_purchase_data);
    bool is_mask_first_purchase_data_Set() const;
    bool is_mask_first_purchase_data_Valid() const;

    qint32 getMaxNumberOfWhiteLabelSellers() const;
    void setMaxNumberOfWhiteLabelSellers(const qint32 &max_number_of_white_label_sellers);
    bool is_max_number_of_white_label_sellers_Set() const;
    bool is_max_number_of_white_label_sellers_Valid() const;

    qint32 getMinimumQuantityAccumulatedForItems() const;
    void setMinimumQuantityAccumulatedForItems(const qint32 &minimum_quantity_accumulated_for_items);
    bool is_minimum_quantity_accumulated_for_items_Set() const;
    bool is_minimum_quantity_accumulated_for_items_Valid() const;

    qint32 getMinimumValueAccumulated() const;
    void setMinimumValueAccumulated(const qint32 &minimum_value_accumulated);
    bool is_minimum_value_accumulated_Set() const;
    bool is_minimum_value_accumulated_Valid() const;

    OAIPaymentConfiguration getPaymentConfiguration() const;
    void setPaymentConfiguration(const OAIPaymentConfiguration &payment_configuration);
    bool is_payment_configuration_Set() const;
    bool is_payment_configuration_Valid() const;

    QString getPaymentSystemToCheckFirstInstallment() const;
    void setPaymentSystemToCheckFirstInstallment(const QString &payment_system_to_check_first_installment);
    bool is_payment_system_to_check_first_installment_Set() const;
    bool is_payment_system_to_check_first_installment_Valid() const;

    QString getRecaptchaValidation() const;
    void setRecaptchaValidation(const QString &recaptcha_validation);
    bool is_recaptcha_validation_Set() const;
    bool is_recaptcha_validation_Valid() const;

    OAIUpdateorderFormconfigurationRequest_taxConfiguration getTaxConfiguration() const;
    void setTaxConfiguration(const OAIUpdateorderFormconfigurationRequest_taxConfiguration &tax_configuration);
    bool is_tax_configuration_Set() const;
    bool is_tax_configuration_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_manual_price;
    bool m_allow_manual_price_isSet;
    bool m_allow_manual_price_isValid;

    bool m_allow_multiple_deliveries;
    bool m_allow_multiple_deliveries_isSet;
    bool m_allow_multiple_deliveries_isValid;

    QList<OAIUpdateorderFormconfigurationRequest_apps_inner> m_apps;
    bool m_apps_isSet;
    bool m_apps_isValid;

    qint32 m_decimal_digits_precision;
    bool m_decimal_digits_precision_isSet;
    bool m_decimal_digits_precision_isValid;

    bool m_mask_first_purchase_data;
    bool m_mask_first_purchase_data_isSet;
    bool m_mask_first_purchase_data_isValid;

    qint32 m_max_number_of_white_label_sellers;
    bool m_max_number_of_white_label_sellers_isSet;
    bool m_max_number_of_white_label_sellers_isValid;

    qint32 m_minimum_quantity_accumulated_for_items;
    bool m_minimum_quantity_accumulated_for_items_isSet;
    bool m_minimum_quantity_accumulated_for_items_isValid;

    qint32 m_minimum_value_accumulated;
    bool m_minimum_value_accumulated_isSet;
    bool m_minimum_value_accumulated_isValid;

    OAIPaymentConfiguration m_payment_configuration;
    bool m_payment_configuration_isSet;
    bool m_payment_configuration_isValid;

    QString m_payment_system_to_check_first_installment;
    bool m_payment_system_to_check_first_installment_isSet;
    bool m_payment_system_to_check_first_installment_isValid;

    QString m_recaptcha_validation;
    bool m_recaptcha_validation_isSet;
    bool m_recaptcha_validation_isValid;

    OAIUpdateorderFormconfigurationRequest_taxConfiguration m_tax_configuration;
    bool m_tax_configuration_isSet;
    bool m_tax_configuration_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateorderFormconfigurationRequest)

#endif // OAIUpdateorderFormconfigurationRequest_H
