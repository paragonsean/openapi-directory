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
 * OAILegacyDeploymentHistoryResponse_history_inner.h
 *
 * Information about a specific release.
 */

#ifndef OAILegacyDeploymentHistoryResponse_history_inner_H
#define OAILegacyDeploymentHistoryResponse_history_inner_H

#include <QJsonObject>

#include "OAILegacyCodePushReleaseResponse_package.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILegacyCodePushReleaseResponse_package;

class OAILegacyDeploymentHistoryResponse_history_inner : public OAIObject {
public:
    OAILegacyDeploymentHistoryResponse_history_inner();
    OAILegacyDeploymentHistoryResponse_history_inner(QString json);
    ~OAILegacyDeploymentHistoryResponse_history_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAILegacyCodePushReleaseResponse_package getAllOf() const;
    void setAllOf(const OAILegacyCodePushReleaseResponse_package &all_of);
    bool is_all_of_Set() const;
    bool is_all_of_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getOriginalDeployment() const;
    void setOriginalDeployment(const QString &original_deployment);
    bool is_original_deployment_Set() const;
    bool is_original_deployment_Valid() const;

    QString getOriginalLabel() const;
    void setOriginalLabel(const QString &original_label);
    bool is_original_label_Set() const;
    bool is_original_label_Valid() const;

    QString getPackageHash() const;
    void setPackageHash(const QString &package_hash);
    bool is_package_hash_Set() const;
    bool is_package_hash_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAILegacyCodePushReleaseResponse_package m_all_of;
    bool m_all_of_isSet;
    bool m_all_of_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_original_deployment;
    bool m_original_deployment_isSet;
    bool m_original_deployment_isValid;

    QString m_original_label;
    bool m_original_label_isSet;
    bool m_original_label_isValid;

    QString m_package_hash;
    bool m_package_hash_isSet;
    bool m_package_hash_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILegacyDeploymentHistoryResponse_history_inner)

#endif // OAILegacyDeploymentHistoryResponse_history_inner_H
