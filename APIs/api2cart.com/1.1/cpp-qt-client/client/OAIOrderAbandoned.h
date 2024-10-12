/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOrderAbandoned.h
 *
 * 
 */

#ifndef OAIOrderAbandoned_H
#define OAIOrderAbandoned_H

#include <QJsonObject>

#include "OAIA2CDateTime.h"
#include "OAIBaseCustomer.h"
#include "OAICurrency.h"
#include "OAIObject.h"
#include "OAIOrder_Item.h"
#include "OAIOrder_Totals.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIA2CDateTime;
class OAICurrency;
class OAIBaseCustomer;
class OAIOrder_Item;
class OAIOrder_Totals;

class OAIOrderAbandoned : public OAIObject {
public:
    OAIOrderAbandoned();
    OAIOrderAbandoned(QString json);
    ~OAIOrderAbandoned() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getBasketId() const;
    void setBasketId(const QString &basket_id);
    bool is_basket_id_Set() const;
    bool is_basket_id_Valid() const;

    QString getBasketUrl() const;
    void setBasketUrl(const QString &basket_url);
    bool is_basket_url_Set() const;
    bool is_basket_url_Valid() const;

    OAIA2CDateTime getCreatedAt() const;
    void setCreatedAt(const OAIA2CDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAICurrency getCurrency() const;
    void setCurrency(const OAICurrency &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    OAIBaseCustomer getCustomer() const;
    void setCustomer(const OAIBaseCustomer &customer);
    bool is_customer_Set() const;
    bool is_customer_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIA2CDateTime getModifiedAt() const;
    void setModifiedAt(const OAIA2CDateTime &modified_at);
    bool is_modified_at_Set() const;
    bool is_modified_at_Valid() const;

    QList<OAIOrder_Item> getOrderProducts() const;
    void setOrderProducts(const QList<OAIOrder_Item> &order_products);
    bool is_order_products_Set() const;
    bool is_order_products_Valid() const;

    OAIOrder_Totals getTotals() const;
    void setTotals(const OAIOrder_Totals &totals);
    bool is_totals_Set() const;
    bool is_totals_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_basket_id;
    bool m_basket_id_isSet;
    bool m_basket_id_isValid;

    QString m_basket_url;
    bool m_basket_url_isSet;
    bool m_basket_url_isValid;

    OAIA2CDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAICurrency m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    OAIBaseCustomer m_customer;
    bool m_customer_isSet;
    bool m_customer_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIA2CDateTime m_modified_at;
    bool m_modified_at_isSet;
    bool m_modified_at_isValid;

    QList<OAIOrder_Item> m_order_products;
    bool m_order_products_isSet;
    bool m_order_products_isValid;

    OAIOrder_Totals m_totals;
    bool m_totals_isSet;
    bool m_totals_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrderAbandoned)

#endif // OAIOrderAbandoned_H
