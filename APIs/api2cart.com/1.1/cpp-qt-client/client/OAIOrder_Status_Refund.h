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
 * OAIOrder_Status_Refund.h
 *
 * 
 */

#ifndef OAIOrder_Status_Refund_H
#define OAIOrder_Status_Refund_H

#include <QJsonObject>

#include "OAIA2CDateTime.h"
#include "OAIObject.h"
#include "OAIOrder_Status_Refund_Item.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrder_Status_Refund_Item;
class OAIA2CDateTime;

class OAIOrder_Status_Refund : public OAIObject {
public:
    OAIOrder_Status_Refund();
    OAIOrder_Status_Refund(QString json);
    ~OAIOrder_Status_Refund() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getComment() const;
    void setComment(const QString &comment);
    bool is_comment_Set() const;
    bool is_comment_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    double getFee() const;
    void setFee(const double &fee);
    bool is_fee_Set() const;
    bool is_fee_Valid() const;

    QList<OAIOrder_Status_Refund_Item> getRefundedItems() const;
    void setRefundedItems(const QList<OAIOrder_Status_Refund_Item> &refunded_items);
    bool is_refunded_items_Set() const;
    bool is_refunded_items_Valid() const;

    double getShipping() const;
    void setShipping(const double &shipping);
    bool is_shipping_Set() const;
    bool is_shipping_Valid() const;

    double getTax() const;
    void setTax(const double &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    OAIA2CDateTime getTime() const;
    void setTime(const OAIA2CDateTime &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    double getTotalRefunded() const;
    void setTotalRefunded(const double &total_refunded);
    bool is_total_refunded_Set() const;
    bool is_total_refunded_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_comment;
    bool m_comment_isSet;
    bool m_comment_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    double m_fee;
    bool m_fee_isSet;
    bool m_fee_isValid;

    QList<OAIOrder_Status_Refund_Item> m_refunded_items;
    bool m_refunded_items_isSet;
    bool m_refunded_items_isValid;

    double m_shipping;
    bool m_shipping_isSet;
    bool m_shipping_isValid;

    double m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    OAIA2CDateTime m_time;
    bool m_time_isSet;
    bool m_time_isValid;

    double m_total_refunded;
    bool m_total_refunded_isSet;
    bool m_total_refunded_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrder_Status_Refund)

#endif // OAIOrder_Status_Refund_H
