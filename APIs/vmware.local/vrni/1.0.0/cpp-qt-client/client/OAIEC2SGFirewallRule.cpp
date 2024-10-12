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

#include "OAIEC2SGFirewallRule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEC2SGFirewallRule::OAIEC2SGFirewallRule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEC2SGFirewallRule::OAIEC2SGFirewallRule() {
    this->initializeModel();
}

OAIEC2SGFirewallRule::~OAIEC2SGFirewallRule() {}

void OAIEC2SGFirewallRule::initializeModel() {

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_entity_type_isSet = false;
    m_entity_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_action_isSet = false;
    m_action_isValid = false;

    m_destination_any_isSet = false;
    m_destination_any_isValid = false;

    m_destination_inversion_isSet = false;
    m_destination_inversion_isValid = false;

    m_destinations_isSet = false;
    m_destinations_isValid = false;

    m_disabled_isSet = false;
    m_disabled_isValid = false;

    m_port_ranges_isSet = false;
    m_port_ranges_isValid = false;

    m_rule_id_isSet = false;
    m_rule_id_isValid = false;

    m_section_id_isSet = false;
    m_section_id_isValid = false;

    m_section_name_isSet = false;
    m_section_name_isValid = false;

    m_sequence_number_isSet = false;
    m_sequence_number_isValid = false;

    m_service_any_isSet = false;
    m_service_any_isValid = false;

    m_services_isSet = false;
    m_services_isValid = false;

    m_source_any_isSet = false;
    m_source_any_isValid = false;

    m_source_inversion_isSet = false;
    m_source_inversion_isValid = false;

    m_sources_isSet = false;
    m_sources_isValid = false;

    m_direction_isSet = false;
    m_direction_isValid = false;

    m_owner_security_group_isSet = false;
    m_owner_security_group_isValid = false;

    m_vpc_isSet = false;
    m_vpc_isValid = false;
}

void OAIEC2SGFirewallRule::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEC2SGFirewallRule::fromJsonObject(QJsonObject json) {

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_entity_type_isValid = ::OpenAPI::fromJsonValue(m_entity_type, json[QString("entity_type")]);
    m_entity_type_isSet = !json[QString("entity_type")].isNull() && m_entity_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_destination_any_isValid = ::OpenAPI::fromJsonValue(m_destination_any, json[QString("destination_any")]);
    m_destination_any_isSet = !json[QString("destination_any")].isNull() && m_destination_any_isValid;

    m_destination_inversion_isValid = ::OpenAPI::fromJsonValue(m_destination_inversion, json[QString("destination_inversion")]);
    m_destination_inversion_isSet = !json[QString("destination_inversion")].isNull() && m_destination_inversion_isValid;

    m_destinations_isValid = ::OpenAPI::fromJsonValue(m_destinations, json[QString("destinations")]);
    m_destinations_isSet = !json[QString("destinations")].isNull() && m_destinations_isValid;

    m_disabled_isValid = ::OpenAPI::fromJsonValue(m_disabled, json[QString("disabled")]);
    m_disabled_isSet = !json[QString("disabled")].isNull() && m_disabled_isValid;

    m_port_ranges_isValid = ::OpenAPI::fromJsonValue(m_port_ranges, json[QString("port_ranges")]);
    m_port_ranges_isSet = !json[QString("port_ranges")].isNull() && m_port_ranges_isValid;

    m_rule_id_isValid = ::OpenAPI::fromJsonValue(m_rule_id, json[QString("rule_id")]);
    m_rule_id_isSet = !json[QString("rule_id")].isNull() && m_rule_id_isValid;

    m_section_id_isValid = ::OpenAPI::fromJsonValue(m_section_id, json[QString("section_id")]);
    m_section_id_isSet = !json[QString("section_id")].isNull() && m_section_id_isValid;

    m_section_name_isValid = ::OpenAPI::fromJsonValue(m_section_name, json[QString("section_name")]);
    m_section_name_isSet = !json[QString("section_name")].isNull() && m_section_name_isValid;

    m_sequence_number_isValid = ::OpenAPI::fromJsonValue(m_sequence_number, json[QString("sequence_number")]);
    m_sequence_number_isSet = !json[QString("sequence_number")].isNull() && m_sequence_number_isValid;

    m_service_any_isValid = ::OpenAPI::fromJsonValue(m_service_any, json[QString("service_any")]);
    m_service_any_isSet = !json[QString("service_any")].isNull() && m_service_any_isValid;

    m_services_isValid = ::OpenAPI::fromJsonValue(m_services, json[QString("services")]);
    m_services_isSet = !json[QString("services")].isNull() && m_services_isValid;

    m_source_any_isValid = ::OpenAPI::fromJsonValue(m_source_any, json[QString("source_any")]);
    m_source_any_isSet = !json[QString("source_any")].isNull() && m_source_any_isValid;

    m_source_inversion_isValid = ::OpenAPI::fromJsonValue(m_source_inversion, json[QString("source_inversion")]);
    m_source_inversion_isSet = !json[QString("source_inversion")].isNull() && m_source_inversion_isValid;

    m_sources_isValid = ::OpenAPI::fromJsonValue(m_sources, json[QString("sources")]);
    m_sources_isSet = !json[QString("sources")].isNull() && m_sources_isValid;

    m_direction_isValid = ::OpenAPI::fromJsonValue(m_direction, json[QString("direction")]);
    m_direction_isSet = !json[QString("direction")].isNull() && m_direction_isValid;

    m_owner_security_group_isValid = ::OpenAPI::fromJsonValue(m_owner_security_group, json[QString("owner_security_group")]);
    m_owner_security_group_isSet = !json[QString("owner_security_group")].isNull() && m_owner_security_group_isValid;

    m_vpc_isValid = ::OpenAPI::fromJsonValue(m_vpc, json[QString("vpc")]);
    m_vpc_isSet = !json[QString("vpc")].isNull() && m_vpc_isValid;
}

QString OAIEC2SGFirewallRule::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEC2SGFirewallRule::asJsonObject() const {
    QJsonObject obj;
    if (m_entity_id_isSet) {
        obj.insert(QString("entity_id"), ::OpenAPI::toJsonValue(m_entity_id));
    }
    if (m_entity_type.isSet()) {
        obj.insert(QString("entity_type"), ::OpenAPI::toJsonValue(m_entity_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_action.isSet()) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_destination_any_isSet) {
        obj.insert(QString("destination_any"), ::OpenAPI::toJsonValue(m_destination_any));
    }
    if (m_destination_inversion_isSet) {
        obj.insert(QString("destination_inversion"), ::OpenAPI::toJsonValue(m_destination_inversion));
    }
    if (m_destinations.size() > 0) {
        obj.insert(QString("destinations"), ::OpenAPI::toJsonValue(m_destinations));
    }
    if (m_disabled_isSet) {
        obj.insert(QString("disabled"), ::OpenAPI::toJsonValue(m_disabled));
    }
    if (m_port_ranges.size() > 0) {
        obj.insert(QString("port_ranges"), ::OpenAPI::toJsonValue(m_port_ranges));
    }
    if (m_rule_id_isSet) {
        obj.insert(QString("rule_id"), ::OpenAPI::toJsonValue(m_rule_id));
    }
    if (m_section_id_isSet) {
        obj.insert(QString("section_id"), ::OpenAPI::toJsonValue(m_section_id));
    }
    if (m_section_name_isSet) {
        obj.insert(QString("section_name"), ::OpenAPI::toJsonValue(m_section_name));
    }
    if (m_sequence_number_isSet) {
        obj.insert(QString("sequence_number"), ::OpenAPI::toJsonValue(m_sequence_number));
    }
    if (m_service_any_isSet) {
        obj.insert(QString("service_any"), ::OpenAPI::toJsonValue(m_service_any));
    }
    if (m_services.size() > 0) {
        obj.insert(QString("services"), ::OpenAPI::toJsonValue(m_services));
    }
    if (m_source_any_isSet) {
        obj.insert(QString("source_any"), ::OpenAPI::toJsonValue(m_source_any));
    }
    if (m_source_inversion_isSet) {
        obj.insert(QString("source_inversion"), ::OpenAPI::toJsonValue(m_source_inversion));
    }
    if (m_sources.size() > 0) {
        obj.insert(QString("sources"), ::OpenAPI::toJsonValue(m_sources));
    }
    if (m_direction.isSet()) {
        obj.insert(QString("direction"), ::OpenAPI::toJsonValue(m_direction));
    }
    if (m_owner_security_group.isSet()) {
        obj.insert(QString("owner_security_group"), ::OpenAPI::toJsonValue(m_owner_security_group));
    }
    if (m_vpc.isSet()) {
        obj.insert(QString("vpc"), ::OpenAPI::toJsonValue(m_vpc));
    }
    return obj;
}

QString OAIEC2SGFirewallRule::getEntityId() const {
    return m_entity_id;
}
void OAIEC2SGFirewallRule::setEntityId(const QString &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAIEC2SGFirewallRule::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAIEC2SGFirewallRule::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

OAIEntityType OAIEC2SGFirewallRule::getEntityType() const {
    return m_entity_type;
}
void OAIEC2SGFirewallRule::setEntityType(const OAIEntityType &entity_type) {
    m_entity_type = entity_type;
    m_entity_type_isSet = true;
}

bool OAIEC2SGFirewallRule::is_entity_type_Set() const{
    return m_entity_type_isSet;
}

bool OAIEC2SGFirewallRule::is_entity_type_Valid() const{
    return m_entity_type_isValid;
}

QString OAIEC2SGFirewallRule::getName() const {
    return m_name;
}
void OAIEC2SGFirewallRule::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIEC2SGFirewallRule::is_name_Set() const{
    return m_name_isSet;
}

bool OAIEC2SGFirewallRule::is_name_Valid() const{
    return m_name_isValid;
}

OAIFirewallAction OAIEC2SGFirewallRule::getAction() const {
    return m_action;
}
void OAIEC2SGFirewallRule::setAction(const OAIFirewallAction &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIEC2SGFirewallRule::is_action_Set() const{
    return m_action_isSet;
}

bool OAIEC2SGFirewallRule::is_action_Valid() const{
    return m_action_isValid;
}

bool OAIEC2SGFirewallRule::isDestinationAny() const {
    return m_destination_any;
}
void OAIEC2SGFirewallRule::setDestinationAny(const bool &destination_any) {
    m_destination_any = destination_any;
    m_destination_any_isSet = true;
}

bool OAIEC2SGFirewallRule::is_destination_any_Set() const{
    return m_destination_any_isSet;
}

bool OAIEC2SGFirewallRule::is_destination_any_Valid() const{
    return m_destination_any_isValid;
}

bool OAIEC2SGFirewallRule::isDestinationInversion() const {
    return m_destination_inversion;
}
void OAIEC2SGFirewallRule::setDestinationInversion(const bool &destination_inversion) {
    m_destination_inversion = destination_inversion;
    m_destination_inversion_isSet = true;
}

bool OAIEC2SGFirewallRule::is_destination_inversion_Set() const{
    return m_destination_inversion_isSet;
}

bool OAIEC2SGFirewallRule::is_destination_inversion_Valid() const{
    return m_destination_inversion_isValid;
}

QList<OAIReference> OAIEC2SGFirewallRule::getDestinations() const {
    return m_destinations;
}
void OAIEC2SGFirewallRule::setDestinations(const QList<OAIReference> &destinations) {
    m_destinations = destinations;
    m_destinations_isSet = true;
}

bool OAIEC2SGFirewallRule::is_destinations_Set() const{
    return m_destinations_isSet;
}

bool OAIEC2SGFirewallRule::is_destinations_Valid() const{
    return m_destinations_isValid;
}

bool OAIEC2SGFirewallRule::isDisabled() const {
    return m_disabled;
}
void OAIEC2SGFirewallRule::setDisabled(const bool &disabled) {
    m_disabled = disabled;
    m_disabled_isSet = true;
}

bool OAIEC2SGFirewallRule::is_disabled_Set() const{
    return m_disabled_isSet;
}

bool OAIEC2SGFirewallRule::is_disabled_Valid() const{
    return m_disabled_isValid;
}

QList<OAIPortRange> OAIEC2SGFirewallRule::getPortRanges() const {
    return m_port_ranges;
}
void OAIEC2SGFirewallRule::setPortRanges(const QList<OAIPortRange> &port_ranges) {
    m_port_ranges = port_ranges;
    m_port_ranges_isSet = true;
}

bool OAIEC2SGFirewallRule::is_port_ranges_Set() const{
    return m_port_ranges_isSet;
}

bool OAIEC2SGFirewallRule::is_port_ranges_Valid() const{
    return m_port_ranges_isValid;
}

QString OAIEC2SGFirewallRule::getRuleId() const {
    return m_rule_id;
}
void OAIEC2SGFirewallRule::setRuleId(const QString &rule_id) {
    m_rule_id = rule_id;
    m_rule_id_isSet = true;
}

bool OAIEC2SGFirewallRule::is_rule_id_Set() const{
    return m_rule_id_isSet;
}

bool OAIEC2SGFirewallRule::is_rule_id_Valid() const{
    return m_rule_id_isValid;
}

QString OAIEC2SGFirewallRule::getSectionId() const {
    return m_section_id;
}
void OAIEC2SGFirewallRule::setSectionId(const QString &section_id) {
    m_section_id = section_id;
    m_section_id_isSet = true;
}

bool OAIEC2SGFirewallRule::is_section_id_Set() const{
    return m_section_id_isSet;
}

bool OAIEC2SGFirewallRule::is_section_id_Valid() const{
    return m_section_id_isValid;
}

QString OAIEC2SGFirewallRule::getSectionName() const {
    return m_section_name;
}
void OAIEC2SGFirewallRule::setSectionName(const QString &section_name) {
    m_section_name = section_name;
    m_section_name_isSet = true;
}

bool OAIEC2SGFirewallRule::is_section_name_Set() const{
    return m_section_name_isSet;
}

bool OAIEC2SGFirewallRule::is_section_name_Valid() const{
    return m_section_name_isValid;
}

qint32 OAIEC2SGFirewallRule::getSequenceNumber() const {
    return m_sequence_number;
}
void OAIEC2SGFirewallRule::setSequenceNumber(const qint32 &sequence_number) {
    m_sequence_number = sequence_number;
    m_sequence_number_isSet = true;
}

bool OAIEC2SGFirewallRule::is_sequence_number_Set() const{
    return m_sequence_number_isSet;
}

bool OAIEC2SGFirewallRule::is_sequence_number_Valid() const{
    return m_sequence_number_isValid;
}

bool OAIEC2SGFirewallRule::isServiceAny() const {
    return m_service_any;
}
void OAIEC2SGFirewallRule::setServiceAny(const bool &service_any) {
    m_service_any = service_any;
    m_service_any_isSet = true;
}

bool OAIEC2SGFirewallRule::is_service_any_Set() const{
    return m_service_any_isSet;
}

bool OAIEC2SGFirewallRule::is_service_any_Valid() const{
    return m_service_any_isValid;
}

QList<OAIReference> OAIEC2SGFirewallRule::getServices() const {
    return m_services;
}
void OAIEC2SGFirewallRule::setServices(const QList<OAIReference> &services) {
    m_services = services;
    m_services_isSet = true;
}

bool OAIEC2SGFirewallRule::is_services_Set() const{
    return m_services_isSet;
}

bool OAIEC2SGFirewallRule::is_services_Valid() const{
    return m_services_isValid;
}

bool OAIEC2SGFirewallRule::isSourceAny() const {
    return m_source_any;
}
void OAIEC2SGFirewallRule::setSourceAny(const bool &source_any) {
    m_source_any = source_any;
    m_source_any_isSet = true;
}

bool OAIEC2SGFirewallRule::is_source_any_Set() const{
    return m_source_any_isSet;
}

bool OAIEC2SGFirewallRule::is_source_any_Valid() const{
    return m_source_any_isValid;
}

bool OAIEC2SGFirewallRule::isSourceInversion() const {
    return m_source_inversion;
}
void OAIEC2SGFirewallRule::setSourceInversion(const bool &source_inversion) {
    m_source_inversion = source_inversion;
    m_source_inversion_isSet = true;
}

bool OAIEC2SGFirewallRule::is_source_inversion_Set() const{
    return m_source_inversion_isSet;
}

bool OAIEC2SGFirewallRule::is_source_inversion_Valid() const{
    return m_source_inversion_isValid;
}

QList<OAIReference> OAIEC2SGFirewallRule::getSources() const {
    return m_sources;
}
void OAIEC2SGFirewallRule::setSources(const QList<OAIReference> &sources) {
    m_sources = sources;
    m_sources_isSet = true;
}

bool OAIEC2SGFirewallRule::is_sources_Set() const{
    return m_sources_isSet;
}

bool OAIEC2SGFirewallRule::is_sources_Valid() const{
    return m_sources_isValid;
}

OAIEC2FirewallDirection OAIEC2SGFirewallRule::getDirection() const {
    return m_direction;
}
void OAIEC2SGFirewallRule::setDirection(const OAIEC2FirewallDirection &direction) {
    m_direction = direction;
    m_direction_isSet = true;
}

bool OAIEC2SGFirewallRule::is_direction_Set() const{
    return m_direction_isSet;
}

bool OAIEC2SGFirewallRule::is_direction_Valid() const{
    return m_direction_isValid;
}

OAIReference OAIEC2SGFirewallRule::getOwnerSecurityGroup() const {
    return m_owner_security_group;
}
void OAIEC2SGFirewallRule::setOwnerSecurityGroup(const OAIReference &owner_security_group) {
    m_owner_security_group = owner_security_group;
    m_owner_security_group_isSet = true;
}

bool OAIEC2SGFirewallRule::is_owner_security_group_Set() const{
    return m_owner_security_group_isSet;
}

bool OAIEC2SGFirewallRule::is_owner_security_group_Valid() const{
    return m_owner_security_group_isValid;
}

OAIReference OAIEC2SGFirewallRule::getVpc() const {
    return m_vpc;
}
void OAIEC2SGFirewallRule::setVpc(const OAIReference &vpc) {
    m_vpc = vpc;
    m_vpc_isSet = true;
}

bool OAIEC2SGFirewallRule::is_vpc_Set() const{
    return m_vpc_isSet;
}

bool OAIEC2SGFirewallRule::is_vpc_Valid() const{
    return m_vpc_isValid;
}

bool OAIEC2SGFirewallRule::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_entity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_action.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_destination_any_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_destination_inversion_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_destinations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_disabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_port_ranges.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rule_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_section_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_section_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sequence_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_any_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_services.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_any_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_inversion_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_direction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_security_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vpc.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEC2SGFirewallRule::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
