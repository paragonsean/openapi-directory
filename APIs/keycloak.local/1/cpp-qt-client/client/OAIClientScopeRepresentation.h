/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIClientScopeRepresentation.h
 *
 * 
 */

#ifndef OAIClientScopeRepresentation_H
#define OAIClientScopeRepresentation_H

#include <QJsonObject>

#include "OAIProtocolMapperRepresentation.h"
#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProtocolMapperRepresentation;

class OAIClientScopeRepresentation : public OAIObject {
public:
    OAIClientScopeRepresentation();
    OAIClientScopeRepresentation(QString json);
    ~OAIClientScopeRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QJsonValue> getAttributes() const;
    void setAttributes(const QMap<QString, QJsonValue> &attributes);
    bool is_attributes_Set() const;
    bool is_attributes_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

    QList<OAIProtocolMapperRepresentation> getProtocolMappers() const;
    void setProtocolMappers(const QList<OAIProtocolMapperRepresentation> &protocol_mappers);
    bool is_protocol_mappers_Set() const;
    bool is_protocol_mappers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QJsonValue> m_attributes;
    bool m_attributes_isSet;
    bool m_attributes_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;

    QList<OAIProtocolMapperRepresentation> m_protocol_mappers;
    bool m_protocol_mappers_isSet;
    bool m_protocol_mappers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIClientScopeRepresentation)

#endif // OAIClientScopeRepresentation_H
