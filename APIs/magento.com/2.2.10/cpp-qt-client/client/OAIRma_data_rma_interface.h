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
 * OAIRma_data_rma_interface.h
 *
 * Interface RmaInterface
 */

#ifndef OAIRma_data_rma_interface_H
#define OAIRma_data_rma_interface_H

#include <QJsonObject>

#include "OAIFramework_attribute_interface.h"
#include "OAIObject.h"
#include "OAIRma_data_comment_interface.h"
#include "OAIRma_data_item_interface.h"
#include "OAIRma_data_track_interface.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRma_data_comment_interface;
class OAIFramework_attribute_interface;
class OAIRma_data_item_interface;
class OAIRma_data_track_interface;

class OAIRma_data_rma_interface : public OAIObject {
public:
    OAIRma_data_rma_interface();
    OAIRma_data_rma_interface(QString json);
    ~OAIRma_data_rma_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIRma_data_comment_interface> getComments() const;
    void setComments(const QList<OAIRma_data_comment_interface> &comments);
    bool is_comments_Set() const;
    bool is_comments_Valid() const;

    QList<OAIFramework_attribute_interface> getCustomAttributes() const;
    void setCustomAttributes(const QList<OAIFramework_attribute_interface> &custom_attributes);
    bool is_custom_attributes_Set() const;
    bool is_custom_attributes_Valid() const;

    QString getCustomerCustomEmail() const;
    void setCustomerCustomEmail(const QString &customer_custom_email);
    bool is_customer_custom_email_Set() const;
    bool is_customer_custom_email_Valid() const;

    qint32 getCustomerId() const;
    void setCustomerId(const qint32 &customer_id);
    bool is_customer_id_Set() const;
    bool is_customer_id_Valid() const;

    QString getDateRequested() const;
    void setDateRequested(const QString &date_requested);
    bool is_date_requested_Set() const;
    bool is_date_requested_Valid() const;

    qint32 getEntityId() const;
    void setEntityId(const qint32 &entity_id);
    bool is_entity_id_Set() const;
    bool is_entity_id_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getIncrementId() const;
    void setIncrementId(const QString &increment_id);
    bool is_increment_id_Set() const;
    bool is_increment_id_Valid() const;

    QList<OAIRma_data_item_interface> getItems() const;
    void setItems(const QList<OAIRma_data_item_interface> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    qint32 getOrderId() const;
    void setOrderId(const qint32 &order_id);
    bool is_order_id_Set() const;
    bool is_order_id_Valid() const;

    QString getOrderIncrementId() const;
    void setOrderIncrementId(const QString &order_increment_id);
    bool is_order_increment_id_Set() const;
    bool is_order_increment_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint32 getStoreId() const;
    void setStoreId(const qint32 &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    QList<OAIRma_data_track_interface> getTracks() const;
    void setTracks(const QList<OAIRma_data_track_interface> &tracks);
    bool is_tracks_Set() const;
    bool is_tracks_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIRma_data_comment_interface> m_comments;
    bool m_comments_isSet;
    bool m_comments_isValid;

    QList<OAIFramework_attribute_interface> m_custom_attributes;
    bool m_custom_attributes_isSet;
    bool m_custom_attributes_isValid;

    QString m_customer_custom_email;
    bool m_customer_custom_email_isSet;
    bool m_customer_custom_email_isValid;

    qint32 m_customer_id;
    bool m_customer_id_isSet;
    bool m_customer_id_isValid;

    QString m_date_requested;
    bool m_date_requested_isSet;
    bool m_date_requested_isValid;

    qint32 m_entity_id;
    bool m_entity_id_isSet;
    bool m_entity_id_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_increment_id;
    bool m_increment_id_isSet;
    bool m_increment_id_isValid;

    QList<OAIRma_data_item_interface> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    qint32 m_order_id;
    bool m_order_id_isSet;
    bool m_order_id_isValid;

    QString m_order_increment_id;
    bool m_order_increment_id_isSet;
    bool m_order_increment_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint32 m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    QList<OAIRma_data_track_interface> m_tracks;
    bool m_tracks_isSet;
    bool m_tracks_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRma_data_rma_interface)

#endif // OAIRma_data_rma_interface_H
