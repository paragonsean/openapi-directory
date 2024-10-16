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
 * OAIShipmentSimpleVO.h
 *
 * Java type: com.noosh.nooshapi.vo.ShipmentSimpleVO
 */

#ifndef OAIShipmentSimpleVO_H
#define OAIShipmentSimpleVO_H

#include <QJsonObject>

#include "OAISpecBaseVO.h"
#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISpecBaseVO;

class OAIShipmentSimpleVO : public OAIObject {
public:
    OAIShipmentSimpleVO();
    OAIShipmentSimpleVO(QString json);
    ~OAIShipmentSimpleVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getLocationsCount() const;
    void setLocationsCount(const qint64 &locations_count);
    bool is_locations_count_Set() const;
    bool is_locations_count_Valid() const;

    qint64 getQtyReceived() const;
    void setQtyReceived(const qint64 &qty_received);
    bool is_qty_received_Set() const;
    bool is_qty_received_Valid() const;

    qint64 getQtyRequested() const;
    void setQtyRequested(const qint64 &qty_requested);
    bool is_qty_requested_Set() const;
    bool is_qty_requested_Valid() const;

    qint64 getQtyShipped() const;
    void setQtyShipped(const qint64 &qty_shipped);
    bool is_qty_shipped_Set() const;
    bool is_qty_shipped_Valid() const;

    QDate getReceivedDate() const;
    void setReceivedDate(const QDate &received_date);
    bool is_received_date_Set() const;
    bool is_received_date_Valid() const;

    qint64 getShipmentId() const;
    void setShipmentId(const qint64 &shipment_id);
    bool is_shipment_id_Set() const;
    bool is_shipment_id_Valid() const;

    QString getShipmentStatus() const;
    void setShipmentStatus(const QString &shipment_status);
    bool is_shipment_status_Set() const;
    bool is_shipment_status_Valid() const;

    QDate getShippedDate() const;
    void setShippedDate(const QDate &shipped_date);
    bool is_shipped_date_Set() const;
    bool is_shipped_date_Valid() const;

    OAISpecBaseVO getSpec() const;
    void setSpec(const OAISpecBaseVO &spec);
    bool is_spec_Set() const;
    bool is_spec_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_locations_count;
    bool m_locations_count_isSet;
    bool m_locations_count_isValid;

    qint64 m_qty_received;
    bool m_qty_received_isSet;
    bool m_qty_received_isValid;

    qint64 m_qty_requested;
    bool m_qty_requested_isSet;
    bool m_qty_requested_isValid;

    qint64 m_qty_shipped;
    bool m_qty_shipped_isSet;
    bool m_qty_shipped_isValid;

    QDate m_received_date;
    bool m_received_date_isSet;
    bool m_received_date_isValid;

    qint64 m_shipment_id;
    bool m_shipment_id_isSet;
    bool m_shipment_id_isValid;

    QString m_shipment_status;
    bool m_shipment_status_isSet;
    bool m_shipment_status_isValid;

    QDate m_shipped_date;
    bool m_shipped_date_isSet;
    bool m_shipped_date_isValid;

    OAISpecBaseVO m_spec;
    bool m_spec_isSet;
    bool m_spec_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShipmentSimpleVO)

#endif // OAIShipmentSimpleVO_H
