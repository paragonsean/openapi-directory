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
 * OAIUpdateKeyVaultMetaInfo.h
 *
 * The Key Vault update information used for user managed key rotation.
 */

#ifndef OAIUpdateKeyVaultMetaInfo_H
#define OAIUpdateKeyVaultMetaInfo_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateKeyVaultMetaInfo : public OAIObject {
public:
    OAIUpdateKeyVaultMetaInfo();
    OAIUpdateKeyVaultMetaInfo(QString json);
    ~OAIUpdateKeyVaultMetaInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEncryptionKeyVersion() const;
    void setEncryptionKeyVersion(const QString &encryption_key_version);
    bool is_encryption_key_version_Set() const;
    bool is_encryption_key_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_encryption_key_version;
    bool m_encryption_key_version_isSet;
    bool m_encryption_key_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateKeyVaultMetaInfo)

#endif // OAIUpdateKeyVaultMetaInfo_H
