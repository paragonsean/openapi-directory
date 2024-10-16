/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppleMappingRequest.h
 *
 * Apple Mapping Request Type
 */

#ifndef OAIAppleMappingRequest_H
#define OAIAppleMappingRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppleMappingRequest : public OAIObject {
public:
    OAIAppleMappingRequest();
    OAIAppleMappingRequest(QString json);
    ~OAIAppleMappingRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppleId() const;
    void setAppleId(const QString &apple_id);
    bool is_apple_id_Set() const;
    bool is_apple_id_Valid() const;

    QString getBundleIdentifier() const;
    void setBundleIdentifier(const QString &bundle_identifier);
    bool is_bundle_identifier_Set() const;
    bool is_bundle_identifier_Valid() const;

    QString getServiceConnectionId() const;
    void setServiceConnectionId(const QString &service_connection_id);
    bool is_service_connection_id_Set() const;
    bool is_service_connection_id_Valid() const;

    QString getTeamIdentifier() const;
    void setTeamIdentifier(const QString &team_identifier);
    bool is_team_identifier_Set() const;
    bool is_team_identifier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_apple_id;
    bool m_apple_id_isSet;
    bool m_apple_id_isValid;

    QString m_bundle_identifier;
    bool m_bundle_identifier_isSet;
    bool m_bundle_identifier_isValid;

    QString m_service_connection_id;
    bool m_service_connection_id_isSet;
    bool m_service_connection_id_isValid;

    QString m_team_identifier;
    bool m_team_identifier_isSet;
    bool m_team_identifier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppleMappingRequest)

#endif // OAIAppleMappingRequest_H
