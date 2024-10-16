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
 * OAIReleaseDestinationResponse.h
 *
 * 
 */

#ifndef OAIReleaseDestinationResponse_H
#define OAIReleaseDestinationResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReleaseDestinationResponse : public OAIObject {
public:
    OAIReleaseDestinationResponse();
    OAIReleaseDestinationResponse(QString json);
    ~OAIReleaseDestinationResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isMandatoryUpdate() const;
    void setMandatoryUpdate(const bool &mandatory_update);
    bool is_mandatory_update_Set() const;
    bool is_mandatory_update_Valid() const;

    QString getProvisioningStatusUrl() const;
    void setProvisioningStatusUrl(const QString &provisioning_status_url);
    bool is_provisioning_status_url_Set() const;
    bool is_provisioning_status_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_mandatory_update;
    bool m_mandatory_update_isSet;
    bool m_mandatory_update_isValid;

    QString m_provisioning_status_url;
    bool m_provisioning_status_url_isSet;
    bool m_provisioning_status_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReleaseDestinationResponse)

#endif // OAIReleaseDestinationResponse_H
