/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIA2pUpgradeLeaseDto.h
 *
 * ~
 */

#ifndef OAIA2pUpgradeLeaseDto_H
#define OAIA2pUpgradeLeaseDto_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIA2pUpgradeLeaseDto : public OAIObject {
public:
    OAIA2pUpgradeLeaseDto();
    OAIA2pUpgradeLeaseDto(QString json);
    ~OAIA2pUpgradeLeaseDto() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getBlocked() const;
    void setBlocked(const QDateTime &blocked);
    bool is_blocked_Set() const;
    bool is_blocked_Valid() const;

    bool isCanceled() const;
    void setCanceled(const bool &canceled);
    bool is_canceled_Set() const;
    bool is_canceled_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint64 getInvoiceId() const;
    void setInvoiceId(const qint64 &invoice_id);
    bool is_invoice_id_Set() const;
    bool is_invoice_id_Valid() const;

    QDateTime getNextBilling() const;
    void setNextBilling(const QDateTime &next_billing);
    bool is_next_billing_Set() const;
    bool is_next_billing_Valid() const;

    bool isPackaged() const;
    void setPackaged(const bool &packaged);
    bool is_packaged_Set() const;
    bool is_packaged_Valid() const;

    qint64 getPrepaidDiscountId() const;
    void setPrepaidDiscountId(const qint64 &prepaid_discount_id);
    bool is_prepaid_discount_id_Set() const;
    bool is_prepaid_discount_id_Valid() const;

    double getPrice() const;
    void setPrice(const double &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_blocked;
    bool m_blocked_isSet;
    bool m_blocked_isValid;

    bool m_canceled;
    bool m_canceled_isSet;
    bool m_canceled_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint64 m_invoice_id;
    bool m_invoice_id_isSet;
    bool m_invoice_id_isValid;

    QDateTime m_next_billing;
    bool m_next_billing_isSet;
    bool m_next_billing_isValid;

    bool m_packaged;
    bool m_packaged_isSet;
    bool m_packaged_isValid;

    qint64 m_prepaid_discount_id;
    bool m_prepaid_discount_id_isSet;
    bool m_prepaid_discount_id_isValid;

    double m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIA2pUpgradeLeaseDto)

#endif // OAIA2pUpgradeLeaseDto_H
