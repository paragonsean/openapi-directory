/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEnvironmentSize.h
 *
 * Represents a size category supported by this Lab Account (small, medium or large)
 */

#ifndef OAIEnvironmentSize_H
#define OAIEnvironmentSize_H

#include <QJsonObject>

#include "OAISizeInfo.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISizeInfo;

class OAIEnvironmentSize : public OAIObject {
public:
    OAIEnvironmentSize();
    OAIEnvironmentSize(QString json);
    ~OAIEnvironmentSize() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getMaxPrice() const;
    void setMaxPrice(const double &max_price);
    bool is_max_price_Set() const;
    bool is_max_price_Valid() const;

    double getMinMemory() const;
    void setMinMemory(const double &min_memory);
    bool is_min_memory_Set() const;
    bool is_min_memory_Valid() const;

    qint32 getMinNumberOfCores() const;
    void setMinNumberOfCores(const qint32 &min_number_of_cores);
    bool is_min_number_of_cores_Set() const;
    bool is_min_number_of_cores_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAISizeInfo> getVmSizes() const;
    void setVmSizes(const QList<OAISizeInfo> &vm_sizes);
    bool is_vm_sizes_Set() const;
    bool is_vm_sizes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_max_price;
    bool m_max_price_isSet;
    bool m_max_price_isValid;

    double m_min_memory;
    bool m_min_memory_isSet;
    bool m_min_memory_isValid;

    qint32 m_min_number_of_cores;
    bool m_min_number_of_cores_isSet;
    bool m_min_number_of_cores_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAISizeInfo> m_vm_sizes;
    bool m_vm_sizes_isSet;
    bool m_vm_sizes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEnvironmentSize)

#endif // OAIEnvironmentSize_H
