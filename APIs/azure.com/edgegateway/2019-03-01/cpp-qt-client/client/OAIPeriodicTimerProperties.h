/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPeriodicTimerProperties.h
 *
 * Periodic timer trigger properties.
 */

#ifndef OAIPeriodicTimerProperties_H
#define OAIPeriodicTimerProperties_H

#include <QJsonObject>

#include "OAIPeriodicTimerSourceInfo.h"
#include "OAIRoleSinkInfo.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRoleSinkInfo;
class OAIPeriodicTimerSourceInfo;

class OAIPeriodicTimerProperties : public OAIObject {
public:
    OAIPeriodicTimerProperties();
    OAIPeriodicTimerProperties(QString json);
    ~OAIPeriodicTimerProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCustomContextTag() const;
    void setCustomContextTag(const QString &custom_context_tag);
    bool is_custom_context_tag_Set() const;
    bool is_custom_context_tag_Valid() const;

    OAIRoleSinkInfo getSinkInfo() const;
    void setSinkInfo(const OAIRoleSinkInfo &sink_info);
    bool is_sink_info_Set() const;
    bool is_sink_info_Valid() const;

    OAIPeriodicTimerSourceInfo getSourceInfo() const;
    void setSourceInfo(const OAIPeriodicTimerSourceInfo &source_info);
    bool is_source_info_Set() const;
    bool is_source_info_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_custom_context_tag;
    bool m_custom_context_tag_isSet;
    bool m_custom_context_tag_isValid;

    OAIRoleSinkInfo m_sink_info;
    bool m_sink_info_isSet;
    bool m_sink_info_isValid;

    OAIPeriodicTimerSourceInfo m_source_info;
    bool m_source_info_isSet;
    bool m_source_info_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPeriodicTimerProperties)

#endif // OAIPeriodicTimerProperties_H
