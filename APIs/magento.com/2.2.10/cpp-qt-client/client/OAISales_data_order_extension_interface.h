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

/*
 * OAISales_data_order_extension_interface.h
 *
 * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\OrderInterface
 */

#ifndef OAISales_data_order_extension_interface_H
#define OAISales_data_order_extension_interface_H

#include <QJsonObject>

#include "OAICompany_data_company_order_interface.h"
#include "OAIGift_card_account_data_gift_card_interface.h"
#include "OAIGift_message_data_message_interface.h"
#include "OAIPayment_data_payment_additional_info_interface.h"
#include "OAISales_data_shipping_assignment_interface.h"
#include "OAITax_data_order_tax_details_applied_tax_interface.h"
#include "OAITax_data_order_tax_details_item_interface.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITax_data_order_tax_details_applied_tax_interface;
class OAICompany_data_company_order_interface;
class OAIGift_card_account_data_gift_card_interface;
class OAIGift_message_data_message_interface;
class OAITax_data_order_tax_details_item_interface;
class OAIPayment_data_payment_additional_info_interface;
class OAISales_data_shipping_assignment_interface;

class OAISales_data_order_extension_interface : public OAIObject {
public:
    OAISales_data_order_extension_interface();
    OAISales_data_order_extension_interface(QString json);
    ~OAISales_data_order_extension_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAmazonOrderReferenceId() const;
    void setAmazonOrderReferenceId(const QString &amazon_order_reference_id);
    bool is_amazon_order_reference_id_Set() const;
    bool is_amazon_order_reference_id_Valid() const;

    QList<OAITax_data_order_tax_details_applied_tax_interface> getAppliedTaxes() const;
    void setAppliedTaxes(const QList<OAITax_data_order_tax_details_applied_tax_interface> &applied_taxes);
    bool is_applied_taxes_Set() const;
    bool is_applied_taxes_Valid() const;

    double getBaseCustomerBalanceAmount() const;
    void setBaseCustomerBalanceAmount(const double &base_customer_balance_amount);
    bool is_base_customer_balance_amount_Set() const;
    bool is_base_customer_balance_amount_Valid() const;

    double getBaseCustomerBalanceInvoiced() const;
    void setBaseCustomerBalanceInvoiced(const double &base_customer_balance_invoiced);
    bool is_base_customer_balance_invoiced_Set() const;
    bool is_base_customer_balance_invoiced_Valid() const;

    double getBaseCustomerBalanceRefunded() const;
    void setBaseCustomerBalanceRefunded(const double &base_customer_balance_refunded);
    bool is_base_customer_balance_refunded_Set() const;
    bool is_base_customer_balance_refunded_Valid() const;

    double getBaseCustomerBalanceTotalRefunded() const;
    void setBaseCustomerBalanceTotalRefunded(const double &base_customer_balance_total_refunded);
    bool is_base_customer_balance_total_refunded_Set() const;
    bool is_base_customer_balance_total_refunded_Valid() const;

    double getBaseGiftCardsAmount() const;
    void setBaseGiftCardsAmount(const double &base_gift_cards_amount);
    bool is_base_gift_cards_amount_Set() const;
    bool is_base_gift_cards_amount_Valid() const;

    double getBaseGiftCardsInvoiced() const;
    void setBaseGiftCardsInvoiced(const double &base_gift_cards_invoiced);
    bool is_base_gift_cards_invoiced_Set() const;
    bool is_base_gift_cards_invoiced_Valid() const;

    double getBaseGiftCardsRefunded() const;
    void setBaseGiftCardsRefunded(const double &base_gift_cards_refunded);
    bool is_base_gift_cards_refunded_Set() const;
    bool is_base_gift_cards_refunded_Valid() const;

    double getBaseRewardCurrencyAmount() const;
    void setBaseRewardCurrencyAmount(const double &base_reward_currency_amount);
    bool is_base_reward_currency_amount_Set() const;
    bool is_base_reward_currency_amount_Valid() const;

    OAICompany_data_company_order_interface getCompanyOrderAttributes() const;
    void setCompanyOrderAttributes(const OAICompany_data_company_order_interface &company_order_attributes);
    bool is_company_order_attributes_Set() const;
    bool is_company_order_attributes_Valid() const;

    bool isConvertingFromQuote() const;
    void setConvertingFromQuote(const bool &converting_from_quote);
    bool is_converting_from_quote_Set() const;
    bool is_converting_from_quote_Valid() const;

    double getCustomerBalanceAmount() const;
    void setCustomerBalanceAmount(const double &customer_balance_amount);
    bool is_customer_balance_amount_Set() const;
    bool is_customer_balance_amount_Valid() const;

    double getCustomerBalanceInvoiced() const;
    void setCustomerBalanceInvoiced(const double &customer_balance_invoiced);
    bool is_customer_balance_invoiced_Set() const;
    bool is_customer_balance_invoiced_Valid() const;

    double getCustomerBalanceRefunded() const;
    void setCustomerBalanceRefunded(const double &customer_balance_refunded);
    bool is_customer_balance_refunded_Set() const;
    bool is_customer_balance_refunded_Valid() const;

    double getCustomerBalanceTotalRefunded() const;
    void setCustomerBalanceTotalRefunded(const double &customer_balance_total_refunded);
    bool is_customer_balance_total_refunded_Set() const;
    bool is_customer_balance_total_refunded_Valid() const;

    QList<OAIGift_card_account_data_gift_card_interface> getGiftCards() const;
    void setGiftCards(const QList<OAIGift_card_account_data_gift_card_interface> &gift_cards);
    bool is_gift_cards_Set() const;
    bool is_gift_cards_Valid() const;

    double getGiftCardsAmount() const;
    void setGiftCardsAmount(const double &gift_cards_amount);
    bool is_gift_cards_amount_Set() const;
    bool is_gift_cards_amount_Valid() const;

    double getGiftCardsInvoiced() const;
    void setGiftCardsInvoiced(const double &gift_cards_invoiced);
    bool is_gift_cards_invoiced_Set() const;
    bool is_gift_cards_invoiced_Valid() const;

    double getGiftCardsRefunded() const;
    void setGiftCardsRefunded(const double &gift_cards_refunded);
    bool is_gift_cards_refunded_Set() const;
    bool is_gift_cards_refunded_Valid() const;

    OAIGift_message_data_message_interface getGiftMessage() const;
    void setGiftMessage(const OAIGift_message_data_message_interface &gift_message);
    bool is_gift_message_Set() const;
    bool is_gift_message_Valid() const;

    QString getGwAddCard() const;
    void setGwAddCard(const QString &gw_add_card);
    bool is_gw_add_card_Set() const;
    bool is_gw_add_card_Valid() const;

    QString getGwAllowGiftReceipt() const;
    void setGwAllowGiftReceipt(const QString &gw_allow_gift_receipt);
    bool is_gw_allow_gift_receipt_Set() const;
    bool is_gw_allow_gift_receipt_Valid() const;

    QString getGwBasePrice() const;
    void setGwBasePrice(const QString &gw_base_price);
    bool is_gw_base_price_Set() const;
    bool is_gw_base_price_Valid() const;

    QString getGwBasePriceInclTax() const;
    void setGwBasePriceInclTax(const QString &gw_base_price_incl_tax);
    bool is_gw_base_price_incl_tax_Set() const;
    bool is_gw_base_price_incl_tax_Valid() const;

    QString getGwBasePriceInvoiced() const;
    void setGwBasePriceInvoiced(const QString &gw_base_price_invoiced);
    bool is_gw_base_price_invoiced_Set() const;
    bool is_gw_base_price_invoiced_Valid() const;

    QString getGwBasePriceRefunded() const;
    void setGwBasePriceRefunded(const QString &gw_base_price_refunded);
    bool is_gw_base_price_refunded_Set() const;
    bool is_gw_base_price_refunded_Valid() const;

    QString getGwBaseTaxAmount() const;
    void setGwBaseTaxAmount(const QString &gw_base_tax_amount);
    bool is_gw_base_tax_amount_Set() const;
    bool is_gw_base_tax_amount_Valid() const;

    QString getGwBaseTaxAmountInvoiced() const;
    void setGwBaseTaxAmountInvoiced(const QString &gw_base_tax_amount_invoiced);
    bool is_gw_base_tax_amount_invoiced_Set() const;
    bool is_gw_base_tax_amount_invoiced_Valid() const;

    QString getGwBaseTaxAmountRefunded() const;
    void setGwBaseTaxAmountRefunded(const QString &gw_base_tax_amount_refunded);
    bool is_gw_base_tax_amount_refunded_Set() const;
    bool is_gw_base_tax_amount_refunded_Valid() const;

    QString getGwCardBasePrice() const;
    void setGwCardBasePrice(const QString &gw_card_base_price);
    bool is_gw_card_base_price_Set() const;
    bool is_gw_card_base_price_Valid() const;

    QString getGwCardBasePriceInclTax() const;
    void setGwCardBasePriceInclTax(const QString &gw_card_base_price_incl_tax);
    bool is_gw_card_base_price_incl_tax_Set() const;
    bool is_gw_card_base_price_incl_tax_Valid() const;

    QString getGwCardBasePriceInvoiced() const;
    void setGwCardBasePriceInvoiced(const QString &gw_card_base_price_invoiced);
    bool is_gw_card_base_price_invoiced_Set() const;
    bool is_gw_card_base_price_invoiced_Valid() const;

    QString getGwCardBasePriceRefunded() const;
    void setGwCardBasePriceRefunded(const QString &gw_card_base_price_refunded);
    bool is_gw_card_base_price_refunded_Set() const;
    bool is_gw_card_base_price_refunded_Valid() const;

    QString getGwCardBaseTaxAmount() const;
    void setGwCardBaseTaxAmount(const QString &gw_card_base_tax_amount);
    bool is_gw_card_base_tax_amount_Set() const;
    bool is_gw_card_base_tax_amount_Valid() const;

    QString getGwCardBaseTaxInvoiced() const;
    void setGwCardBaseTaxInvoiced(const QString &gw_card_base_tax_invoiced);
    bool is_gw_card_base_tax_invoiced_Set() const;
    bool is_gw_card_base_tax_invoiced_Valid() const;

    QString getGwCardBaseTaxRefunded() const;
    void setGwCardBaseTaxRefunded(const QString &gw_card_base_tax_refunded);
    bool is_gw_card_base_tax_refunded_Set() const;
    bool is_gw_card_base_tax_refunded_Valid() const;

    QString getGwCardPrice() const;
    void setGwCardPrice(const QString &gw_card_price);
    bool is_gw_card_price_Set() const;
    bool is_gw_card_price_Valid() const;

    QString getGwCardPriceInclTax() const;
    void setGwCardPriceInclTax(const QString &gw_card_price_incl_tax);
    bool is_gw_card_price_incl_tax_Set() const;
    bool is_gw_card_price_incl_tax_Valid() const;

    QString getGwCardPriceInvoiced() const;
    void setGwCardPriceInvoiced(const QString &gw_card_price_invoiced);
    bool is_gw_card_price_invoiced_Set() const;
    bool is_gw_card_price_invoiced_Valid() const;

    QString getGwCardPriceRefunded() const;
    void setGwCardPriceRefunded(const QString &gw_card_price_refunded);
    bool is_gw_card_price_refunded_Set() const;
    bool is_gw_card_price_refunded_Valid() const;

    QString getGwCardTaxAmount() const;
    void setGwCardTaxAmount(const QString &gw_card_tax_amount);
    bool is_gw_card_tax_amount_Set() const;
    bool is_gw_card_tax_amount_Valid() const;

    QString getGwCardTaxInvoiced() const;
    void setGwCardTaxInvoiced(const QString &gw_card_tax_invoiced);
    bool is_gw_card_tax_invoiced_Set() const;
    bool is_gw_card_tax_invoiced_Valid() const;

    QString getGwCardTaxRefunded() const;
    void setGwCardTaxRefunded(const QString &gw_card_tax_refunded);
    bool is_gw_card_tax_refunded_Set() const;
    bool is_gw_card_tax_refunded_Valid() const;

    QString getGwId() const;
    void setGwId(const QString &gw_id);
    bool is_gw_id_Set() const;
    bool is_gw_id_Valid() const;

    QString getGwItemsBasePrice() const;
    void setGwItemsBasePrice(const QString &gw_items_base_price);
    bool is_gw_items_base_price_Set() const;
    bool is_gw_items_base_price_Valid() const;

    QString getGwItemsBasePriceInclTax() const;
    void setGwItemsBasePriceInclTax(const QString &gw_items_base_price_incl_tax);
    bool is_gw_items_base_price_incl_tax_Set() const;
    bool is_gw_items_base_price_incl_tax_Valid() const;

    QString getGwItemsBasePriceInvoiced() const;
    void setGwItemsBasePriceInvoiced(const QString &gw_items_base_price_invoiced);
    bool is_gw_items_base_price_invoiced_Set() const;
    bool is_gw_items_base_price_invoiced_Valid() const;

    QString getGwItemsBasePriceRefunded() const;
    void setGwItemsBasePriceRefunded(const QString &gw_items_base_price_refunded);
    bool is_gw_items_base_price_refunded_Set() const;
    bool is_gw_items_base_price_refunded_Valid() const;

    QString getGwItemsBaseTaxAmount() const;
    void setGwItemsBaseTaxAmount(const QString &gw_items_base_tax_amount);
    bool is_gw_items_base_tax_amount_Set() const;
    bool is_gw_items_base_tax_amount_Valid() const;

    QString getGwItemsBaseTaxInvoiced() const;
    void setGwItemsBaseTaxInvoiced(const QString &gw_items_base_tax_invoiced);
    bool is_gw_items_base_tax_invoiced_Set() const;
    bool is_gw_items_base_tax_invoiced_Valid() const;

    QString getGwItemsBaseTaxRefunded() const;
    void setGwItemsBaseTaxRefunded(const QString &gw_items_base_tax_refunded);
    bool is_gw_items_base_tax_refunded_Set() const;
    bool is_gw_items_base_tax_refunded_Valid() const;

    QString getGwItemsPrice() const;
    void setGwItemsPrice(const QString &gw_items_price);
    bool is_gw_items_price_Set() const;
    bool is_gw_items_price_Valid() const;

    QString getGwItemsPriceInclTax() const;
    void setGwItemsPriceInclTax(const QString &gw_items_price_incl_tax);
    bool is_gw_items_price_incl_tax_Set() const;
    bool is_gw_items_price_incl_tax_Valid() const;

    QString getGwItemsPriceInvoiced() const;
    void setGwItemsPriceInvoiced(const QString &gw_items_price_invoiced);
    bool is_gw_items_price_invoiced_Set() const;
    bool is_gw_items_price_invoiced_Valid() const;

    QString getGwItemsPriceRefunded() const;
    void setGwItemsPriceRefunded(const QString &gw_items_price_refunded);
    bool is_gw_items_price_refunded_Set() const;
    bool is_gw_items_price_refunded_Valid() const;

    QString getGwItemsTaxAmount() const;
    void setGwItemsTaxAmount(const QString &gw_items_tax_amount);
    bool is_gw_items_tax_amount_Set() const;
    bool is_gw_items_tax_amount_Valid() const;

    QString getGwItemsTaxInvoiced() const;
    void setGwItemsTaxInvoiced(const QString &gw_items_tax_invoiced);
    bool is_gw_items_tax_invoiced_Set() const;
    bool is_gw_items_tax_invoiced_Valid() const;

    QString getGwItemsTaxRefunded() const;
    void setGwItemsTaxRefunded(const QString &gw_items_tax_refunded);
    bool is_gw_items_tax_refunded_Set() const;
    bool is_gw_items_tax_refunded_Valid() const;

    QString getGwPrice() const;
    void setGwPrice(const QString &gw_price);
    bool is_gw_price_Set() const;
    bool is_gw_price_Valid() const;

    QString getGwPriceInclTax() const;
    void setGwPriceInclTax(const QString &gw_price_incl_tax);
    bool is_gw_price_incl_tax_Set() const;
    bool is_gw_price_incl_tax_Valid() const;

    QString getGwPriceInvoiced() const;
    void setGwPriceInvoiced(const QString &gw_price_invoiced);
    bool is_gw_price_invoiced_Set() const;
    bool is_gw_price_invoiced_Valid() const;

    QString getGwPriceRefunded() const;
    void setGwPriceRefunded(const QString &gw_price_refunded);
    bool is_gw_price_refunded_Set() const;
    bool is_gw_price_refunded_Valid() const;

    QString getGwTaxAmount() const;
    void setGwTaxAmount(const QString &gw_tax_amount);
    bool is_gw_tax_amount_Set() const;
    bool is_gw_tax_amount_Valid() const;

    QString getGwTaxAmountInvoiced() const;
    void setGwTaxAmountInvoiced(const QString &gw_tax_amount_invoiced);
    bool is_gw_tax_amount_invoiced_Set() const;
    bool is_gw_tax_amount_invoiced_Valid() const;

    QString getGwTaxAmountRefunded() const;
    void setGwTaxAmountRefunded(const QString &gw_tax_amount_refunded);
    bool is_gw_tax_amount_refunded_Set() const;
    bool is_gw_tax_amount_refunded_Valid() const;

    QList<OAITax_data_order_tax_details_item_interface> getItemAppliedTaxes() const;
    void setItemAppliedTaxes(const QList<OAITax_data_order_tax_details_item_interface> &item_applied_taxes);
    bool is_item_applied_taxes_Set() const;
    bool is_item_applied_taxes_Valid() const;

    QList<OAIPayment_data_payment_additional_info_interface> getPaymentAdditionalInfo() const;
    void setPaymentAdditionalInfo(const QList<OAIPayment_data_payment_additional_info_interface> &payment_additional_info);
    bool is_payment_additional_info_Set() const;
    bool is_payment_additional_info_Valid() const;

    double getRewardCurrencyAmount() const;
    void setRewardCurrencyAmount(const double &reward_currency_amount);
    bool is_reward_currency_amount_Set() const;
    bool is_reward_currency_amount_Valid() const;

    qint32 getRewardPointsBalance() const;
    void setRewardPointsBalance(const qint32 &reward_points_balance);
    bool is_reward_points_balance_Set() const;
    bool is_reward_points_balance_Valid() const;

    QList<OAISales_data_shipping_assignment_interface> getShippingAssignments() const;
    void setShippingAssignments(const QList<OAISales_data_shipping_assignment_interface> &shipping_assignments);
    bool is_shipping_assignments_Set() const;
    bool is_shipping_assignments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_amazon_order_reference_id;
    bool m_amazon_order_reference_id_isSet;
    bool m_amazon_order_reference_id_isValid;

    QList<OAITax_data_order_tax_details_applied_tax_interface> m_applied_taxes;
    bool m_applied_taxes_isSet;
    bool m_applied_taxes_isValid;

    double m_base_customer_balance_amount;
    bool m_base_customer_balance_amount_isSet;
    bool m_base_customer_balance_amount_isValid;

    double m_base_customer_balance_invoiced;
    bool m_base_customer_balance_invoiced_isSet;
    bool m_base_customer_balance_invoiced_isValid;

    double m_base_customer_balance_refunded;
    bool m_base_customer_balance_refunded_isSet;
    bool m_base_customer_balance_refunded_isValid;

    double m_base_customer_balance_total_refunded;
    bool m_base_customer_balance_total_refunded_isSet;
    bool m_base_customer_balance_total_refunded_isValid;

    double m_base_gift_cards_amount;
    bool m_base_gift_cards_amount_isSet;
    bool m_base_gift_cards_amount_isValid;

    double m_base_gift_cards_invoiced;
    bool m_base_gift_cards_invoiced_isSet;
    bool m_base_gift_cards_invoiced_isValid;

    double m_base_gift_cards_refunded;
    bool m_base_gift_cards_refunded_isSet;
    bool m_base_gift_cards_refunded_isValid;

    double m_base_reward_currency_amount;
    bool m_base_reward_currency_amount_isSet;
    bool m_base_reward_currency_amount_isValid;

    OAICompany_data_company_order_interface m_company_order_attributes;
    bool m_company_order_attributes_isSet;
    bool m_company_order_attributes_isValid;

    bool m_converting_from_quote;
    bool m_converting_from_quote_isSet;
    bool m_converting_from_quote_isValid;

    double m_customer_balance_amount;
    bool m_customer_balance_amount_isSet;
    bool m_customer_balance_amount_isValid;

    double m_customer_balance_invoiced;
    bool m_customer_balance_invoiced_isSet;
    bool m_customer_balance_invoiced_isValid;

    double m_customer_balance_refunded;
    bool m_customer_balance_refunded_isSet;
    bool m_customer_balance_refunded_isValid;

    double m_customer_balance_total_refunded;
    bool m_customer_balance_total_refunded_isSet;
    bool m_customer_balance_total_refunded_isValid;

    QList<OAIGift_card_account_data_gift_card_interface> m_gift_cards;
    bool m_gift_cards_isSet;
    bool m_gift_cards_isValid;

    double m_gift_cards_amount;
    bool m_gift_cards_amount_isSet;
    bool m_gift_cards_amount_isValid;

    double m_gift_cards_invoiced;
    bool m_gift_cards_invoiced_isSet;
    bool m_gift_cards_invoiced_isValid;

    double m_gift_cards_refunded;
    bool m_gift_cards_refunded_isSet;
    bool m_gift_cards_refunded_isValid;

    OAIGift_message_data_message_interface m_gift_message;
    bool m_gift_message_isSet;
    bool m_gift_message_isValid;

    QString m_gw_add_card;
    bool m_gw_add_card_isSet;
    bool m_gw_add_card_isValid;

    QString m_gw_allow_gift_receipt;
    bool m_gw_allow_gift_receipt_isSet;
    bool m_gw_allow_gift_receipt_isValid;

    QString m_gw_base_price;
    bool m_gw_base_price_isSet;
    bool m_gw_base_price_isValid;

    QString m_gw_base_price_incl_tax;
    bool m_gw_base_price_incl_tax_isSet;
    bool m_gw_base_price_incl_tax_isValid;

    QString m_gw_base_price_invoiced;
    bool m_gw_base_price_invoiced_isSet;
    bool m_gw_base_price_invoiced_isValid;

    QString m_gw_base_price_refunded;
    bool m_gw_base_price_refunded_isSet;
    bool m_gw_base_price_refunded_isValid;

    QString m_gw_base_tax_amount;
    bool m_gw_base_tax_amount_isSet;
    bool m_gw_base_tax_amount_isValid;

    QString m_gw_base_tax_amount_invoiced;
    bool m_gw_base_tax_amount_invoiced_isSet;
    bool m_gw_base_tax_amount_invoiced_isValid;

    QString m_gw_base_tax_amount_refunded;
    bool m_gw_base_tax_amount_refunded_isSet;
    bool m_gw_base_tax_amount_refunded_isValid;

    QString m_gw_card_base_price;
    bool m_gw_card_base_price_isSet;
    bool m_gw_card_base_price_isValid;

    QString m_gw_card_base_price_incl_tax;
    bool m_gw_card_base_price_incl_tax_isSet;
    bool m_gw_card_base_price_incl_tax_isValid;

    QString m_gw_card_base_price_invoiced;
    bool m_gw_card_base_price_invoiced_isSet;
    bool m_gw_card_base_price_invoiced_isValid;

    QString m_gw_card_base_price_refunded;
    bool m_gw_card_base_price_refunded_isSet;
    bool m_gw_card_base_price_refunded_isValid;

    QString m_gw_card_base_tax_amount;
    bool m_gw_card_base_tax_amount_isSet;
    bool m_gw_card_base_tax_amount_isValid;

    QString m_gw_card_base_tax_invoiced;
    bool m_gw_card_base_tax_invoiced_isSet;
    bool m_gw_card_base_tax_invoiced_isValid;

    QString m_gw_card_base_tax_refunded;
    bool m_gw_card_base_tax_refunded_isSet;
    bool m_gw_card_base_tax_refunded_isValid;

    QString m_gw_card_price;
    bool m_gw_card_price_isSet;
    bool m_gw_card_price_isValid;

    QString m_gw_card_price_incl_tax;
    bool m_gw_card_price_incl_tax_isSet;
    bool m_gw_card_price_incl_tax_isValid;

    QString m_gw_card_price_invoiced;
    bool m_gw_card_price_invoiced_isSet;
    bool m_gw_card_price_invoiced_isValid;

    QString m_gw_card_price_refunded;
    bool m_gw_card_price_refunded_isSet;
    bool m_gw_card_price_refunded_isValid;

    QString m_gw_card_tax_amount;
    bool m_gw_card_tax_amount_isSet;
    bool m_gw_card_tax_amount_isValid;

    QString m_gw_card_tax_invoiced;
    bool m_gw_card_tax_invoiced_isSet;
    bool m_gw_card_tax_invoiced_isValid;

    QString m_gw_card_tax_refunded;
    bool m_gw_card_tax_refunded_isSet;
    bool m_gw_card_tax_refunded_isValid;

    QString m_gw_id;
    bool m_gw_id_isSet;
    bool m_gw_id_isValid;

    QString m_gw_items_base_price;
    bool m_gw_items_base_price_isSet;
    bool m_gw_items_base_price_isValid;

    QString m_gw_items_base_price_incl_tax;
    bool m_gw_items_base_price_incl_tax_isSet;
    bool m_gw_items_base_price_incl_tax_isValid;

    QString m_gw_items_base_price_invoiced;
    bool m_gw_items_base_price_invoiced_isSet;
    bool m_gw_items_base_price_invoiced_isValid;

    QString m_gw_items_base_price_refunded;
    bool m_gw_items_base_price_refunded_isSet;
    bool m_gw_items_base_price_refunded_isValid;

    QString m_gw_items_base_tax_amount;
    bool m_gw_items_base_tax_amount_isSet;
    bool m_gw_items_base_tax_amount_isValid;

    QString m_gw_items_base_tax_invoiced;
    bool m_gw_items_base_tax_invoiced_isSet;
    bool m_gw_items_base_tax_invoiced_isValid;

    QString m_gw_items_base_tax_refunded;
    bool m_gw_items_base_tax_refunded_isSet;
    bool m_gw_items_base_tax_refunded_isValid;

    QString m_gw_items_price;
    bool m_gw_items_price_isSet;
    bool m_gw_items_price_isValid;

    QString m_gw_items_price_incl_tax;
    bool m_gw_items_price_incl_tax_isSet;
    bool m_gw_items_price_incl_tax_isValid;

    QString m_gw_items_price_invoiced;
    bool m_gw_items_price_invoiced_isSet;
    bool m_gw_items_price_invoiced_isValid;

    QString m_gw_items_price_refunded;
    bool m_gw_items_price_refunded_isSet;
    bool m_gw_items_price_refunded_isValid;

    QString m_gw_items_tax_amount;
    bool m_gw_items_tax_amount_isSet;
    bool m_gw_items_tax_amount_isValid;

    QString m_gw_items_tax_invoiced;
    bool m_gw_items_tax_invoiced_isSet;
    bool m_gw_items_tax_invoiced_isValid;

    QString m_gw_items_tax_refunded;
    bool m_gw_items_tax_refunded_isSet;
    bool m_gw_items_tax_refunded_isValid;

    QString m_gw_price;
    bool m_gw_price_isSet;
    bool m_gw_price_isValid;

    QString m_gw_price_incl_tax;
    bool m_gw_price_incl_tax_isSet;
    bool m_gw_price_incl_tax_isValid;

    QString m_gw_price_invoiced;
    bool m_gw_price_invoiced_isSet;
    bool m_gw_price_invoiced_isValid;

    QString m_gw_price_refunded;
    bool m_gw_price_refunded_isSet;
    bool m_gw_price_refunded_isValid;

    QString m_gw_tax_amount;
    bool m_gw_tax_amount_isSet;
    bool m_gw_tax_amount_isValid;

    QString m_gw_tax_amount_invoiced;
    bool m_gw_tax_amount_invoiced_isSet;
    bool m_gw_tax_amount_invoiced_isValid;

    QString m_gw_tax_amount_refunded;
    bool m_gw_tax_amount_refunded_isSet;
    bool m_gw_tax_amount_refunded_isValid;

    QList<OAITax_data_order_tax_details_item_interface> m_item_applied_taxes;
    bool m_item_applied_taxes_isSet;
    bool m_item_applied_taxes_isValid;

    QList<OAIPayment_data_payment_additional_info_interface> m_payment_additional_info;
    bool m_payment_additional_info_isSet;
    bool m_payment_additional_info_isValid;

    double m_reward_currency_amount;
    bool m_reward_currency_amount_isSet;
    bool m_reward_currency_amount_isValid;

    qint32 m_reward_points_balance;
    bool m_reward_points_balance_isSet;
    bool m_reward_points_balance_isValid;

    QList<OAISales_data_shipping_assignment_interface> m_shipping_assignments;
    bool m_shipping_assignments_isSet;
    bool m_shipping_assignments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_data_order_extension_interface)

#endif // OAISales_data_order_extension_interface_H
