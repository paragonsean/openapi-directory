/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDealerDB_Models_LicenseActivation.h
 *
 * 
 */

#ifndef OAIDealerDB_Models_LicenseActivation_H
#define OAIDealerDB_Models_LicenseActivation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDealerDB_Models_LicenseActivation : public OAIObject {
public:
    OAIDealerDB_Models_LicenseActivation();
    OAIDealerDB_Models_LicenseActivation(QString json);
    ~OAIDealerDB_Models_LicenseActivation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getLicenseData() const;
    void setLicenseData(const QString &license_data);
    bool is_license_data_Set() const;
    bool is_license_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_license_data;
    bool m_license_data_isSet;
    bool m_license_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDealerDB_Models_LicenseActivation)

#endif // OAIDealerDB_Models_LicenseActivation_H
