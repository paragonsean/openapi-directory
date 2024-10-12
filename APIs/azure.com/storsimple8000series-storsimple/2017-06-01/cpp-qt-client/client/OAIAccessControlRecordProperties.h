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
 * OAIAccessControlRecordProperties.h
 *
 * The properties of access control record.
 */

#ifndef OAIAccessControlRecordProperties_H
#define OAIAccessControlRecordProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccessControlRecordProperties : public OAIObject {
public:
    OAIAccessControlRecordProperties();
    OAIAccessControlRecordProperties(QString json);
    ~OAIAccessControlRecordProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getInitiatorName() const;
    void setInitiatorName(const QString &initiator_name);
    bool is_initiator_name_Set() const;
    bool is_initiator_name_Valid() const;

    qint32 getVolumeCount() const;
    void setVolumeCount(const qint32 &volume_count);
    bool is_volume_count_Set() const;
    bool is_volume_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_initiator_name;
    bool m_initiator_name_isSet;
    bool m_initiator_name_isValid;

    qint32 m_volume_count;
    bool m_volume_count_isSet;
    bool m_volume_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccessControlRecordProperties)

#endif // OAIAccessControlRecordProperties_H
