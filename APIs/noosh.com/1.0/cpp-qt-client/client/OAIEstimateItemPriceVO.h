/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEstimateItemPriceVO.h
 *
 * Java type: com.noosh.nooshapi.vo.EstimateItemPriceVO
 */

#ifndef OAIEstimateItemPriceVO_H
#define OAIEstimateItemPriceVO_H

#include <QJsonObject>

#include "OAIBreakoutVO.h"
#include "OAIItemOptionVO.h"
#include <QJsonValue>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBreakoutVO;
class OAIItemOptionVO;

class OAIEstimateItemPriceVO : public OAIObject {
public:
    OAIEstimateItemPriceVO();
    OAIEstimateItemPriceVO(QString json);
    ~OAIEstimateItemPriceVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getAddPrice() const;
    void setAddPrice(const QJsonValue &add_price);
    bool is_add_price_Set() const;
    bool is_add_price_Valid() const;

    QList<OAIBreakoutVO> getBreakouts() const;
    void setBreakouts(const QList<OAIBreakoutVO> &breakouts);
    bool is_breakouts_Set() const;
    bool is_breakouts_Valid() const;

    qint64 getEmEstimateItemPriceId() const;
    void setEmEstimateItemPriceId(const qint64 &em_estimate_item_price_id);
    bool is_em_estimate_item_price_id_Set() const;
    bool is_em_estimate_item_price_id_Valid() const;

    OAIItemOptionVO getItemOption() const;
    void setItemOption(const OAIItemOptionVO &item_option);
    bool is_item_option_Set() const;
    bool is_item_option_Valid() const;

    QJsonValue getPrice() const;
    void setPrice(const QJsonValue &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QJsonValue getShipping() const;
    void setShipping(const QJsonValue &shipping);
    bool is_shipping_Set() const;
    bool is_shipping_Valid() const;

    QJsonValue getTax() const;
    void setTax(const QJsonValue &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    QJsonValue getTotalPrice() const;
    void setTotalPrice(const QJsonValue &total_price);
    bool is_total_price_Set() const;
    bool is_total_price_Valid() const;

    QJsonValue getTransactionalAddPrice() const;
    void setTransactionalAddPrice(const QJsonValue &transactional_add_price);
    bool is_transactional_add_price_Set() const;
    bool is_transactional_add_price_Valid() const;

    QJsonValue getTransactionalPrice() const;
    void setTransactionalPrice(const QJsonValue &transactional_price);
    bool is_transactional_price_Set() const;
    bool is_transactional_price_Valid() const;

    QJsonValue getTransactionalShipping() const;
    void setTransactionalShipping(const QJsonValue &transactional_shipping);
    bool is_transactional_shipping_Set() const;
    bool is_transactional_shipping_Valid() const;

    QJsonValue getTransactionalTax() const;
    void setTransactionalTax(const QJsonValue &transactional_tax);
    bool is_transactional_tax_Set() const;
    bool is_transactional_tax_Valid() const;

    QJsonValue getTransactionalTotalPrice() const;
    void setTransactionalTotalPrice(const QJsonValue &transactional_total_price);
    bool is_transactional_total_price_Set() const;
    bool is_transactional_total_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_add_price;
    bool m_add_price_isSet;
    bool m_add_price_isValid;

    QList<OAIBreakoutVO> m_breakouts;
    bool m_breakouts_isSet;
    bool m_breakouts_isValid;

    qint64 m_em_estimate_item_price_id;
    bool m_em_estimate_item_price_id_isSet;
    bool m_em_estimate_item_price_id_isValid;

    OAIItemOptionVO m_item_option;
    bool m_item_option_isSet;
    bool m_item_option_isValid;

    QJsonValue m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QJsonValue m_shipping;
    bool m_shipping_isSet;
    bool m_shipping_isValid;

    QJsonValue m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    QJsonValue m_total_price;
    bool m_total_price_isSet;
    bool m_total_price_isValid;

    QJsonValue m_transactional_add_price;
    bool m_transactional_add_price_isSet;
    bool m_transactional_add_price_isValid;

    QJsonValue m_transactional_price;
    bool m_transactional_price_isSet;
    bool m_transactional_price_isValid;

    QJsonValue m_transactional_shipping;
    bool m_transactional_shipping_isSet;
    bool m_transactional_shipping_isValid;

    QJsonValue m_transactional_tax;
    bool m_transactional_tax_isSet;
    bool m_transactional_tax_isValid;

    QJsonValue m_transactional_total_price;
    bool m_transactional_total_price_isSet;
    bool m_transactional_total_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEstimateItemPriceVO)

#endif // OAIEstimateItemPriceVO_H
