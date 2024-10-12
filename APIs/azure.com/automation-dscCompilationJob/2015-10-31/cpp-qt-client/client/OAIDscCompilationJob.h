/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDscCompilationJob.h
 *
 * Definition of the Dsc Compilation job.
 */

#ifndef OAIDscCompilationJob_H
#define OAIDscCompilationJob_H

#include <QJsonObject>

#include "OAIDscCompilationJobProperties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDscCompilationJobProperties;

class OAIDscCompilationJob : public OAIObject {
public:
    OAIDscCompilationJob();
    OAIDscCompilationJob(QString json);
    ~OAIDscCompilationJob() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIDscCompilationJobProperties getProperties() const;
    void setProperties(const OAIDscCompilationJobProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

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

    OAIDscCompilationJobProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDscCompilationJob)

#endif // OAIDscCompilationJob_H
