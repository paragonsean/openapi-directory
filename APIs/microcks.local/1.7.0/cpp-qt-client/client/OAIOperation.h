/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOperation.h
 *
 * An Operation of a Service or API
 */

#ifndef OAIOperation_H
#define OAIOperation_H

#include <QJsonObject>

#include "OAIBinding.h"
#include "OAIParameterConstraint.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBinding;
class OAIParameterConstraint;

class OAIOperation : public OAIObject {
public:
    OAIOperation();
    OAIOperation(QString json);
    ~OAIOperation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, OAIBinding> getBindings() const;
    void setBindings(const QMap<QString, OAIBinding> &bindings);
    bool is_bindings_Set() const;
    bool is_bindings_Valid() const;

    double getDefaultDelay() const;
    void setDefaultDelay(const double &default_delay);
    bool is_default_delay_Set() const;
    bool is_default_delay_Valid() const;

    QString getDispatcher() const;
    void setDispatcher(const QString &dispatcher);
    bool is_dispatcher_Set() const;
    bool is_dispatcher_Valid() const;

    QString getDispatcherRules() const;
    void setDispatcherRules(const QString &dispatcher_rules);
    bool is_dispatcher_rules_Set() const;
    bool is_dispatcher_rules_Valid() const;

    QString getInputName() const;
    void setInputName(const QString &input_name);
    bool is_input_name_Set() const;
    bool is_input_name_Valid() const;

    QString getMethod() const;
    void setMethod(const QString &method);
    bool is_method_Set() const;
    bool is_method_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOutputName() const;
    void setOutputName(const QString &output_name);
    bool is_output_name_Set() const;
    bool is_output_name_Valid() const;

    QList<OAIParameterConstraint> getParameterContraints() const;
    void setParameterContraints(const QList<OAIParameterConstraint> &parameter_contraints);
    bool is_parameter_contraints_Set() const;
    bool is_parameter_contraints_Valid() const;

    QList<QString> getResourcePaths() const;
    void setResourcePaths(const QList<QString> &resource_paths);
    bool is_resource_paths_Set() const;
    bool is_resource_paths_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, OAIBinding> m_bindings;
    bool m_bindings_isSet;
    bool m_bindings_isValid;

    double m_default_delay;
    bool m_default_delay_isSet;
    bool m_default_delay_isValid;

    QString m_dispatcher;
    bool m_dispatcher_isSet;
    bool m_dispatcher_isValid;

    QString m_dispatcher_rules;
    bool m_dispatcher_rules_isSet;
    bool m_dispatcher_rules_isValid;

    QString m_input_name;
    bool m_input_name_isSet;
    bool m_input_name_isValid;

    QString m_method;
    bool m_method_isSet;
    bool m_method_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_output_name;
    bool m_output_name_isSet;
    bool m_output_name_isValid;

    QList<OAIParameterConstraint> m_parameter_contraints;
    bool m_parameter_contraints_isSet;
    bool m_parameter_contraints_isValid;

    QList<QString> m_resource_paths;
    bool m_resource_paths_isSet;
    bool m_resource_paths_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOperation)

#endif // OAIOperation_H
