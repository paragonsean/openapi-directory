/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIContentSource.h
 *
 * Definition of the content source.
 */

#ifndef OAIContentSource_H
#define OAIContentSource_H

#include <QJsonObject>

#include "OAIContentHash.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContentHash;

class OAIContentSource : public OAIObject {
public:
    OAIContentSource();
    OAIContentSource(QString json);
    ~OAIContentSource() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContentHash getHash() const;
    void setHash(const OAIContentHash &hash);
    bool is_hash_Set() const;
    bool is_hash_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContentHash m_hash;
    bool m_hash_isSet;
    bool m_hash_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContentSource)

#endif // OAIContentSource_H
