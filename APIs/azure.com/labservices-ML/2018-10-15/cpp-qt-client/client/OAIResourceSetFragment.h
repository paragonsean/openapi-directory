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
 * OAIResourceSetFragment.h
 *
 * Represents a VM and the setting Id it was created for.
 */

#ifndef OAIResourceSetFragment_H
#define OAIResourceSetFragment_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIResourceSetFragment : public OAIObject {
public:
    OAIResourceSetFragment();
    OAIResourceSetFragment(QString json);
    ~OAIResourceSetFragment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getResourceSettingId() const;
    void setResourceSettingId(const QString &resource_setting_id);
    bool is_resource_setting_id_Set() const;
    bool is_resource_setting_id_Valid() const;

    QString getVmResourceId() const;
    void setVmResourceId(const QString &vm_resource_id);
    bool is_vm_resource_id_Set() const;
    bool is_vm_resource_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_resource_setting_id;
    bool m_resource_setting_id_isSet;
    bool m_resource_setting_id_isValid;

    QString m_vm_resource_id;
    bool m_vm_resource_id_isSet;
    bool m_vm_resource_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceSetFragment)

#endif // OAIResourceSetFragment_H
