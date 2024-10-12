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
 * OAIModelPythonSection.h
 *
 * 
 */

#ifndef OAIModelPythonSection_H
#define OAIModelPythonSection_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIModelPythonSection : public OAIObject {
public:
    OAIModelPythonSection();
    OAIModelPythonSection(QString json);
    ~OAIModelPythonSection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseCondaEnvironment() const;
    void setBaseCondaEnvironment(const QString &base_conda_environment);
    bool is_base_conda_environment_Set() const;
    bool is_base_conda_environment_Valid() const;

    OAIObject getCondaDependencies() const;
    void setCondaDependencies(const OAIObject &conda_dependencies);
    bool is_conda_dependencies_Set() const;
    bool is_conda_dependencies_Valid() const;

    QString getInterpreterPath() const;
    void setInterpreterPath(const QString &interpreter_path);
    bool is_interpreter_path_Set() const;
    bool is_interpreter_path_Valid() const;

    bool isUserManagedDependencies() const;
    void setUserManagedDependencies(const bool &user_managed_dependencies);
    bool is_user_managed_dependencies_Set() const;
    bool is_user_managed_dependencies_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_base_conda_environment;
    bool m_base_conda_environment_isSet;
    bool m_base_conda_environment_isValid;

    OAIObject m_conda_dependencies;
    bool m_conda_dependencies_isSet;
    bool m_conda_dependencies_isValid;

    QString m_interpreter_path;
    bool m_interpreter_path_isSet;
    bool m_interpreter_path_isValid;

    bool m_user_managed_dependencies;
    bool m_user_managed_dependencies_isSet;
    bool m_user_managed_dependencies_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIModelPythonSection)

#endif // OAIModelPythonSection_H
