/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITargetRuntime.h
 *
 * The target runtime.
 */

#ifndef OAITargetRuntime_H
#define OAITargetRuntime_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITargetRuntime : public OAIObject {
public:
    OAITargetRuntime();
    OAITargetRuntime(QString json);
    ~OAITargetRuntime() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getOsType() const;
    void setOsType(const QString &os_type);
    bool is_os_type_Set() const;
    bool is_os_type_Valid() const;

    QMap<QString, QString> getProperties() const;
    void setProperties(const QMap<QString, QString> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getRuntimeType() const;
    void setRuntimeType(const QString &runtime_type);
    bool is_runtime_type_Set() const;
    bool is_runtime_type_Valid() const;

    QString getTargetArchitecture() const;
    void setTargetArchitecture(const QString &target_architecture);
    bool is_target_architecture_Set() const;
    bool is_target_architecture_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_os_type;
    bool m_os_type_isSet;
    bool m_os_type_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_runtime_type;
    bool m_runtime_type_isSet;
    bool m_runtime_type_isValid;

    QString m_target_architecture;
    bool m_target_architecture_isSet;
    bool m_target_architecture_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITargetRuntime)

#endif // OAITargetRuntime_H
