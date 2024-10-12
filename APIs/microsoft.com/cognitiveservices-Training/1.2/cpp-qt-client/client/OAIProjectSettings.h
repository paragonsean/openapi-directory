/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectSettings.h
 *
 * Represents settings associated with a project
 */

#ifndef OAIProjectSettings_H
#define OAIProjectSettings_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProjectSettings : public OAIObject {
public:
    OAIProjectSettings();
    OAIProjectSettings(QString json);
    ~OAIProjectSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDomainId() const;
    void setDomainId(const QString &domain_id);
    bool is_domain_id_Set() const;
    bool is_domain_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_domain_id;
    bool m_domain_id_isSet;
    bool m_domain_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectSettings)

#endif // OAIProjectSettings_H
