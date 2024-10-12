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
 * OAIResponse_Order_List_Result.h
 *
 * 
 */

#ifndef OAIResponse_Order_List_Result_H
#define OAIResponse_Order_List_Result_H

#include <QJsonObject>

#include "OAIObject.h"
#include "OAIOrder.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrder;

class OAIResponse_Order_List_Result : public OAIObject {
public:
    OAIResponse_Order_List_Result();
    OAIResponse_Order_List_Result(QString json);
    ~OAIResponse_Order_List_Result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QList<OAIOrder> getOrder() const;
    void setOrder(const QList<OAIOrder> &order);
    bool is_order_Set() const;
    bool is_order_Valid() const;

    qint32 getOrdersCount() const;
    void setOrdersCount(const qint32 &orders_count);
    bool is_orders_count_Set() const;
    bool is_orders_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QList<OAIOrder> m_order;
    bool m_order_isSet;
    bool m_order_isValid;

    qint32 m_orders_count;
    bool m_orders_count_isSet;
    bool m_orders_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResponse_Order_List_Result)

#endif // OAIResponse_Order_List_Result_H
