/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFixedScaleSettings.h
 *
 * 
 */

#ifndef OAIFixedScaleSettings_H
#define OAIFixedScaleSettings_H

#include <QJsonObject>

#include "OAIComputeNodeDeallocationOption.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFixedScaleSettings : public OAIObject {
public:
    OAIFixedScaleSettings();
    OAIFixedScaleSettings(QString json);
    ~OAIFixedScaleSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIComputeNodeDeallocationOption getNodeDeallocationOption() const;
    void setNodeDeallocationOption(const OAIComputeNodeDeallocationOption &node_deallocation_option);
    bool is_node_deallocation_option_Set() const;
    bool is_node_deallocation_option_Valid() const;

    QString getResizeTimeout() const;
    void setResizeTimeout(const QString &resize_timeout);
    bool is_resize_timeout_Set() const;
    bool is_resize_timeout_Valid() const;

    qint32 getTargetDedicatedNodes() const;
    void setTargetDedicatedNodes(const qint32 &target_dedicated_nodes);
    bool is_target_dedicated_nodes_Set() const;
    bool is_target_dedicated_nodes_Valid() const;

    qint32 getTargetLowPriorityNodes() const;
    void setTargetLowPriorityNodes(const qint32 &target_low_priority_nodes);
    bool is_target_low_priority_nodes_Set() const;
    bool is_target_low_priority_nodes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIComputeNodeDeallocationOption m_node_deallocation_option;
    bool m_node_deallocation_option_isSet;
    bool m_node_deallocation_option_isValid;

    QString m_resize_timeout;
    bool m_resize_timeout_isSet;
    bool m_resize_timeout_isValid;

    qint32 m_target_dedicated_nodes;
    bool m_target_dedicated_nodes_isSet;
    bool m_target_dedicated_nodes_isValid;

    qint32 m_target_low_priority_nodes;
    bool m_target_low_priority_nodes_isSet;
    bool m_target_low_priority_nodes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFixedScaleSettings)

#endif // OAIFixedScaleSettings_H
