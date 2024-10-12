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
 * OAIVxlanLayer2Network.h
 *
 * 
 */

#ifndef OAIVxlanLayer2Network_H
#define OAIVxlanLayer2Network_H

#include <QJsonObject>

#include "OAIBaseL2Network.h"
#include "OAIEntityType.h"
#include "OAIReference.h"
#include "OAIScopeEnum.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReference;

class OAIVxlanLayer2Network : public OAIObject {
public:
    OAIVxlanLayer2Network();
    OAIVxlanLayer2Network(QString json);
    ~OAIVxlanLayer2Network() override;

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

    QList<QString> getGateways() const;
    void setGateways(const QList<QString> &gateways);
    bool is_gateways_Set() const;
    bool is_gateways_Valid() const;

    QList<QString> getNetworkAddresses() const;
    void setNetworkAddresses(const QList<QString> &network_addresses);
    bool is_network_addresses_Set() const;
    bool is_network_addresses_Valid() const;

    QList<OAIReference> getNsxManagers() const;
    void setNsxManagers(const QList<OAIReference> &nsx_managers);
    bool is_nsx_managers_Set() const;
    bool is_nsx_managers_Valid() const;

    OAIScopeEnum getScope() const;
    void setScope(const OAIScopeEnum &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    qint32 getSegmentId() const;
    void setSegmentId(const qint32 &segment_id);
    bool is_segment_id_Set() const;
    bool is_segment_id_Valid() const;

    QList<OAIReference> getVteps() const;
    void setVteps(const QList<OAIReference> &vteps);
    bool is_vteps_Set() const;
    bool is_vteps_Valid() const;

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

    QList<QString> m_gateways;
    bool m_gateways_isSet;
    bool m_gateways_isValid;

    QList<QString> m_network_addresses;
    bool m_network_addresses_isSet;
    bool m_network_addresses_isValid;

    QList<OAIReference> m_nsx_managers;
    bool m_nsx_managers_isSet;
    bool m_nsx_managers_isValid;

    OAIScopeEnum m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    qint32 m_segment_id;
    bool m_segment_id_isSet;
    bool m_segment_id_isValid;

    QList<OAIReference> m_vteps;
    bool m_vteps_isSet;
    bool m_vteps_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVxlanLayer2Network)

#endif // OAIVxlanLayer2Network_H
