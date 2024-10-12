/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITransparentDataEncryptionActivityProperties.h
 *
 * Represents the properties of a database transparent data encryption Scan.
 */

#ifndef OAITransparentDataEncryptionActivityProperties_H
#define OAITransparentDataEncryptionActivityProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITransparentDataEncryptionActivityProperties : public OAIObject {
public:
    OAITransparentDataEncryptionActivityProperties();
    OAITransparentDataEncryptionActivityProperties(QString json);
    ~OAITransparentDataEncryptionActivityProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getPercentComplete() const;
    void setPercentComplete(const float &percent_complete);
    bool is_percent_complete_Set() const;
    bool is_percent_complete_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_percent_complete;
    bool m_percent_complete_isSet;
    bool m_percent_complete_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITransparentDataEncryptionActivityProperties)

#endif // OAITransparentDataEncryptionActivityProperties_H
