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
 * OAIQuoteItemDetailVO.h
 *
 * Java type: com.noosh.nooshapi.vo.QuoteItemDetailVO
 */

#ifndef OAIQuoteItemDetailVO_H
#define OAIQuoteItemDetailVO_H

#include <QJsonObject>

#include "OAIPropertyPaAndAttVO.h"
#include "OAIQuotePriceDetailVO.h"
#include "OAISpecBaseVO.h"
#include <QDate>
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPropertyPaAndAttVO;
class OAIQuotePriceDetailVO;
class OAISpecBaseVO;

class OAIQuoteItemDetailVO : public OAIObject {
public:
    OAIQuoteItemDetailVO();
    OAIQuoteItemDetailVO(QString json);
    ~OAIQuoteItemDetailVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getChosenQuantity() const;
    void setChosenQuantity(const QJsonValue &chosen_quantity);
    bool is_chosen_quantity_Set() const;
    bool is_chosen_quantity_Valid() const;

    QString getComments() const;
    void setComments(const QString &comments);
    bool is_comments_Set() const;
    bool is_comments_Valid() const;

    QDate getCompletionDate() const;
    void setCompletionDate(const QDate &completion_date);
    bool is_completion_date_Set() const;
    bool is_completion_date_Valid() const;

    QList<OAIPropertyPaAndAttVO> getCustomFields() const;
    void setCustomFields(const QList<OAIPropertyPaAndAttVO> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    qint64 getItemId() const;
    void setItemId(const qint64 &item_id);
    bool is_item_id_Set() const;
    bool is_item_id_Valid() const;

    QList<OAIQuotePriceDetailVO> getItemPrices() const;
    void setItemPrices(const QList<OAIQuotePriceDetailVO> &item_prices);
    bool is_item_prices_Set() const;
    bool is_item_prices_Valid() const;

    QJsonValue getItemShippingTotal() const;
    void setItemShippingTotal(const QJsonValue &item_shipping_total);
    bool is_item_shipping_total_Set() const;
    bool is_item_shipping_total_Valid() const;

    QJsonValue getItemTaxTotal() const;
    void setItemTaxTotal(const QJsonValue &item_tax_total);
    bool is_item_tax_total_Set() const;
    bool is_item_tax_total_Valid() const;

    QJsonValue getItemTotal() const;
    void setItemTotal(const QJsonValue &item_total);
    bool is_item_total_Set() const;
    bool is_item_total_Valid() const;

    QString getReasonForQuoteSelection() const;
    void setReasonForQuoteSelection(const QString &reason_for_quote_selection);
    bool is_reason_for_quote_selection_Set() const;
    bool is_reason_for_quote_selection_Valid() const;

    bool isShowCostPricesAndMarkup() const;
    void setShowCostPricesAndMarkup(const bool &show_cost_prices_and_markup);
    bool is_show_cost_prices_and_markup_Set() const;
    bool is_show_cost_prices_and_markup_Valid() const;

    OAISpecBaseVO getSpec() const;
    void setSpec(const OAISpecBaseVO &spec);
    bool is_spec_Set() const;
    bool is_spec_Valid() const;

    QJsonValue getTransactionalItemShippingTotal() const;
    void setTransactionalItemShippingTotal(const QJsonValue &transactional_item_shipping_total);
    bool is_transactional_item_shipping_total_Set() const;
    bool is_transactional_item_shipping_total_Valid() const;

    QJsonValue getTransactionalItemTaxTotal() const;
    void setTransactionalItemTaxTotal(const QJsonValue &transactional_item_tax_total);
    bool is_transactional_item_tax_total_Set() const;
    bool is_transactional_item_tax_total_Valid() const;

    QJsonValue getTransactionalItemTotal() const;
    void setTransactionalItemTotal(const QJsonValue &transactional_item_total);
    bool is_transactional_item_total_Set() const;
    bool is_transactional_item_total_Valid() const;

    QString getVatCode() const;
    void setVatCode(const QString &vat_code);
    bool is_vat_code_Set() const;
    bool is_vat_code_Valid() const;

    QJsonValue getVatRate() const;
    void setVatRate(const QJsonValue &vat_rate);
    bool is_vat_rate_Set() const;
    bool is_vat_rate_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_chosen_quantity;
    bool m_chosen_quantity_isSet;
    bool m_chosen_quantity_isValid;

    QString m_comments;
    bool m_comments_isSet;
    bool m_comments_isValid;

    QDate m_completion_date;
    bool m_completion_date_isSet;
    bool m_completion_date_isValid;

    QList<OAIPropertyPaAndAttVO> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    qint64 m_item_id;
    bool m_item_id_isSet;
    bool m_item_id_isValid;

    QList<OAIQuotePriceDetailVO> m_item_prices;
    bool m_item_prices_isSet;
    bool m_item_prices_isValid;

    QJsonValue m_item_shipping_total;
    bool m_item_shipping_total_isSet;
    bool m_item_shipping_total_isValid;

    QJsonValue m_item_tax_total;
    bool m_item_tax_total_isSet;
    bool m_item_tax_total_isValid;

    QJsonValue m_item_total;
    bool m_item_total_isSet;
    bool m_item_total_isValid;

    QString m_reason_for_quote_selection;
    bool m_reason_for_quote_selection_isSet;
    bool m_reason_for_quote_selection_isValid;

    bool m_show_cost_prices_and_markup;
    bool m_show_cost_prices_and_markup_isSet;
    bool m_show_cost_prices_and_markup_isValid;

    OAISpecBaseVO m_spec;
    bool m_spec_isSet;
    bool m_spec_isValid;

    QJsonValue m_transactional_item_shipping_total;
    bool m_transactional_item_shipping_total_isSet;
    bool m_transactional_item_shipping_total_isValid;

    QJsonValue m_transactional_item_tax_total;
    bool m_transactional_item_tax_total_isSet;
    bool m_transactional_item_tax_total_isValid;

    QJsonValue m_transactional_item_total;
    bool m_transactional_item_total_isSet;
    bool m_transactional_item_total_isValid;

    QString m_vat_code;
    bool m_vat_code_isSet;
    bool m_vat_code_isValid;

    QJsonValue m_vat_rate;
    bool m_vat_rate_isSet;
    bool m_vat_rate_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuoteItemDetailVO)

#endif // OAIQuoteItemDetailVO_H
