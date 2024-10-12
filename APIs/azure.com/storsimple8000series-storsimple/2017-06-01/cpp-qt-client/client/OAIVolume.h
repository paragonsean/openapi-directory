/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVolume.h
 *
 * The volume.
 */

#ifndef OAIVolume_H
#define OAIVolume_H

#include <QJsonObject>

#include "OAIVolumeProperties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVolumeProperties;

class OAIVolume : public OAIObject {
public:
    OAIVolume();
    OAIVolume(QString json);
    ~OAIVolume() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIVolumeProperties getProperties() const;
    void setProperties(const OAIVolumeProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIVolumeProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVolume)

#endif // OAIVolume_H
