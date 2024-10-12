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
 * OAIProductPriceAdd.h
 *
 * 
 */

#ifndef OAIProductPriceAdd_H
#define OAIProductPriceAdd_H

#include <QJsonObject>

#include "OAIProductAdd_group_prices_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProductAdd_group_prices_inner;

class OAIProductPriceAdd : public OAIObject {
public:
    OAIProductPriceAdd();
    OAIProductPriceAdd(QString json);
    ~OAIProductPriceAdd() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIProductAdd_group_prices_inner> getGroupPrices() const;
    void setGroupPrices(const QList<OAIProductAdd_group_prices_inner> &group_prices);
    bool is_group_prices_Set() const;
    bool is_group_prices_Valid() const;

    QString getProductId() const;
    void setProductId(const QString &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIProductAdd_group_prices_inner> m_group_prices;
    bool m_group_prices_isSet;
    bool m_group_prices_isValid;

    QString m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductPriceAdd)

#endif // OAIProductPriceAdd_H
