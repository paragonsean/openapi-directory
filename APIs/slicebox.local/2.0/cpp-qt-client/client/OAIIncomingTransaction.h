/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIncomingTransaction.h
 *
 * 
 */

#ifndef OAIIncomingTransaction_H
#define OAIIncomingTransaction_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIncomingTransaction : public OAIObject {
public:
    OAIIncomingTransaction();
    OAIIncomingTransaction(QString json);
    ~OAIIncomingTransaction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getBoxId() const;
    void setBoxId(const qint64 &box_id);
    bool is_box_id_Set() const;
    bool is_box_id_Valid() const;

    QString getBoxName() const;
    void setBoxName(const QString &box_name);
    bool is_box_name_Set() const;
    bool is_box_name_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint64 getOutgoingTransactionId() const;
    void setOutgoingTransactionId(const qint64 &outgoing_transaction_id);
    bool is_outgoing_transaction_id_Set() const;
    bool is_outgoing_transaction_id_Valid() const;

    qint64 getReceivedImageCount() const;
    void setReceivedImageCount(const qint64 &received_image_count);
    bool is_received_image_count_Set() const;
    bool is_received_image_count_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint64 getTotalImageCount() const;
    void setTotalImageCount(const qint64 &total_image_count);
    bool is_total_image_count_Set() const;
    bool is_total_image_count_Valid() const;

    qint64 getUpdated() const;
    void setUpdated(const qint64 &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_box_id;
    bool m_box_id_isSet;
    bool m_box_id_isValid;

    QString m_box_name;
    bool m_box_name_isSet;
    bool m_box_name_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint64 m_outgoing_transaction_id;
    bool m_outgoing_transaction_id_isSet;
    bool m_outgoing_transaction_id_isValid;

    qint64 m_received_image_count;
    bool m_received_image_count_isSet;
    bool m_received_image_count_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint64 m_total_image_count;
    bool m_total_image_count_isSet;
    bool m_total_image_count_isValid;

    qint64 m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIncomingTransaction)

#endif // OAIIncomingTransaction_H
