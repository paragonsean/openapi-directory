/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEnvironmentSetting.h
 *
 * Represents settings of an environment, from which environment instances would be created
 */

#ifndef OAIEnvironmentSetting_H
#define OAIEnvironmentSetting_H

#include <QJsonObject>

#include "OAIEnvironmentSettingProperties.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEnvironmentSettingProperties;

class OAIEnvironmentSetting : public OAIObject {
public:
    OAIEnvironmentSetting();
    OAIEnvironmentSetting(QString json);
    ~OAIEnvironmentSetting() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEnvironmentSettingProperties getProperties() const;
    void setProperties(const OAIEnvironmentSettingProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QMap<QString, QString> getTags() const;
    void setTags(const QMap<QString, QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEnvironmentSettingProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QMap<QString, QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEnvironmentSetting)

#endif // OAIEnvironmentSetting_H
