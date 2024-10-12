/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICertificateCreateOrUpdateProperties.h
 *
 * Certificate properties for create operations
 */

#ifndef OAICertificateCreateOrUpdateProperties_H
#define OAICertificateCreateOrUpdateProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICertificateCreateOrUpdateProperties : public OAIObject {
public:
    OAICertificateCreateOrUpdateProperties();
    OAICertificateCreateOrUpdateProperties(QString json);
    ~OAICertificateCreateOrUpdateProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getData() const;
    void setData(const QString &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QString getThumbprint() const;
    void setThumbprint(const QString &thumbprint);
    bool is_thumbprint_Set() const;
    bool is_thumbprint_Valid() const;

    QString getThumbprintAlgorithm() const;
    void setThumbprintAlgorithm(const QString &thumbprint_algorithm);
    bool is_thumbprint_algorithm_Set() const;
    bool is_thumbprint_algorithm_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QString m_thumbprint;
    bool m_thumbprint_isSet;
    bool m_thumbprint_isValid;

    QString m_thumbprint_algorithm;
    bool m_thumbprint_algorithm_isSet;
    bool m_thumbprint_algorithm_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICertificateCreateOrUpdateProperties)

#endif // OAICertificateCreateOrUpdateProperties_H
