/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBaseFirewallRule.h
 *
 * 
 */

#ifndef OAIBaseFirewallRule_H
#define OAIBaseFirewallRule_H

#include <QJsonObject>

#include "OAIBaseEntity.h"
#include "OAIEntityType.h"
#include "OAIFirewallAction.h"
#include "OAIPortRange.h"
#include "OAIReference.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReference;
class OAIPortRange;

class OAIBaseFirewallRule : public OAIObject {
public:
    OAIBaseFirewallRule();
    OAIBaseFirewallRule(QString json);
    ~OAIBaseFirewallRule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEntityId() const;
    void setEntityId(const QString &entity_id);
    bool is_entity_id_Set() const;
    bool is_entity_id_Valid() const;

    OAIEntityType getEntityType() const;
    void setEntityType(const OAIEntityType &entity_type);
    bool is_entity_type_Set() const;
    bool is_entity_type_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIFirewallAction getAction() const;
    void setAction(const OAIFirewallAction &action);
    bool is_action_Set() const;
    bool is_action_Valid() const;

    bool isDestinationAny() const;
    void setDestinationAny(const bool &destination_any);
    bool is_destination_any_Set() const;
    bool is_destination_any_Valid() const;

    bool isDestinationInversion() const;
    void setDestinationInversion(const bool &destination_inversion);
    bool is_destination_inversion_Set() const;
    bool is_destination_inversion_Valid() const;

    QList<OAIReference> getDestinations() const;
    void setDestinations(const QList<OAIReference> &destinations);
    bool is_destinations_Set() const;
    bool is_destinations_Valid() const;

    bool isDisabled() const;
    void setDisabled(const bool &disabled);
    bool is_disabled_Set() const;
    bool is_disabled_Valid() const;

    QList<OAIPortRange> getPortRanges() const;
    void setPortRanges(const QList<OAIPortRange> &port_ranges);
    bool is_port_ranges_Set() const;
    bool is_port_ranges_Valid() const;

    QString getRuleId() const;
    void setRuleId(const QString &rule_id);
    bool is_rule_id_Set() const;
    bool is_rule_id_Valid() const;

    QString getSectionId() const;
    void setSectionId(const QString &section_id);
    bool is_section_id_Set() const;
    bool is_section_id_Valid() const;

    QString getSectionName() const;
    void setSectionName(const QString &section_name);
    bool is_section_name_Set() const;
    bool is_section_name_Valid() const;

    qint32 getSequenceNumber() const;
    void setSequenceNumber(const qint32 &sequence_number);
    bool is_sequence_number_Set() const;
    bool is_sequence_number_Valid() const;

    bool isServiceAny() const;
    void setServiceAny(const bool &service_any);
    bool is_service_any_Set() const;
    bool is_service_any_Valid() const;

    QList<OAIReference> getServices() const;
    void setServices(const QList<OAIReference> &services);
    bool is_services_Set() const;
    bool is_services_Valid() const;

    bool isSourceAny() const;
    void setSourceAny(const bool &source_any);
    bool is_source_any_Set() const;
    bool is_source_any_Valid() const;

    bool isSourceInversion() const;
    void setSourceInversion(const bool &source_inversion);
    bool is_source_inversion_Set() const;
    bool is_source_inversion_Valid() const;

    QList<OAIReference> getSources() const;
    void setSources(const QList<OAIReference> &sources);
    bool is_sources_Set() const;
    bool is_sources_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_entity_id;
    bool m_entity_id_isSet;
    bool m_entity_id_isValid;

    OAIEntityType m_entity_type;
    bool m_entity_type_isSet;
    bool m_entity_type_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIFirewallAction m_action;
    bool m_action_isSet;
    bool m_action_isValid;

    bool m_destination_any;
    bool m_destination_any_isSet;
    bool m_destination_any_isValid;

    bool m_destination_inversion;
    bool m_destination_inversion_isSet;
    bool m_destination_inversion_isValid;

    QList<OAIReference> m_destinations;
    bool m_destinations_isSet;
    bool m_destinations_isValid;

    bool m_disabled;
    bool m_disabled_isSet;
    bool m_disabled_isValid;

    QList<OAIPortRange> m_port_ranges;
    bool m_port_ranges_isSet;
    bool m_port_ranges_isValid;

    QString m_rule_id;
    bool m_rule_id_isSet;
    bool m_rule_id_isValid;

    QString m_section_id;
    bool m_section_id_isSet;
    bool m_section_id_isValid;

    QString m_section_name;
    bool m_section_name_isSet;
    bool m_section_name_isValid;

    qint32 m_sequence_number;
    bool m_sequence_number_isSet;
    bool m_sequence_number_isValid;

    bool m_service_any;
    bool m_service_any_isSet;
    bool m_service_any_isValid;

    QList<OAIReference> m_services;
    bool m_services_isSet;
    bool m_services_isValid;

    bool m_source_any;
    bool m_source_any_isSet;
    bool m_source_any_isValid;

    bool m_source_inversion;
    bool m_source_inversion_isSet;
    bool m_source_inversion_isValid;

    QList<OAIReference> m_sources;
    bool m_sources_isSet;
    bool m_sources_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBaseFirewallRule)

#endif // OAIBaseFirewallRule_H
