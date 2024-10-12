/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBillLineItem.h
 *
 * 
 */

#ifndef OAIBillLineItem_H
#define OAIBillLineItem_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBillLineItem : public OAIObject {
public:
    OAIBillLineItem();
    OAIBillLineItem(QString json);
    ~OAIBillLineItem() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAmount() const;
    void setAmount(const double &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    double getDiscount() const;
    void setDiscount(const double &discount);
    bool is_discount_Set() const;
    bool is_discount_Valid() const;

    qint64 getInventoryItemIdfk() const;
    void setInventoryItemIdfk(const qint64 &inventory_item_idfk);
    bool is_inventory_item_idfk_Set() const;
    bool is_inventory_item_idfk_Valid() const;

    QString getInventoryItemName() const;
    void setInventoryItemName(const QString &inventory_item_name);
    bool is_inventory_item_name_Set() const;
    bool is_inventory_item_name_Valid() const;

    QString getInventoryItemSku() const;
    void setInventoryItemSku(const QString &inventory_item_sku);
    bool is_inventory_item_sku_Set() const;
    bool is_inventory_item_sku_Valid() const;

    qint32 getProjectIdfk() const;
    void setProjectIdfk(const qint32 &project_idfk);
    bool is_project_idfk_Set() const;
    bool is_project_idfk_Valid() const;

    QString getProjectTitle() const;
    void setProjectTitle(const QString &project_title);
    bool is_project_title_Set() const;
    bool is_project_title_Valid() const;

    double getQuantity() const;
    void setQuantity(const double &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    double getTaxAmount() const;
    void setTaxAmount(const double &tax_amount);
    bool is_tax_amount_Set() const;
    bool is_tax_amount_Valid() const;

    QString getTaxCode() const;
    void setTaxCode(const QString &tax_code);
    bool is_tax_code_Set() const;
    bool is_tax_code_Valid() const;

    qint32 getTaxIdfk() const;
    void setTaxIdfk(const qint32 &tax_idfk);
    bool is_tax_idfk_Set() const;
    bool is_tax_idfk_Valid() const;

    QString getTaxName() const;
    void setTaxName(const QString &tax_name);
    bool is_tax_name_Set() const;
    bool is_tax_name_Valid() const;

    qint64 getTransactionLineItemId() const;
    void setTransactionLineItemId(const qint64 &transaction_line_item_id);
    bool is_transaction_line_item_id_Set() const;
    bool is_transaction_line_item_id_Valid() const;

    double getUnitPrice() const;
    void setUnitPrice(const double &unit_price);
    bool is_unit_price_Set() const;
    bool is_unit_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    double m_discount;
    bool m_discount_isSet;
    bool m_discount_isValid;

    qint64 m_inventory_item_idfk;
    bool m_inventory_item_idfk_isSet;
    bool m_inventory_item_idfk_isValid;

    QString m_inventory_item_name;
    bool m_inventory_item_name_isSet;
    bool m_inventory_item_name_isValid;

    QString m_inventory_item_sku;
    bool m_inventory_item_sku_isSet;
    bool m_inventory_item_sku_isValid;

    qint32 m_project_idfk;
    bool m_project_idfk_isSet;
    bool m_project_idfk_isValid;

    QString m_project_title;
    bool m_project_title_isSet;
    bool m_project_title_isValid;

    double m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    double m_tax_amount;
    bool m_tax_amount_isSet;
    bool m_tax_amount_isValid;

    QString m_tax_code;
    bool m_tax_code_isSet;
    bool m_tax_code_isValid;

    qint32 m_tax_idfk;
    bool m_tax_idfk_isSet;
    bool m_tax_idfk_isValid;

    QString m_tax_name;
    bool m_tax_name_isSet;
    bool m_tax_name_isValid;

    qint64 m_transaction_line_item_id;
    bool m_transaction_line_item_id_isSet;
    bool m_transaction_line_item_id_isValid;

    double m_unit_price;
    bool m_unit_price_isSet;
    bool m_unit_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBillLineItem)

#endif // OAIBillLineItem_H
