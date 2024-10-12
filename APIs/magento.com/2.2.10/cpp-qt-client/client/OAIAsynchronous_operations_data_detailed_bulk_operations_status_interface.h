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
 * OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface.h
 *
 * Interface BulkStatusInterface Bulk summary data with list of operations items full data.
 */

#ifndef OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface_H
#define OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface_H

#include <QJsonObject>

#include "OAIAsynchronous_operations_data_detailed_operation_status_interface.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAsynchronous_operations_data_detailed_operation_status_interface;

class OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface : public OAIObject {
public:
    OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface();
    OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface(QString json);
    ~OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBulkId() const;
    void setBulkId(const QString &bulk_id);
    bool is_bulk_id_Set() const;
    bool is_bulk_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getOperationCount() const;
    void setOperationCount(const qint32 &operation_count);
    bool is_operation_count_Set() const;
    bool is_operation_count_Valid() const;

    QList<OAIAsynchronous_operations_data_detailed_operation_status_interface> getOperationsList() const;
    void setOperationsList(const QList<OAIAsynchronous_operations_data_detailed_operation_status_interface> &operations_list);
    bool is_operations_list_Set() const;
    bool is_operations_list_Valid() const;

    QString getStartTime() const;
    void setStartTime(const QString &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    qint32 getUserId() const;
    void setUserId(const qint32 &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_bulk_id;
    bool m_bulk_id_isSet;
    bool m_bulk_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_operation_count;
    bool m_operation_count_isSet;
    bool m_operation_count_isValid;

    QList<OAIAsynchronous_operations_data_detailed_operation_status_interface> m_operations_list;
    bool m_operations_list_isSet;
    bool m_operations_list_isValid;

    QString m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    qint32 m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface)

#endif // OAIAsynchronous_operations_data_detailed_bulk_operations_status_interface_H
