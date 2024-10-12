/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApplicationPackage.h
 *
 * An application package which represents a particular version of an application.
 */

#ifndef OAIApplicationPackage_H
#define OAIApplicationPackage_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationPackage : public OAIObject {
public:
    OAIApplicationPackage();
    OAIApplicationPackage(QString json);
    ~OAIApplicationPackage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QDateTime getLastActivationTime() const;
    void setLastActivationTime(const QDateTime &last_activation_time);
    bool is_last_activation_time_Set() const;
    bool is_last_activation_time_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStorageUrl() const;
    void setStorageUrl(const QString &storage_url);
    bool is_storage_url_Set() const;
    bool is_storage_url_Valid() const;

    QDateTime getStorageUrlExpiry() const;
    void setStorageUrlExpiry(const QDateTime &storage_url_expiry);
    bool is_storage_url_expiry_Set() const;
    bool is_storage_url_expiry_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QDateTime m_last_activation_time;
    bool m_last_activation_time_isSet;
    bool m_last_activation_time_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_storage_url;
    bool m_storage_url_isSet;
    bool m_storage_url_isValid;

    QDateTime m_storage_url_expiry;
    bool m_storage_url_expiry_isSet;
    bool m_storage_url_expiry_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationPackage)

#endif // OAIApplicationPackage_H
