/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDiaryAppointmentTypeModel.h
 *
 * Represents a diary appointment type.
 */

#ifndef OAIDiaryAppointmentTypeModel_H
#define OAIDiaryAppointmentTypeModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDiaryAppointmentTypeModel : public OAIObject {
public:
    OAIDiaryAppointmentTypeModel();
    OAIDiaryAppointmentTypeModel(QString json);
    ~OAIDiaryAppointmentTypeModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    QString getSystemType() const;
    void setSystemType(const QString &system_type);
    bool is_system_type_Set() const;
    bool is_system_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    QString m_system_type;
    bool m_system_type_isSet;
    bool m_system_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDiaryAppointmentTypeModel)

#endif // OAIDiaryAppointmentTypeModel_H
