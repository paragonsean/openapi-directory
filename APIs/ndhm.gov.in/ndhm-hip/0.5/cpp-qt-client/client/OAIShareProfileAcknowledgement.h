/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShareProfileAcknowledgement.h
 *
 * 
 */

#ifndef OAIShareProfileAcknowledgement_H
#define OAIShareProfileAcknowledgement_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShareProfileAcknowledgement : public OAIObject {
public:
    OAIShareProfileAcknowledgement();
    OAIShareProfileAcknowledgement(QString json);
    ~OAIShareProfileAcknowledgement() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHealthId() const;
    void setHealthId(const QString &health_id);
    bool is_health_id_Set() const;
    bool is_health_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_health_id;
    bool m_health_id_isSet;
    bool m_health_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShareProfileAcknowledgement)

#endif // OAIShareProfileAcknowledgement_H
