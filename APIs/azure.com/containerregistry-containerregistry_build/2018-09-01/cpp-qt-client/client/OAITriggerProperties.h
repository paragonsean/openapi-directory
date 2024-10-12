/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITriggerProperties.h
 *
 * The properties of a trigger.
 */

#ifndef OAITriggerProperties_H
#define OAITriggerProperties_H

#include <QJsonObject>

#include "OAIBaseImageTrigger.h"
#include "OAISourceTrigger.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBaseImageTrigger;
class OAISourceTrigger;

class OAITriggerProperties : public OAIObject {
public:
    OAITriggerProperties();
    OAITriggerProperties(QString json);
    ~OAITriggerProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBaseImageTrigger getBaseImageTrigger() const;
    void setBaseImageTrigger(const OAIBaseImageTrigger &base_image_trigger);
    bool is_base_image_trigger_Set() const;
    bool is_base_image_trigger_Valid() const;

    QList<OAISourceTrigger> getSourceTriggers() const;
    void setSourceTriggers(const QList<OAISourceTrigger> &source_triggers);
    bool is_source_triggers_Set() const;
    bool is_source_triggers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBaseImageTrigger m_base_image_trigger;
    bool m_base_image_trigger_isSet;
    bool m_base_image_trigger_isValid;

    QList<OAISourceTrigger> m_source_triggers;
    bool m_source_triggers_isSet;
    bool m_source_triggers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITriggerProperties)

#endif // OAITriggerProperties_H
