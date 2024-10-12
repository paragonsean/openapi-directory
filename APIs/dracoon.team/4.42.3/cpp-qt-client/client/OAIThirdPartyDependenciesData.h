/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIThirdPartyDependenciesData.h
 *
 * Third-party dependency information
 */

#ifndef OAIThirdPartyDependenciesData_H
#define OAIThirdPartyDependenciesData_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIThirdPartyDependenciesData : public OAIObject {
public:
    OAIThirdPartyDependenciesData();
    OAIThirdPartyDependenciesData(QString json);
    ~OAIThirdPartyDependenciesData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArtifactId() const;
    void setArtifactId(const QString &artifact_id);
    bool is_artifact_id_Set() const;
    bool is_artifact_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getGroupId() const;
    void setGroupId(const QString &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<QString> getLicenses() const;
    void setLicenses(const QList<QString> &licenses);
    bool is_licenses_Set() const;
    bool is_licenses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_artifact_id;
    bool m_artifact_id_isSet;
    bool m_artifact_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<QString> m_licenses;
    bool m_licenses_isSet;
    bool m_licenses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIThirdPartyDependenciesData)

#endif // OAIThirdPartyDependenciesData_H
