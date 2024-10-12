/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITrustedIdProviderProperties.h
 *
 * The trusted identity provider properties.
 */

#ifndef OAITrustedIdProviderProperties_H
#define OAITrustedIdProviderProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITrustedIdProviderProperties : public OAIObject {
public:
    OAITrustedIdProviderProperties();
    OAITrustedIdProviderProperties(QString json);
    ~OAITrustedIdProviderProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIdProvider() const;
    void setIdProvider(const QString &id_provider);
    bool is_id_provider_Set() const;
    bool is_id_provider_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id_provider;
    bool m_id_provider_isSet;
    bool m_id_provider_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrustedIdProviderProperties)

#endif // OAITrustedIdProviderProperties_H
