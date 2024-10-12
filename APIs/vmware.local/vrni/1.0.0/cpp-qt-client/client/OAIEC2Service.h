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
 * OAIEC2Service.h
 *
 * 
 */

#ifndef OAIEC2Service_H
#define OAIEC2Service_H

#include <QJsonObject>

#include "OAIBaseService.h"
#include "OAIEntityType.h"
#include "OAIPortRange.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPortRange;

class OAIEC2Service : public OAIObject {
public:
    OAIEC2Service();
    OAIEC2Service(QString json);
    ~OAIEC2Service() override;

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

    QList<OAIPortRange> getPortRanges() const;
    void setPortRanges(const QList<OAIPortRange> &port_ranges);
    bool is_port_ranges_Set() const;
    bool is_port_ranges_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

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

    QList<OAIPortRange> m_port_ranges;
    bool m_port_ranges_isSet;
    bool m_port_ranges_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEC2Service)

#endif // OAIEC2Service_H
