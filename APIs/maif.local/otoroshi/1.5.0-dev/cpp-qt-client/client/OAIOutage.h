/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOutage.h
 *
 * An outage by the Snow Monkey on a service
 */

#ifndef OAIOutage_H
#define OAIOutage_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOutage : public OAIObject {
public:
    OAIOutage();
    OAIOutage(QString json);
    ~OAIOutage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescriptorId() const;
    void setDescriptorId(const QString &descriptor_id);
    bool is_descriptor_id_Set() const;
    bool is_descriptor_id_Valid() const;

    QString getDescriptorName() const;
    void setDescriptorName(const QString &descriptor_name);
    bool is_descriptor_name_Set() const;
    bool is_descriptor_name_Valid() const;

    qint32 getDuration() const;
    void setDuration(const qint32 &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getUntil() const;
    void setUntil(const QString &until);
    bool is_until_Set() const;
    bool is_until_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_descriptor_id;
    bool m_descriptor_id_isSet;
    bool m_descriptor_id_isValid;

    QString m_descriptor_name;
    bool m_descriptor_name_isSet;
    bool m_descriptor_name_isValid;

    qint32 m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_until;
    bool m_until_isSet;
    bool m_until_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOutage)

#endif // OAIOutage_H
